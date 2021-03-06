import json
import tarfile
import zstandard as zstd
import os
import shutil


class Parser:
    """Parse twirl package files"""

    def __init__(
        self, package_location: str, tmpdir: str = "/tmp/twrl-parse." + str(os.getpid())
    ):
        """Package location and tmpdir"""
        if os.path.isfile(package_location):
            self.pkg = package_location
        else:
            raise FileNotFoundException(
                f"{package_location} is not a valid twirl package file."
            )
        if os.path.isdir(tmpdir):
            xtraslash = "/" if tmpdir[-1] != "/" else ""
            self.tmpdir = tmpdir + xtraslash
        else:
            status_code = os.system(f"mkdir -p {tmpdir}")
            if status_code != 0:
                raise FileNotFoundException(
                    f"{tmpdir} is not a valid directory. (Error {status_code})"
                )

    def load(self) -> list:
        """Extract File to Temp Dir"""
        dctx = zstd.ZstdDecompressor()
        with open(self.pkg, "rb") as zst, open(
            self.tmpdir + self.pkg.split(".")[0] + ".tar", "wb"
        ) as dest:
            dctx.copy_stream(zst, dest)
        self.tarfile = tarfile.open(self.tmpdir + self.pkg.split(".")[0] + ".tar")
        return [self.tmpdir + self.pkg.split(".")[0] + ".tar", self.tarfile]

    def pkginfo(self) -> dict:
        """Get info about the package (run load() first)"""
        stuff = self.tarfile.extractfile("pkginfo/PKGINFO")
        pkginfo_data = json.load(stuff)
        return pkginfo_data

    def extract_rootfs(self, dest: str) -> str:
        """Extract the package's contents to location specified in dest"""
        if os.path.isdir(dest):
            pass
        else:
            raise Exception(f"{dest} is not a valid folder.")
        tf = self.tarfile
        subdir_and_files = [
            tarinfo
            for tarinfo in tf.getmembers()
            if tarinfo.name.startswith("data/") and len(tarinfo.name) > 5
        ]
        tf.extractall(members=subdir_and_files, path=self.tmpdir)
        src = self.tmpdir + "data/"
        files = os.listdir(src)
        for file in files:
            shutil.move(src + file, dest)
        return dest

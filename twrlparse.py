import json
import tarfile
import zstandard as zstd
os = zstd.os


class Parser:
    """Parse gzip files"""

    def __init__(self, package_location, tmpdir="/tmp/twrl-parse."+str(os.getpid())):
        """Package location and tmpdir"""
        if os.path.isfile(package_location):
            self.pkg = package_location
        else:
            raise FileNotFoundException(
                f"{package_location} is not a valid twirl package file.")
        if os.path.isdir(tmpdir):
            xtraslash = "/" if tmpdir[-1] != "/" else ""
            self.tmpdir = tmpdir + xtraslash
        else:
            status_code = os.system(f"mkdir -p {tmpdir}")
            if status_code != 0:
                raise FileNotFoundException(
                    f"{tmpdir} is not a valid directory. (Error {status_code})")

    def load(self):
        """write it"""
        dctx = zstd.ZstdDecompressor()
        with open(self.pkg, "rb") as zst, open(self.tmpdir + self.pkg.split(".")[0] + ".tar", "wb") as dest:
            dctx.copy_stream(zst, dest)
        return [self.tmpdir + self.pkg.split(".")[0] + ".tar", tarfile.open(self.tmpdir + self.pkg.split(".")[0] + ".tar")]

    def pkginfo(self, tar_file : tarfile.TarFile):
        stuff = tar_file.read().strip().replace(b"\n", b"")
        pkginfo_data = json.loads(stuff)
        return pkginfo_data

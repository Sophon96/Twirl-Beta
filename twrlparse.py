import json
import tarfile
import zstandard as zstd
os = zstd.os


class Parser:
    """Parse twirl package files"""

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
        self.tarfile = tarfile.open(self.tmpdir + self.pkg.split(".")[0] + ".tar")
        return [self.tmpdir + self.pkg.split(".")[0] + ".tar", self.tarfile]


    def pkginfo(self):
        stuff = self.tarfile.extractfile("pkginfo/PKGINFO")
#        stuff = self.tarfile.read().strip().replace(b"\n", b"")
        pkginfo_data = json.load(stuff)
        return pkginfo_data

    def extract_rootfs(self,dest):
        if os.path.isdir(dest):
            pass
        else:
            raise Exception(f"{dest} is not a valid folder.")
        tf = self.tarfile
        res = tf.extractall(path=dest)
        return dest + "/" if dest[-1] != "/" else "" + self.pkg.split(".")[0]
        # use self.tarfile and extract to {dest}

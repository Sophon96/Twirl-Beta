class TwirlErrors(Exception):
    pass
class DownloadError(TwirlErrors):
    print("Package failed to dowwnload")
    pass
class ChecksumDoesntMatch(WTwirlErrors):
    print("Package checksum doesn't match, retry")
    pass
class PackageNotFound(TwirlErrors):
    print("Package unable to be found")
    pass
class PackageInstallFailed(TwirlErrors):
    print("Package failed to install")
    pass
class PackageAlreadyInstalled(TwirlErrors):
    print("Package is already installed")
    pass
class PackageConflicts(TwirlErrors):
    #needs to find and print conflicting packages
    print("Package conflicts with other installed package")
    pass


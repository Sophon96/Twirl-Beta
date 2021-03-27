class TwirlErrors(Exception):
    pass
class DownloadError(TwirlErrors):
    pass
class ChecksumDoesntMatch(TwirlErrors):
    pass
class PackageNotFound(TwirlErrors):
    pass
class PackageInstallFailed(TwirlErrors):
    pass
class PackageAlreadyInstalled(TwirlErrors):
    pass
class PackageConflicts(TwirlErrors):
    pass


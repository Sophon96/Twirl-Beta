class TwirlErrors(Exception):
    """Base class for all Twirl errors."""
    pass


class DownloadError(TwirlErrors):
    """The target package failed to download."""
    pass


class InetgrityError(TwirlErrors):
    """The checksum of the tarball doesn't match."""
    pass


class PackageNotFound(TwirlErrors):
    """The target package wasn't found/doesn't exist."""
    pass


class PackageInstallFailed(TwirlErrors):
    """The target package failed to install."""
    pass


class PackageAlreadyInstalled(TwirlErrors):
    """The target package is already installed."""
    pass


class PackageConflicts(TwirlErrors):
    """Target package conflicts with an already installed package."""
    pass

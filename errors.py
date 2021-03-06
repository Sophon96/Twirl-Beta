class TwirlErrors(Exception):
    """Base class for all Twirl errors."""


class DownloadError(TwirlErrors):
    """The target package failed to download."""


class InetgrityError(TwirlErrors):
    """The checksum of the tarball doesn't match."""


class PackageNotFound(TwirlErrors):
    """The target package wasn't found/doesn't exist."""


class PackageInstallFailed(TwirlErrors):
    """The target package failed to install."""


class PackageAlreadyInstalled(TwirlErrors):
    """The target package is already installed."""


class PackageConflicts(TwirlErrors):
    """Target package conflicts with an already installed package."""

from b_lambda_layer_common.package_version import PackageVersion


class Boto3Version(PackageVersion):
    """
    Deprecated ``boto3`` package version identifier.

    Use general ``PackageVersion`` class instead.
    """

    Boto3VersionType = PackageVersion.VersionType

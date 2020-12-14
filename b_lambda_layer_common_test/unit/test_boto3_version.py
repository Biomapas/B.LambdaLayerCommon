from b_lambda_layer_common.boto3_version import Boto3Version


def test_FUNC_from_string_version_WITH_string_version_EXPECT_version_created():
    """
    Test whether a version can be built from a string version.

    :return: No return.
    """
    version = Boto3Version.from_string_version('123')
    assert version.version_string == '123'
    assert version.version_type == Boto3Version.Boto3VersionType.SPECIFIC


def test_FUNC_latest_WITH_no_parameters_EXPECT_version_created():
    """
    Test whether the latest version can be built.

    :return: No return.
    """
    version = Boto3Version.latest()
    assert version.version_string is None
    assert version.version_type == Boto3Version.Boto3VersionType.LATEST


def test_FUNC_dont_install_WITH_no_parameters_EXPECT_version_created():
    """
    Test whether the version can be None.

    :return: No return.
    """
    version = Boto3Version.dont_install()
    assert version.version_string is None
    assert version.version_type == Boto3Version.Boto3VersionType.NONE

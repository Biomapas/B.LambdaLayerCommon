from b_lambda_layer_common.util.logging import LoggingManager


def test_FUNC_setup_logging_WITH_nothing_EXPECT_logging_successfully_set_up() -> None:
    """
    Checks whether the call succeeds.

    :return: No return.
    """
    LoggingManager().setup_logging()

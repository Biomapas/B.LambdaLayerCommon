from b_lambda_layer_common.util.do_not_update import DoNotUpdate


def test_FUNC_init_WITH_no_params_EXPECT_class_initiated() -> None:
    """
    Checks whether class initialization works.

    :return: No return.
    """
    DoNotUpdate()


def test_FUNC_init_WITH_no_params_EXPECT_class_is_type() -> None:
    """
    Checks whether class initialization works.

    :return: No return.
    """
    dnu1 = DoNotUpdate()
    dnu2 = DoNotUpdate

    assert dnu1 is dnu2

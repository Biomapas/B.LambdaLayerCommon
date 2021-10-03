from b_lambda_layer_common.ssm.refreshable import Refreshable


def test_FUNC_refresh_on_error_WITH_error_EXPECT_value_refreshed():
    """
    Test whether decorator works.

    :return: No return.
    """

    class DummyParameter(Refreshable):
        def __init__(self):
            super().__init__()

            self.called_counter = 0

        def update_value(self):
            self.called_counter += 1

    dummy_parameter = DummyParameter()

    @dummy_parameter.refresh_on_error()
    def dummy_function():
        raise Exception()

    try:
        dummy_function()
    except:
        pass

    assert dummy_parameter.called_counter == 1

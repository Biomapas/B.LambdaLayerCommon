from b_lambda_layer_common.source.python.b_lambda_layer_common.ssm.ssm_parameter import SSMParameter


def test_FUNC_value_WITH_fresh_parameter_EXPECT_value_fetched():
    """
    Test whether the parameter can fetch the value from SSM.

    :return: No return.
    """

    class SSMClient:
        def get_parameters(self, *args, **kwargs):
            return {
                'Parameters': [
                    {
                        'Name': 'TestParameter',
                        'Type': 'String',
                        'Value': 'StringValue123',
                        'Version': 123,
                    },
                ],
                'InvalidParameters': []
            }

    parameter = SSMParameter(
        param_name='TestParameter',
        ssm_client=SSMClient()
    )

    assert parameter.value == 'StringValue123'

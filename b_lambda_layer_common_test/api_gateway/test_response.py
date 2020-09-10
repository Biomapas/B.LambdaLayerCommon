from b_lambda_layer_common.source.python.b_lambda_layer_common.api_gateway.response import Response


def test_FUNC_message_WITH_test_message_EXPECT_dictionary_returned() -> None:
    """
    Test that the function can create an appropriate dictionary response from text body.

    :return: No return.
    """
    response = Response.message(200, 'test')
    assert response == {'body': '{"message": "test"}', 'isBase64Encoded': False, 'statusCode': 200}


def test_FUNC_json_WITH_test_dictionary_EXPECT_dictionary_returned() -> None:
    """
    Test that the function can create an appropriate dictionary response from dictionary body.

    :return: No return.
    """
    response = Response.json(200, body={'test_key': 'test_value'})
    assert response == {'body': '{"test_key": "test_value"}', 'isBase64Encoded': False, 'statusCode': 200}

import base64
from typing import Any

from pytest import mark

from b_lambda_layer_common.api_gateway.response import Response
from b_lambda_layer_common.api_gateway.response_headers import ResponseHeaders


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


def test_FUNC_media_WITH_encoded_file_EXPECT_dictionary_returned() -> None:
    """
    Test that the function will return a byte64 encoded file.

    :return: No return.
    """

    test_value = base64.b64encode(b'test_value')

    response = Response.media(200, ResponseHeaders.wav_headers(), test_value)
    assert response == {'body': test_value, 'isBase64Encoded': True, 'statusCode': 200, 'headers': {'Content-Type': 'audio/wav'}}


@mark.parametrize(
    "data,headers,encoded",
    [
        ('a string', ResponseHeaders.text_headers(), False),
        ('a string', ResponseHeaders.text_headers(), True),
        ('<p>a html paragraph</p>', ResponseHeaders.html_headers(), False),
        ('<p>a html paragraph</p>', ResponseHeaders.html_headers(), True),
    ]
)
def test_FUNC_any_WITH_any_data_EXPECT_dictionary_returned(data: Any, headers: ResponseHeaders, encoded: bool) -> None:
    """
    Test that the function will return any data with according headers.

    :return: No return.
    """
    response = Response.any(200, headers, data, encoded)
    assert response == {'body': data, 'isBase64Encoded': encoded, 'statusCode': 200, 'headers': headers.headers_dict}

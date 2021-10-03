import json

from b_lambda_layer_common.ws_api_gateway.ws_message import WsMessage


def test_FUNC_success_WITH_text_EXPECT_ws_api_gateway_message_formed_and_encoded():
    """
    Test if the message is formed and encoded correctly.

    :return: No return.
    """
    text = 'test_text'

    message = WsMessage.success(text)

    assert json.loads(message.decode('UTF-8')) == {
        'message': text,
        'type': 'SUCCESS'
    }


def test_FUNC_info_WITH_text_EXPECT_ws_api_gateway_message_formed_and_encoded():
    """
    Test if the message is formed and encoded correctly.

    :return: No return.
    """
    text = 'test_text'

    message = WsMessage.info(text)

    assert json.loads(message.decode('UTF-8')) == {
        'message': text,
        'type': 'INFO'
    }


def test_FUNC_warning_WITH_text_EXPECT_ws_api_gateway_message_formed_and_encoded():
    """
    Test if the message is formed and encoded correctly.

    :return: No return.
    """
    text = 'test_text'

    message = WsMessage.warning(text)

    assert json.loads(message.decode('UTF-8')) == {
        'message': text,
        'type': 'WARNING'
    }


def test_FUNC_error_WITH_text_EXPECT_ws_api_gateway_message_formed_and_encoded():
    """
    Test if the message is formed and encoded correctly.

    :return: No return.
    """
    text = 'test_text'

    message = WsMessage.error(text)

    assert json.loads(message.decode('UTF-8')) == {
        'message': text,
        'type': 'ERROR'
    }

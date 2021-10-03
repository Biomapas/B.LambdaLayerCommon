from b_lambda_layer_common.api_gateway.response_headers import ResponseHeaders


def test_FUNC_headers_dict_WITH_dummy_headers_EXPECT_same_dummy_headers() -> None:
    """
    Test that the function returns same headers.

    :return: No return.
    """
    headers = ResponseHeaders({'key': 'value'})
    assert headers.headers_dict == {'key': 'value'}


def test_FUNC_merge_WITH_multiple_headers_EXPECT_headers_merged() -> None:
    """
    Test that the function can merge headers.

    :return: No return.
    """
    headers = ResponseHeaders.merge(
        ResponseHeaders({'key1': 'value'}),
        ResponseHeaders({'key2': 'value'}),
        ResponseHeaders({'key3': 'value'})
    )

    assert headers.headers_dict == {
        'key1': 'value',
        'key2': 'value',
        'key3': 'value'
    }


def test_FUNC_allow_all_cors_headers_WITH_nothing_EXPECT_headers_returned() -> None:
    """
    Test that the function returns appropriate headers.

    :return: No return.
    """
    headers = ResponseHeaders.allow_all_cors_headers().headers_dict

    assert headers == {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': True
    }


def test_FUNC_json_headers_WITH_nothing_EXPECT_headers_returned() -> None:
    """
    Test that the function returns appropriate headers.

    :return: No return.
    """
    headers = ResponseHeaders.json_headers().headers_dict

    assert headers == {
        'Content-Type': 'application/json'
    }


def test_FUNC_wav_headers_WITH_nothing_EXPECT_headers_returned() -> None:
    """
    Test that the function returns appropriate headers.

    :return: No return.
    """
    headers = ResponseHeaders.wav_headers().headers_dict

    assert headers == {
        'Content-Type': 'audio/wav'
    }


def test_FUNC_mpeg_headers_WITH_nothing_EXPECT_headers_returned() -> None:
    """
    Test that the function returns appropriate headers.

    :return: No return.
    """
    headers = ResponseHeaders.mpeg_headers().headers_dict

    assert headers == {
        'Content-Type': 'audio/mpeg'
    }

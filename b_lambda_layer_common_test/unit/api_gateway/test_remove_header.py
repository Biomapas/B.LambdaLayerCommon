from b_lambda_layer_common.api_gateway.remove_header import remove_header

EVENT = {
    'headers': {
        'Content-Length': '100',
        'Content-Type': 'application/json',
        'authorization': 'auth-secret'
    },
    'multiValueHeaders': {
        'Content-Length': [
            '100'
        ],
        'Content-Type': [
            'application/json'
        ],
        'authorization': [
            'auth-secret'
        ]
    }
}
CONTEXT = ''


def test_FUNC_with_default_remove_header_EXPECT_successful_return() -> None:
    """
    Check whether decorated function returns expected result when no parameters
    to decorator are passed.
    """
    @remove_header()
    def handler(event, context):
        return event

    response = handler(EVENT, CONTEXT)

    assert response == EVENT


def test_FUNC_with_non_existing_header_EXPECT_successful_return() -> None:
    """
    Check whether decorated function returns expected result when non-existing header
    to decorator is passed.
    """
    @remove_header('non-existing-header')
    def handler(event, context):
        return event

    response = handler(EVENT, CONTEXT)

    assert response == EVENT


def test_FUNC_with_existing_header_header_EXPECT_successful_return() -> None:
    """
    Check whether decorated function returns expected result when existing header
    to decorator is passed.
    """
    header = 'authorization'

    @remove_header(header)
    def handler(event, context):
        return event

    response = handler(EVENT, CONTEXT)

    assert response['headers'].get(header) is None
    assert response['multiValueHeaders'].get(header) is None


def test_FUNC_with_multiple_existing_headers_EXPECT_successful_return() -> None:
    """
    Check whether decorated function returns expected result when multiple existing headers
    to decorator are passed.
    """
    headers = ['authorization', 'Content-Type']

    @remove_header(*headers)
    def handler(event, context):
        return event

    response = handler(EVENT, CONTEXT)

    assert not any(response['headers'].get(header) is not None for header in headers)
    assert not any(response['multiValueHeaders'].get(header) is not None for header in headers)

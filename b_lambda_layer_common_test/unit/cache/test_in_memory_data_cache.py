from b_lambda_layer_common.cache.in_memory_data_cache import InMemoryDataCache


def test_FUNC_use_cache_WITH_cache_empty_EXPECT_cache_saved() -> None:
    """
    Test the default value for message.

    :return: No return.
    """
    cache = InMemoryDataCache()

    data = cache.use_cache(
        pointer='123',
        func=lambda: '123'
    )

    assert data == '123'

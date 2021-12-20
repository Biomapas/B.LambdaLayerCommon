from b_lambda_layer_common.util.list_bytes_batcher import ListBytesBatcher


def test_FUNC_iterate_batches_WITH_dummy_list_EXPECT_successful_split() -> None:
    """
    Checks do ListBatcher correctly splits a given list into desired size batches. 

    :return: No return.
    """

    items = [item for item in range(1000*1000)]
    batch_size = 256*1024
    # Split list of items into batches not exceeding batch size.
    pool = ListBytesBatcher(items=items, batch_size=batch_size)

    # Check size of each batch in pool.
    for batch in pool.iterate_batches():
        assert ListBytesBatcher.size(batch) <= batch_size

    # Convert batches back to list of items.
    items_flatten = [item for batch in pool.iterate_batches() for item in batch]

    # Compare initial list of items with flatten one.
    assert items == items_flatten, items_flatten

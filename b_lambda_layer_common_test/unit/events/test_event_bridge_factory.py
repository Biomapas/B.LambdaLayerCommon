from b_lambda_layer_common.events.event_bridge_factory import EventBridgeFactory


def test_FUNC_emit_WITH_valid_event_EXPECT_event_successful() -> None:
    """
    Test the default value for message.

    :return: No return.
    """
    class DummyBoto:
        def put_events(self, *args, **kwargs):
            return {'FailedEntryCount': 0}

    factory = EventBridgeFactory(
        source='Test',
        detail_type='Test',
        detail={}
    )

    factory.emit(boto_client=DummyBoto())

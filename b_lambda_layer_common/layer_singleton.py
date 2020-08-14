from aws_cdk.core import Stack

from b_lambda_layer_common.layer import Layer


class LayerSingleton:
    """
    Singleton class that creates a Lambda Layer for common usage.
    """
    __instance: 'LayerSingleton' = None
    __lock: bool = True

    @staticmethod
    def is_initialized() -> bool:
        return bool(LayerSingleton.__instance)

    @staticmethod
    def initialize(scope: Stack, name: str):
        if not LayerSingleton.is_initialized():
            LayerSingleton.__lock = False
            LayerSingleton.__instance = LayerSingleton(scope, name)
            LayerSingleton.__lock = True
        else:
            raise Exception('Instance is already initialized.')

    @staticmethod
    def safe_initialize(scope: Stack, name: str):
        if not LayerSingleton.is_initialized():
            LayerSingleton.__lock = False
            LayerSingleton.__instance = LayerSingleton(scope, name)
            LayerSingleton.__lock = True

    @staticmethod
    def get_instance() -> 'LayerSingleton':
        if LayerSingleton.__instance is None:
            raise Exception('Instance is not initialized. Call initialize method.')

        return LayerSingleton.__instance

    def __init__(self, scope: Stack, name: str) -> None:
        """
        Constructor.

        :param scope: A scope in which this resource should be added.
        :param name: Name and an id of the lambda layer.
        """
        if LayerSingleton.__lock:
            raise Exception('You are not allowed to call constructor. Call get_instance method.')

        self.__layer = Layer(scope, name)

    @property
    def layer(self) -> Layer:
        return self.__layer

from itertools import cycle


class DummySsmClient:
    def __init__(self):
        self.__dummy_params = cycle([
            {
                'Name': 'TestParameter',
                'Type': 'String',
                'Value': 'StringValue1',
                'Version': 10,
            },
            {
                'Name': 'TestParameter',
                'Type': 'StringList',
                'Value': 'StringValue2',
                'Version': 20,
            },
            {
                'Name': 'TestParameter',
                'Type': 'SecureString',
                'Value': 'StringValue3',
                'Version': 30,
            },
        ])

        self.get_parameters_function_calls = 0

    def get_parameters(self, *args, **kwargs):
        self.get_parameters_function_calls += 1

        return {
            'Parameters': [next(self.__dummy_params)],
            'InvalidParameters': []
        }

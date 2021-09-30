from aws_cdk.core import App

from b_lambda_layer_common_test.integration.infrastructure.main_stack import MainStack

app = App()
MainStack(app)
app.synth()

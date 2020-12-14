from aws_cdk.core import App
from b_lambda_layer_common_test.integration.infrastructure import Infrastructure

app = App()
Infrastructure(app)
app.synth()

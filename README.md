# B.LambdaLayerCommon

![Pipeline](https://github.com/Biomapas/B.LambdaLayerCommon/workflows/Pipeline/badge.svg?branch=master)

A lambda layer resource that contains various useful methods.

### Description

This is a simple lambda layer, that contains various useful methods that will make infrastructure development 
much easier. It also allows you to easily manage (add) additional external dependencies. Note, docker is used 
to build this code.

### Remarks

[Biomapas](https://www.biomapas.com/) aims to modernise life-science industry by sharing its IT knowledge with other companies and the community. 
This is an open source library intended to be used by anyone. 
Improvements and pull requests are welcome. 

### Related technology

- Python3
- Docker
- AWS CDK
- AWS Lambda
- AWS Lambda Layer

### Assumptions

This project assumes you know what Lambda functions are and how code is being shared between them
(Lambda layers). 

- Excellent knowledge in IaaC (Infrastructure as a Code) principles.
- Excellent knowledge in Lambda functions and Lambda layers.  
- Good experience in AWS CDK and AWS CloudFormation.
- Good Python skills and basis of OOP.

### Useful sources

- AWS CDK:<br>https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html
- AWS CloudFormation:<br>https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
- Lambda layers:<br>https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html
- Lambda layers in AWS CDK:<br>https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/README.html

### Install

Before installing this library, ensure you have these tools setup:

- Python / Pip
- AWS CDK
- Docker

To install this project from source run:

```
pip install .
```


Or you can install it from a PyPi repository:

```
pip install b-lambda_layer_common
```


### Usage & Examples

Main modules:

- _api_gateway_
  <br>Contains various functionalities related to API Gateway service and integrations.
<br><br>
- _cache_
  <br>Contains caching mechanisms for lambda functions.
<br><br>
- _events_
  <br>Contains functionality that supports event-driven architectures.
<br><br>  
- _exceptions_
  <br>Contains advanced exception handling and propagation between lambda function chains.
<br><br>  
- _ssm_
  <br>Contains SSM parameter store handling logic.
<br><br>  
- _util_
  <br>Contains random fun stuff ;) 
<br><br>  
- _ws_api_gateway_
  <br>Contains various functionalities related to API Gateway websocket service and integrations.

Using this layer is extremely simple. Create it like this:

```python
from aws_cdk.core import Stack, DockerImage
from b_lambda_layer_common.layer import Layer
from b_cfn_lambda_layer.package_version import PackageVersion

Layer(
    scope=Stack(),
    name='MyLayer',
    additional_pip_install_args='--pre',
    dependencies={
        'boto3': PackageVersion.from_string('1.16.35'),
    },
    docker_image=DockerImage.from_registry('python:3.9')
)
```

Or without any optional arguments:

```python
from aws_cdk.core import Stack
from b_lambda_layer_common.layer import Layer

Layer(
    scope=Stack(),
    name='MyLayer',
)
```

Once you have deployed a lambda function with this layer, you can start using previously mentioned modules.
For example, lets use an API-Gateway-formatted response:

```python
from b_lambda_layer_common.api_gateway.response import Response

def handler(*args, **kwargs):
    return Response.json(
      http_status=200,
      body={
        'key': 'value'
      }
    )
```

### Testing

This package has unit tests based on **pytest**.
To run tests simply run:

```
pytest --cov=b_lambda_layer_common b_lambda_layer_common_test/unit --cov-fail-under=80
```

This package has integration tests based on **pytest**.
To run tests simply run:

```
pytest b_lambda_layer_common_test/integration/tests
```

### Contribution

Found a bug? Want to add or suggest a new feature? 
Contributions of any kind are gladly welcome. 
You may contact us directly, create a pull-request or an issue in github platform. 
Lets modernize the world together.

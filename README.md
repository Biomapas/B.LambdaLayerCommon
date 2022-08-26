# B.LambdaLayerCommon

![Pipeline](https://github.com/Biomapas/B.LambdaLayerCommon/workflows/Pipeline/badge.svg?branch=master)

> **DEPRECATION WARNING !!!**</br></br>
> This library no longer supports lambda layers and eventually will be moved to another repository. 
> It is a simple python library of common methods to develop in AWS environment.
> Create your own lambda layer using ![B.CfnLambdaLayer](https://github.com/Biomapas/B.CfnLambdaLayer)
> and specify this library as a dependency. Example given below.
> ```python
> from b_cfn_lambda_layer.lambda_layer import LambdaLayer
> layer = LambdaLayer(
>   ...,
>   dependencies={
>      'b-lambda_layer_common': PackageVersion.from_string_version('4.0.0'),
>   }
> )
> ```

### Description

This is a simple python library, that contains various useful methods that will make infrastructure development 
much easier. 

### Remarks

[Biomapas](https://www.biomapas.com/) aims to modernise life-science industry by sharing its IT knowledge with other companies and the community. 
This is an open source library intended to be used by anyone. 
Improvements and pull requests are welcome. 

### Related technology

- Python3
- Docker
- AWS CDK
- AWS Lambda

### Assumptions

This project assumes you have good knowledge in AWS. 

- Good Python skills and basis of OOP.

### Useful sources

- None.

### Install

Before installing this library, ensure you have these tools setup:

- Python / Pip

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
- _validation_
  <br>Various value validations for python.
<br><br>  
- _ws_api_gateway_
  <br>Contains various functionalities related to API Gateway websocket service and integrations.

### Testing

This package has unit tests based on **pytest**.
To run tests simply run:

```
pytest --cov=b_lambda_layer_common b_lambda_layer_common_test/unit --cov-fail-under=80
```

### Contribution

Found a bug? Want to add or suggest a new feature? 
Contributions of any kind are gladly welcome. 
You may contact us directly, create a pull-request or an issue in github platform. 
Lets modernize the world together.

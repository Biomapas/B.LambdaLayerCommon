# Release history

### 2.1.2
* Add a list bytes batching utility.

### 2.0.6
* Handle errors when raising ValueError in SfnCall class.

### 2.0.4
* Simple return JSON of an output if SfnCall raised ValueError.

### 2.0.1
* Include .txt files.

### 2.0.0
* Complete refactor.
* Fix ugly if/else imports.
* Run unit tests inside lambda functions.
* Use b_cfn_lambda_layer dependency.
* Write more unit and integration tests.
* Add README documentation.

### 1.20.0
* Add validation when bundling with Docker.

### 1.19.0
* General testing improvements.
* Add Layer V2 integration tests.

### 1.18.0
* Add V2 Layer class to enable installation of dependencies.

### 1.16.0
* Add response method to return any type.
* Add `text/html` and `text/plain` headers.
* Add missing `fields` parameter support to `NeighbourEndpoint` class.

### 1.15.1
* Improve function return value handling for `InMemoryDataCache` class.

### 1.15.0
* Add in-memory data caching functionality.

### 1.14.0
* Add `fields` parameter support to `HttpEndpoint` class.

### 1.11.1
* Update DoNotUpdate class to be usable as a type.

### 1.11.0
* Add WebSocket Api Gateway message class to form consistent messages.

### 1.10.2
* Allow for changing HttpEndpoint behavior.

### 1.10.1
* Add ability to specify if to fail to errors.
* Try to read from env event bus name.

### 1.10.0
* Add factory to emit EventBridge events.

### 1.9.5
* Make the code a little more robust and less error prone.

### 1.9.4
* Assets input may contain garbage files too, hence, apply
cleanup commands directly on asset outputs folder.

### 1.9.3
* Add builds badge.

### 1.9.2
* Remove leftover code.
* Update requirements.

### 1.9.1
* Delete unnecessary files which result in different asset hash.
* Calculate hash when bundling.

### 1.9.0
* Add CSV headers.

### 1.8.3
* Ensure everything works with a robust integration test.

### 1.8.2
* Improve Boto3Version class.

### 1.8.1
* Fix bug when boto3 version is specified project files
are not copied.

### 1.8.0
* Change asset bundling to asset docker bundling if additional
dependencies are specified.
* Add ability to install boto3 library.
* Add more unit tests.
* Add integration tests to deploy and test the Layer in AWS.

### 1.7.0
* Simplify SSM parameters functionality.
* Add robust SSM parameter tests.

### 1.6.2
* Do not serialize returned ssm parameters.

### 1.6.1
* Add more logging for better visibility.

### 1.6.0
* SSM should_refresh function should be public.

### 1.5.1
* Add logging on ssm error decorator.

### 1.5.0
* Force using error_class to error_classes.

### 1.4.0
* Add functionality to fetch and cache SSM parameters.
* Add OS type parameters.

### 1.3.0
* Add media Response and wav/mpeg headers.

### 1.2.0
* Add DoNotUpdate class, useful when checking what parameters to update and what not.

### 1.1.3
* Implement retrying logic to HttpCall.

### 1.1.2
* Make sure test coverage is at least 80%.
* Add CI/CD pipeline.
* Add more encodings to decode responses.

### 1.1.1
* Add urllib3 dependency.

### 1.1.0
* Add DynamoDBEncoder that subclasses DecimalEncoder and additionally encodes sets as lists.

### 1.0.3
* Modify call_to_json function by checking whether the response contains body.

### 1.0.2
* Add exception logging for failed imports.

### 1.0.1
* Expose http_endpoint on NeigbourEndpoint class.

### 1.0.0
* Release version with major braking changes.
* Consistent naming for imports.
* Unit tests to cover all functions and classes.
* Add neighbour endpoint.
* General code improvements and cleanup.

### 0.0.16
* Fix logging imports.
* Add logging of exception tracebacks to exception_middleware.
* Add logging about HTTP requests.
* Set request scheme for parent API Gateway urls depending on current protocol.

### 0.0.15
* Add a CognitoAccessToken for parsing access token information provided by the API Gateway using Cognito authorizer.

### 0.0.14
* Add a LoggingManager for setting up logging configuration

### 0.0.13
* Add custom JSON encoder with support for decimal.Decimal encoding

### 0.0.12
* Implement API Gateway body parsing.

### 0.0.11
* Fix imports.

### 0.0.10
* Implement exceptions.

### 0.0.9
* Fix api gateway url.

### 0.0.8
* Add xml to dict converter utility. No dependencies.

### 0.0.7
* Fix imports.

### 0.0.6
* Add ability to check whether singleton was initialized.

### 0.0.5
* Remove description.

### 0.0.4
* Do not create an extra stack.

### 0.0.3
* Add safe initialization.

### 0.0.2
* Add Layer class and Singleton.

### 0.0.1
* Initial build.
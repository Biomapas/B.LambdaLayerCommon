from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_lambda_layer_common',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test b_lambda_layer_common files.
        'b_lambda_layer_common_test'
    ]),
    description=(
        'AWS CDK based lambda layer including useful utilities.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        # Used to create lambda layer.
        'b-cfn-lambda-layer>=2.1.1,<3.0.0',
        # This library includes nice ORM for dynamodb.
        "pynamodb>=5.0.3,<6.0.0",
        # A set that remembers its order, and allows looking up its items by their index in that order.
        "ordered-set>=4.0.2,<5.0.0",
        # Cryptography utilities. NOTE! This library is extremely python-version-specific.
        # Therefore please take a close look on which python version it was built/installed.
        # Cryptography might not work if build environment python version is not the same as
        # your Lambda functions python version. For safety, use Python 3.8.
        "cryptography>=36.0.0,<37.0.0"
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='AWS CDK Lambda Layer',
    url='https://github.com/biomapas/B.LambdaLayerCommon.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

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
        # Exclude test source files.
        'b_lambda_layer_common_test'
    ]),
    description=(
        'AWS CDK based lambda layer including useful utilities.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "aws-cdk.aws_lambda>=1.54.0,<2.0.0",
        'b-aws-testing-framework>=0.0.24,<1.0.0',
        "urllib3>=1.25.10,<2.0.0",
        'pytest>=6.0.2,<7.0.0',
        'pytest-cov>=2.10.1,<3.0.0',
        "pook>=1.0.1,<2.0.0",
        "boto3>=1.16.0,<2.0.0",
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

from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))

long_description = "Not so long description."

setup(
    name='s3backup',
    version='0.0.2',
    description='Bison S3 Backup',
    long_description=long_description,
    author='Patrick Allen',
    author_email='pallen@bison.co',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            's3backup = s3backup.cli:main',
        ],
    },
    keywords='backup s3 amazon tar',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'argparse',
        'boto3',
        'pyyaml'
    ]
)

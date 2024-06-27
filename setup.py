# setup.py
from setuptools import setup, find_packages

setup(
    name='pyvectorSDK',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy'  # our package uses Numpy, here you can include other packages
    ],
)

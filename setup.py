# setup.py
from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name='vectorSDK',
    version='0.1.0',
    packages=find_packages(),
    install_requires=read_requirements()
)

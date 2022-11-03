from distutils.core import setup
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    # Application name:
    name="api_test",
    
    # Version number (initial):
    version="0.1.0",
    
    # Application author details:
    author="Yannobiang",
    author_email="princeobiang@gmail.com",
    
    # Packages
    packages=["mon_app"],
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",
    
    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",
    
    # long_description=open("README.txt").read(),
    
    # Dependent packages (distributions)
    install_requires=required,
)
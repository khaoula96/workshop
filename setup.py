#!/usr/bin/env python3
# coding: utf-8

from glob import glob
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="workshop",
    version="0.1",
    license="Infor",
    python_requires="==3.7.5",
    zip_safe=False,
    include_package_data=True,
    install_requires=required,
    packages=["staging"],
    package_dir={
        "staging": "./src/staging",
    }
)
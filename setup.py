#!/usr/bin/env python
import os
from setuptools import setup

# from distutils.core import setup

setup(
    name="ocbauthencryption",
    version="1.0dev",
    packages=["src/", "tests/"],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    url="https://github.com/TrywialnyOrzech/OCBAuthenticatedEncryption",
    author="Natan Orzechowski, Warsaw University of Technology",
    author_email="natan.orzechowski@ncbj.gov.pl",
)

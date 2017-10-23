"""
This file install the module (folder integrator)
such that the code can be used from everywhere, it does not
need to be started from this directory
"""

from setuptools import setup

setup(
    name='Module name',
    version='Module version',
    description='Module description',
    packages=['integrator']  # Install code in this folder
)
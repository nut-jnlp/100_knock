#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nlp100',
    version='0.01',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nose',
        'scikit-learn',
        'numpy',
        'scipy',
        'Click',
    ],
    entry_points='''
        [console_scripts]
    ''',
)

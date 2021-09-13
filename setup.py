#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

python_version = sys.version_info[:2]
if python_version < (3, 6):
    raise Exception(
        f"This package requires Python 3.6 or greater. You have {python_version}."
    )

from setuptools import setup


setup(
    name="Mathics-doctest",
    version="0.1.0",
    zip_safe=False,
    maintainer="The Mathics Team",
    maintainer_email="mathics-devel@googlegroups.com",
    license="GPLv3",
    packages=[
        "mathics_doctest",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="django-staticfiles-noimport",
    version="1.0",
    packages=["staticfiles_noimport"],
    scripts=[
        "bin/collectstatic",
        "bin/findstatic",
    ]
    install_requires=["Django"],
)

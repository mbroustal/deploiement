#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='deploiement',
	version="1.0",
	author="mal",
	author_email = "maelle.broustal@insa-lyon.fr",
    description="trying",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mbroustal/deploiement",
	license_files="LICENSE",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)


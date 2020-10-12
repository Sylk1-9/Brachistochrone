#!/usr/bin/env python

import glob

from setuptools import setup

scripts = glob.glob('bin/*')

description = "Some script and jupyter notbook about the Brachistochrone problem"

version="0.1"
setup(name="Lesson",
    version=version,
    description=description,
    url="https://github.com/Sylk1-9/Brachistochrone",
    author="Sylvain Vanneste",
    author_email="sylvain.vanneste@gmail.com",
    packages=[],
    package_dir = {'': 'py'},
    package_data = {'': ['etc/']},
    install_requires=['numpy','scipy','ipympl','ipykernel', 'jupyter',
'jupyter_kernel_gateway',],
    test_suite='SaclayMocks.test.test_cor',
    scripts = scripts
    )

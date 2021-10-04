#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='db-cyberark-aam',
    version='0.2',
    author='Danske Bank, A/S',
    author_email='odo@danskebank.lt',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='https://github.com/olegasdo/awx-custom-credential-plugin-aam',
    packages=['db_cyberark_aam'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'db_aam_plugin=db_cyberark_aam:db_aam_plugin',
        ]
    }
)

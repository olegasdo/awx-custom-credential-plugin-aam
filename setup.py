#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='db-cyberark-aam',
    version='0.1',
    author='Danske Bank, A/S',
    author_email='odo@danskebank.lt',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='http://github.com/ansible/awx-custom-credential-plugin-example',
    packages=['db-cyberark-aam'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'db-cyberark-aam =   db-custom-aam:db-cyberark-aam',
        ]
    }
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='name',
    version='0.1.0',
    description='Here goes the description',
    long_description=readme,
    author='Patryk Wegrzyn',
    author_email='wegpat@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

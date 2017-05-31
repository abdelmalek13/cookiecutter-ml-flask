#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='hunlp',
    version='0.1.0',
    description="{{cookiecutter.project_short_description}}",
    long_description=readme,
    author="{{cookiecutter.full_name}}",
    author_email='{{cookiecutter.email}}',
    url='{{cookiecutter.url}}',
    packages=[
        '{{cookiecutter.repo_name}}',
    ],
    package_dir={'{{cookiecutter.repo_name}}':
                     '{{cookiecutter.repo_name}}'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='{{cookiecutter.repo_name}}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

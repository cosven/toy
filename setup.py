#!/usr/bin/env python3

from setuptools import setup


requires = [
]


setup(
    name='toy',
    version='0.0.1a',
    description='toy',
    author='Cosven',
    author_email='cosven.yin@gmail.com',
    packages=[
        'toy',
        ],
    package_data={
        '': []
        },
    url='https://github.com/cosven/toy',
    keywords=['toy'],
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        ),
    install_requires=requires,
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'mock',
        'flake8'
    ],
    entry_points={
        'console_scripts': []
        },
)

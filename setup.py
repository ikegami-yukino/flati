# -*- coding: utf-8 -*-
from codecs import open
import os
import re
from setuptools import setup  # type: ignore

with open(os.path.join('flati', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)  # type: ignore


setup(
    name='flati',
    packages=['flati'],
    version=version,
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='Flatten nested iterable object (Pure-Python)',
    author='Yukino Ikegami',
    author_email='yknikgm@gmail.com',
    url='https://github.com/ikegami-yukino/flati',
    keywords=['flatten', 'generator', 'pure-python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    data_files=[('', ['README.rst', 'CHANGES.rst'])],
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read()),
    tests_require=['pytest'],
    test_suite='pytest'
)

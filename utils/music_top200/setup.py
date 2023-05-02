from setuptools import setup, find_packages

# parse version ---------------------------------------------------------------

import re
import ast
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('music_top200/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# setup -----------------------------------------------------------------------

setup(
    name='music_top200',
    packages=find_packages(),
    version=VERSION,
    description='TODO',
    author='Michael Chow',
    license='MIT',
    author_email='mc_al_gh@fastmail.com',
    keywords=['package', ],
    python_requires=">=3.0",
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

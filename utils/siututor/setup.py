from setuptools import setup, find_packages

# parse version ---------------------------------------------------------------

import re
import ast
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('siututor.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# setup -----------------------------------------------------------------------

setup(
    name='siututor',
    py_modules=['siututor'],
    version=version,
    description='TODO',
    author='Michael Chow',
    license='MIT',
    author_email='mc_al_gh@fastmail.com',
    url='https://github.com/machow/siututor',
    keywords=['package', ],
    install_requires=[
        "siuba",
    ],
    python_requires=">=3.0",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

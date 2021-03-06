#!/usr/bin/env python

"""The setup script."""
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    INSTALL_REQUIREs = f.read().strip().split('\n')
with open('README.rst', encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

setup(
    name='integral',
    description='Integral: A Python package to facilitate synthesis and analysis of Earth system data.',
    long_description=LONG_DESCRIPTION,
    python_requires='>=3.6',
    maintainer='NCAR XDev Team',
    maintainer_email='xdev@ucar.edu',
    classifiers=CLASSIFIERS,
    url='https://integral.readthedocs.io',
    project_urls={
        'Documentation': 'https://integral.readthedocs.io',
        'Source': 'https://github.com/NCAR/integral',
        'Tracker': 'https://github.com/NCAR/integral/issues',
    },
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=INSTALL_REQUIREs,
    license='Apache 2.0',
    zip_safe=False,
    entry_points={},
    keywords='reproducible science xarray earth system model',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
)

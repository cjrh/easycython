# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
long_description = ''
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    pass

# Load the version from the local CHANGES file
# The first line with format "vX.X.X, <blah>" is used.
with open('CHANGES.txt', 'r') as f:
    lines = f.readlines()
version = None
for line in lines:
    if line.strip()[0] == 'v':
        entries = line.split(',')
        if len(entries) > 1:
            version = entries[0].strip()[1:]  # ignore the leading 'v'
            break

if not version:
    print('Could not find a suitable "latest" version in CHANGES.txt.')
    print('Exiting.')
    sys.exit(-1)

setup(
    name='easycython',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=version,

    description='$ easycython mylib.pyx ---> mylib.so',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/cjrh/easycython',

    # Author details
    author='Caleb Hattingh',
    author_email='caleb.hattingh@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Cython',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

        'Topic :: Software Development :: Build Tools',

    ],

    # What does your project relate to?
    keywords='cython',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here. These will be installed by pip
    # when your project is installed. For an analysis of "install_requires"
    # vs pip's requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=['cython', 'numpy', 'begins'],

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            # NOTE: the begins package might have modified the entry point, as
            # per http://begins.readthedocs.org/en/latest/guide.html#entry-points
            'easycython=easycython.easycython:main.start',
        ],
    },
)

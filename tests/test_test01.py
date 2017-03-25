'''
    Tests for building cython extensions.
'''

from __future__ import (print_function, division)
import os
import sys
import shutil
import pytest
import subprocess as sp
from glob import glob


def pth(filename):
    return os.path.join('tests', filename)


@pytest.fixture(scope='module')
def build(request):
    print('Attempt easycython build.')
    os.chdir('tests')
    print('Current folder: ' + os.getcwd())
    print('Python version: ' + str(sys.version))
    # TODO Instead of putting the output here, rather
    # use a tempdir, and add the tempdir to sys.path
    # for importing for the tests.  We need to change
    # easycython to use the begins CLI library to
    # provide a much nicer interface for cmd line args.
    print('Running python -V:')
    os.system('python -V')
    print('Running `which cython`')
    os.system('which cython')
    print('Running easycython:')
    # os.system('python ../easycython/easycython.py test01.pyx')
    sp.check_call([sys.executable, '../easycython/easycython.py', 'test01.pyx'])
    os.chdir('..')
    print('Done.')

    assert os.path.exists(pth('test01.html'))
    assert os.path.exists(pth('test01.c'))
    assert os.path.exists(pth('build'))

    import test01
    def finish():
        print()
        print('Teardown build files...')
        remove_files = glob('tests/test01.*')
        # Can't remove the pyd on Windows!
        exclude_types = ['.pyx', '.pyd']
        for fname in remove_files:
            ext = os.path.splitext(fname)[1]
            if ext in exclude_types:
                continue
            os.remove(fname)
        shutil.rmtree(pth('build'))
        print('Done.')
    request.addfinalizer(finish)
    return test01


def test_simple(build):
    ans = build.f(2.0, 3.0)
    assert abs(ans - 5.0) < 1e-15
    del build


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
    print('Current working dir: ' + os.getcwd())
    print('Contents of the test folder: ' + '\n'.join(os.listdir('tests')))

    if sys.platform == 'win32':
        ext = '.pyd'
    else:
        ext = '.so'
    # This doesn't work because of the renaming in PEP 3149
    #expected_module = pth('test01' + ext)
    #assert os.path.exists(expected_module)

    # if os.path.exists('tests/output.log'):
    #     print('Contents of output.log: ' + '\n'.join(open('tests/output.log', 'r').readlines()))
    # else:
    #     print('ERR: tests/output.log doesn''t exist.')
    assert os.path.exists(pth('test01.html'))
    assert os.path.exists(pth('test01.c'))
    assert os.path.exists(pth('build'))

    import test01
    def finish():
        print('Teardown build files...')
        remove_files = glob('test01.*')
        # Can't remove the pyd on Windows!
        exclude_types = ['.pyx', '.pyd']
        all(os.remove(fname) for fname in remove_files if os.path.splitext(fname)[1] not in exclude_types)
        shutil.rmtree(pth('build'))
        print('Done.')
    request.addfinalizer(finish)
    return test01


def test_simple(build):
    ans = build.f(2.0, 3.0)
    assert abs(ans - 5.0) < 1e-15
    del build


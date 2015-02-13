'''
    Tests for building cython extensions.
'''

from __future__ import (print_function, division)
import os
import sys
import shutil
import pytest


def pth(filename):
    return os.path.join('tests', filename)


@pytest.fixture(scope='module')
def build(request):
    print('Attempt easycython build.')
    os.chdir('tests')
    print('Current folder: ' + os.getcwd())
    # TODO Instead of putting the output here, rather
    # use a tempdir, and add the tempdir to sys.path
    # for importing for the tests.  We need to change
    # easycython to use the begins CLI library to
    # provide a much nicer interface for cmd line args.
    os.system('easycython test01.pyx')
    # os.system('python ../easycython/easycython.py test01.pyx > output.log')
    os.chdir('..')
    print('Done.')

    if sys.platform == 'win32':
        ext = '.pyd'
    else:
        ext = '.so'

    # This doesn't work because of the renaming in PEP 3149
    #expected_module = pth('test01' + ext)
    #assert os.path.exists(expected_module)
    # print('Current working dir: ' + os.getcwd())
    # print('Contents of the test folder: ' + '\n'.join(os.listdir('tests')))
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
        #del test01
        for ext in ['html','c']:  #,'pyd']:
            os.remove(pth('test01.' + ext))
        shutil.rmtree(pth('build'))
        print('Done.')
    request.addfinalizer(finish)

    return test01


def test_simple(build):
    ans = build.f(2.0, 3.0)
    assert abs(ans - 5.0) < 1e-15
    del build


import sys
import os
from os.path import splitext
import numpy

if len(sys.argv) == 1:
    print 'You must supply one or more .pyx filenames.'
    sys.exit()

if sys.argv[1].lower() == '*.pyx':
    files = os.listdir('.')
else:
    files = sys.argv[1:]
extensions = [(splitext(f)[0], f) for f in files if splitext(f)[1].lower() == '.pyx']

# No pyx files given.
if len(extensions) == 0:
    print 'No .pyx filenames were supplied.  Exiting.'
    sys.exit()

# Checking for missing files
missing = [f for n, f in extensions if not os.path.exists(f)]
if missing:
    print 'One or more given files were missing:'
    for f in missing:
        print '    {}'.format(f)
    print 'Aborting.'

# Restore distutils command line args
sys.argv = [sys.argv[0], 'build_ext', '--inplace']

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension(
        n, [f], extra_compile_args=["-O2","-march=native"]) for n, f in extensions],
    include_dirs=[numpy.get_include()]
)

# Cleanup: delete intermediate C files.
#for n, f in extensions:
#    if os.path.exists(n+'.c'):
#        os.remove(n+'.c')

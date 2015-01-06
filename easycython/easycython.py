from __future__ import print_function, division
import sys
import os
from os.path import splitext
try:
    import numpy
except:
    print('Numpy is required, but not found. Please install it')

def main():
    if len(sys.argv) == 1:
        print('You must supply one or more .pyx filenames.')
        sys.exit()

    # TODO: This is poor option handling. Should be fixed.
    if sys.argv[1].lower() == '*.pyx':
        files = os.listdir('.')
    else:
        files = sys.argv[1:]

    # Collect all the extensions to process
    extensions = []
    for f in files:
        basename, ext = splitext(f)
        if ext.lower() == '.pyx':
            extensions.append((basename, f))

    # No pyx files given.
    if len(extensions) == 0:
        print('No .pyx filenames were supplied.  Exiting.')
        sys.exit()

    # Checking for missing files
    missing = [f for n, f in extensions if not os.path.exists(f)]
    if missing:
        print('One or more given files were missing:')
        for f in missing:
            print('    {}'.format(f))
        print('Aborting.')

    # Restore distutils command line args
    # TODO: It should be possible to specify these
    # options direction on the objects, rather than
    # hacking the command line.
    sys.argv = [sys.argv[0], 'build_ext', '--inplace']

    import setuptools
    from distutils.core import setup
    from distutils.extension import Extension
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
    import Cython.Compiler.Options
    Cython.Compiler.Options.annotate = True

    # Create module objects
    ext_modules = []
    for n, f in extensions:
        obj = Extension(n, [f], extra_compile_args=["-O2", "-march=native"])
        ext_modules.append(obj)

    setup(
        cmdclass = {'build_ext': build_ext},
        include_dirs=[numpy.get_include()],
        # ext_modules = cythonize([f for n,f in extensions]),
        ext_modules = cythonize(ext_modules),
        # ext_modules = ext_modules
    )

    # Cleanup: delete intermediate C files.
    #for n, f in extensions:
    #    if os.path.exists(n+'.c'):
    #        os.remove(n+'.c')
if __name__ == '__main__':
    main()

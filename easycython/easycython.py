from __future__ import print_function, division
import sys
import os
import logging
from os.path import splitext
import begin
from glob import glob

logging.getLogger().setLevel(logging.INFO)

@begin.start
def main(annotation=True, numpy_includes=True, *filenames):
    # The filename args are allowed to be globs
    # files = [f for g in filenames for f in glob(g) 
    #          if splitext(f)[1].lower() in ['.pyx', '.py', 'pyw']]
    files = [f for g in filenames for f in glob(g)] 
    logging.info('Detected files: ')
    for f in files:
        logging.info(' '*4 + f)

    # Collect all the extensions to process
    extensions = []
    for f in files:
        basename, ext = splitext(f)
        extensions.append((basename, f))

    # No pyx files given.
    if len(extensions) == 0:
        logging.error('No valid source filenames were supplied.')
        sys.exit(1)

    # Checking for missing files
    missing = [f for n, f in extensions if not os.path.exists(f)]
    if missing:
        logging.error('One or more given files were missing:')
        for f in missing:
            logging.error('    {}'.format(f))
        print('Aborting.')
        sys.exit(2)

    # Restore distutils command line args
    # TODO: It should be possible to specify these
    # options direction on the objects, rather than
    # hacking the command line.
    sys.argv = [sys.argv[0], 'build_ext', '--inplace']

    from setuptools import setup, Extension
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
    import Cython.Compiler.Options
    Cython.Compiler.Options.annotate = annotation

    # Create module objects
    ext_modules = []
    for n, f in extensions:
        obj = Extension(n, [f], extra_compile_args=["-O2", "-march=native"])
        ext_modules.append(obj)

    include_dirs = []
    if numpy_includes:
        try:
            import numpy
            include_dirs += [numpy.get_include()]
        except:
            logging.exception('Numpy is required, but not found. Please install it')

    setup(
        cmdclass = {'build_ext': build_ext},
        include_dirs=include_dirs,
        # ext_modules = cythonize([f for n,f in extensions]),
        ext_modules = cythonize(ext_modules),
        # ext_modules = ext_modules
    )

    # Cleanup: delete intermediate C files.
    #for n, f in extensions:
    #    if os.path.exists(n+'.c'):
    #        os.remove(n+'.c')

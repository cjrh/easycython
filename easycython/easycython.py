from __future__ import print_function, division
import sys
import os
import logging
from os.path import splitext
import begin
from glob import glob
import subprocess


@begin.start
def main(annotation=True, numpy_includes=True, debugmode=False,
         make_exes=False,
         *filenames):
    if debugmode:
        logging.getLogger().setLevel(logging.INFO)

    # The filename args are allowed to be globs
    # files = [f for g in filenames for f in glob(g)
    #          if splitext(f)[1].lower() in ['.pyx', '.py', 'pyw']]
    logging.info('Given filenames = ' + '\n'.join(filenames))
    logging.info('Current dir contents: \n    ' + '\n    '.join(os.listdir('.')))
    # This is a beautiful, beautiful line. This is why I use Python.
    files = [f for g in filenames for f in glob(g)]
    logging.info('Detected files: \n    ' + '\n    '.join(files))


    # Collect all the extensions to process
    extensions = []
    for f in files:
        basename, ext = splitext(f)
        extensions.append((basename, f))

    if make_exes:
        for (basename, f) in extensions:
            x = subprocess.check_call(
                ['cython', '--embed', '--set-python-home', f]
            )
            from pprint import pprint
            from distutils import ccompiler
            from distutils import sysconfig
            compiler_name = ccompiler.get_default_compiler(os.name, sys.platform)
            compiler = ccompiler.new_compiler()
            print('Selected compiler: %s' % compiler)
            pprint(vars(compiler))
            # sysconfig.customize_compiler(compiler)
            pprint(vars(compiler))
            compiler.include_dirs += [
                sysconfig.get_python_inc(),
                os.path.dirname(sysconfig.get_python_inc())
            ]
            # compiler.library_dirs += [sysconfig.get_python_lib()]
            # compiler.linker_so += ['-o', basename]
            # compiler.linker_so.remove('-shared')
            pprint(vars(compiler))
            compiler.compile([basename + '.c'])
            print('\n\nCompiling finished, now linking.\n\n')
            static_python = (
                os.path.dirname(sysconfig.get_python_lib(standard_lib=True))
                + '/python3.5/config-3.5m/libpython3.5m.a'
            )
            static_python = '/usr/local/Cellar/python3/3.5.2/Frameworks/Python.framework/Versions/3.5/lib/python3.5/config-3.5m/libpython3.5m.a'
            static_python = '/Users/calebhattingh/Documents/repos/cpythonplay/libpython3.6m.a'
            compiler.link_executable(
                [basename + '.o', static_python], 'main',
            )
            return


    # No pyx files given.
    if len(extensions) == 0:
        logging.error('No valid source filenames were supplied.')
        sys.exit(1)

    # Checking for missing files
    missing = [f for n, f in extensions if not os.path.exists(f)]
    if missing:
        logging.error('These files were missing:')
        for f in missing:
            logging.error('    {}'.format(f))
        logging.error('Aborting.')
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
        # The name must be plain, no path
        module_name = os.path.basename(n)
        obj = Extension(module_name, [f],
                extra_compile_args=["-O2", "-march=native"])
        ext_modules.append(obj)

    # Extra include folders. Mainly for numpy.
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
        ext_modules = cythonize(ext_modules),
        )

    # Cleanup: delete intermediate C files.
    #for n, f in extensions:
    #    if os.path.exists(n+'.c'):
    #        os.remove(n+'.c')

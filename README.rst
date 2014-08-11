.. image:: https://travis-ci.org/cjrh/easycython.svg?branch=master
   :target: https://travis-ci.org/cjrh/easycython

.. image:: https://coveralls.io/repos/cjrh/easycython/badge.png
   :target: https://coveralls.io/r/cjrh/easycython

.. image:: https://ci.appveyor.com/api/projects/status/23heqrp96f6ftmsr
   :target: https://ci.appveyor.com/project/cjrh/easycython

==========
easycython
==========

Because writing a `setup.py` each time is painful.

`easycython.py` is a script that will attempt to
automatically convert one or more `.pyx` files into
the corresponding compiled `.pyd|.so` binary modules
files. Example::

    $ python easycython.py myext.pyx

`pip install easycython` will automatically create an
executable script in your `Scripts/` folder, so you
should be able to simply::

    $ easycython myext.pyx

or even::

    $ easycython *.pyx

Note that:

- Cython annotation (`-a`) is always-on. I find it easier to 
  just always have the annotation available, and clean up unwanted
  files by other means.
- `numpy` is required, because all the work I do requires 
  `numpy` support inside my cython extensions.
- Compiler flags `-O2 -march=native` are automatically passed to
  the compiler. I have not yet had to step through the generated
  C code with a debugger.

These things above could all be made optional. I'm considering 
using the `begins` library for the CLI interface.

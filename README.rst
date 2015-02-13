.. image:: https://travis-ci.org/cjrh/easycython.svg?branch=master
   :target: https://travis-ci.org/cjrh/easycython

.. image:: https://coveralls.io/repos/cjrh/easycython/badge.png
   :target: https://coveralls.io/r/cjrh/easycython

.. image:: https://ci.appveyor.com/api/projects/status/23heqrp96f6ftmsr
   :target: https://ci.appveyor.com/project/cjrh/easycython


==========
easycython
==========

Because writing a :code:`setup.py` each time is painful.

:code:`easycython.py` is a script that will attempt to
automatically convert one or more :code:`.pyx` files into
the corresponding compiled :code:`.pyd|.so` binary modules
files. Example::

    $ python easycython.py myext.pyx

:code:`pip install easycython` will automatically create an
executable script in your :code:`Scripts/` folder, so you
should be able to simply::

    $ easycython myext.pyx

or even::

    $ easycython *.pyx

You can type::

    $ easycython -h

to obtain the following CLI::

    usage: easycython.py [-h] [--annotation] [--no-annotation] [--numpy-includes]
                         [--no-numpy-includes]
                         [filenames [filenames ...]]

    positional arguments:
      filenames

    optional arguments:
      -h, --help           show this help message and exit
      --annotation
      --no-annotation      (default: True)
      --numpy-includes
      --no-numpy-includes  (default: True)


- :code:`--annotation` (default) will emit the HTML Cython annotation file.
- :code:`--numpy-includes` (default) will add the numpy headers to the build command.
- Compiler flags :code:`-O2 -march=native` are automatically passed to
  the compiler. I have not yet had to step through the generated
  C code with a debugger.


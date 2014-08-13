SET PYDIR=C:\Python
SET PYTHON_VERSION=2.6
SET PLATFORM=x86
call appveyor/install.cmd
call appveyor/runtests.cmd
call appveyor/buildwheels.cmd

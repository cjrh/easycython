REM Augment the path so that the correct python gets used.
SET PATH=%PYDIR%\envs\testenv;%PYDIR%\envs\testenv\Scripts;%PATH%
ECHO Inside runtests.cmd
ECHO This is the path:
ECHO %PATH%
ECHO python -V
REM Run tests
python setup.py develop
py.test

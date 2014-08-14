REM Augment the path so that the correct python gets used.
SET PATH=%PYDIR%\envs\testenv;%PYDIR%\envs\testenv\Scripts;%PATH%
ECHO Inside runtests.cmd
ECHO This is the path:
ECHO %PATH%
python.exe -V
dir %PYDIR%
REM Run tests
python.exe setup.py develop
py.test

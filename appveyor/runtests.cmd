REM Augment the path so that the correct python gets used.
SET PATH=%PYDIR%\envs\testenv;%PYDIR%\envs\testenv\Scripts;%PATH%
ECHO Inside runtests.cmd
ECHO This is the path:
ECHO %PATH%
ECHO This is the python version:
python.exe -V
ECHO Contents of the envs subfolder:
dir %PYDIR%\envs
ECHO These are the contents of the python scripts folder:
ECHO (only starting with p*...)
dir %PYDIR%\envs\testenv\Scripts\p*
REM Run tests
ECHO Installing package via "python.exe setup.py develop":
python.exe setup.py develop
ECHO Running tests:
CALL py.test

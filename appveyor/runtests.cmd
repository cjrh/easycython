REM Augment the path so that the correct python gets used.
SET PATHENV=%PYDIR%\envs\testenv
SET PATH=%PATHENV%;%PATHENV%\Scripts;%PATH%
SET PYTHONHOME=%PYDIR%
SET PYTHONPATH=%PYDIR%\Lib
ECHO Inside runtests.cmd
ECHO This is the path:
ECHO %PATH%
ECHO This is the python version:
python.exe -V
ECHO Contents of the envs subfolder:
dir %PYDIR%\envs
ECHO These are the contents of the python scripts folder:
ECHO (only starting with p*...)
dir %PATHENV%\Scripts\p*
REM Run tests
ECHO Installing package via "python.exe setup.py develop":
%PATHENV%\python.exe setup.py develop
ECHO Running tests:
%PATHENV%\Scripts\py.test tests

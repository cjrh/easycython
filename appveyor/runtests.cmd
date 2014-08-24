ECHO Inside runtests.cmd
REM Augment the path so that the correct python gets used.
SET PATHENV=%PYDIR%\envs\testenv
SET PATH=%PATHENV%;%PATHENV%\Scripts;%PATH%
SET PYTHONHOME=
SET PYTHONPATH=
CALL "appveyor\createenv.cmd"
ECHO This is the path:
ECHO %PATH%
ECHO This is the python version:
%PATHENV%\python.exe -V
ECHO Contents of the envs subfolder:
dir %PYDIR%\envs
ECHO ========================================================
ECHO The current environment:
SET
ECHO ========================================================
ECHO These are the contents of the python scripts folder:
ECHO (only starting with p*...)
dir %PATHENV%\Scripts\p*
ECHO ========================================================
REM Run tests
ECHO Installing package via "python.exe setup.py install":
REM %PATHENV%\python.exe setup.py develop
%PATHENV%\python.exe setup.py install
ECHO Running tests:
%PATHENV%\python.exe -m pytest tests
REM %PATHENV%\Scripts\py.test tests

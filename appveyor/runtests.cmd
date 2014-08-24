REM Augment the path so that the correct python gets used.
SET PATHENV=%PYDIR%\envs\testenv
SET PATH=%PATHENV%;%PATHENV%\Scripts;%PATH%
SET PYTHONHOME=
SET PYTHONPATH=
ECHO Inside runtests.cmd
ECHO This is the path:
ECHO %PATH%
ECHO This is the python version:
python.exe -V
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
:: Replicate cmd option /E:ON (command extensions - haven't needed yet)
::setlocal EnableExtensions
:: Replicate cmd option /V:ON (delayed expansion - required)
setlocal EnableDelayedExpansion
CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
SET DISTUTILS_USE_SDK=1
SET MSSdk=1
ECHO ========================================================
REM Run tests
ECHO Installing package via "python.exe setup.py install":
REM %PATHENV%\python.exe setup.py develop
%PATHENV%\python.exe setup.py install
ECHO Running tests:
python.exe -m pytest tests
REM %PATHENV%\Scripts\py.test tests

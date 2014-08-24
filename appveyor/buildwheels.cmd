REM Augment the path so that the correct python gets used.
SET PATHENV=%PYDIR%\envs\testenv
SET PATH=%PATHENV%;%PATHENV%\Scripts;%PATH%
SET PYTHONHOME=
SET PYTHONPATH=
CALL "appveyor\createenv.cmd"
:: Replicate cmd option /V:ON (delayed expansion - required)
setlocal EnableDelayedExpansion
CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
SET DISTUTILS_USE_SDK=1
SET MSSdk=1
ECHO ========================================================
REM Make the wheel
%PATHENV%\python.exe setup.py bdist_wheel

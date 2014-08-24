REM Augment the path so that the correct python gets used.
SET PATHENV=%PYDIR%\envs\testenv
SET PATH=%PATHENV%;%PATHENV%\Scripts;%PATH%
SET PYTHONHOME=
SET PYTHONPATH=
SETLOCAL EnableDelayedExpansion
CALL "appveyor\createenv.cmd"
ECHO ========================================================
REM Make the wheel
%PATHENV%\python.exe setup.py bdist_wheel

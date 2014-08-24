SET PYTHONHOME=
SET PYTHONPATH=

SET WIN_SDK_ROOT=C:\Program Files\Microsoft SDKs\Windows
SET MAJOR_PYTHON_VERSION="%PYTHON_VERSION:~0,1%"
IF %MAJOR_PYTHON_VERSION% == "2" (
    SET WINDOWS_SDK_VERSION=v7.0
) ELSE IF %MAJOR_PYTHON_VERSION% == "3" (
    SET WINDOWS_SDK_VERSION=v7.1
) ELSE (
    ECHO Unsupported Python version: "%MAJOR_PYTHON_VERSION%"
    EXIT 1
)
ECHO ========================================================
ECHO Major Python version is %MAJOR_PYTHON_VERSION%, using Windows SDK %WINDOWS_SDK_VERSION%
ECHO ========================================================

IF "%PLATFORM%"=="x64" (
    CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
    SET DISTUTILS_USE_SDK=1
    SET MSSdk=1
    SET MINICONDA=Miniconda-3.6.0-Windows-x86_64.exe
) ELSE (
    CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x86
    SET MINICONDA=Miniconda-3.6.0-Windows-x86.exe
    REM TODO Ask continuum to use a "latest" URL for the most recent miniconda
)
ECHO Windows SDK enabled.
ECHO ========================================================
SET CONDACMD=%PYDIR%\Scripts\conda.exe
SET PATHENV=%PYDIR%\envs\testenv
ECHO Modified path and added environment vars.
ECHO ========================================================

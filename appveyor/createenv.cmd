::@ECHO OFF
setlocal EnableDelayedExpansion
SET PYTHONHOME=
SET PYTHONPATH=

SET WIN_SDK_ROOT=C:\Program Files\Microsoft SDKs\Windows
SET MAJOR_PYTHON_VERSION="%PYTHON_VERSION:~0,1%"
ECHO Major Python version is %MAJOR_PYTHON_VERSION%
IF %MAJOR_PYTHON_VERSION% == "2" (
    SET WINDOWS_SDK_VERSION=v7.0
) ELSE IF %MAJOR_PYTHON_VERSION% == "3" (
    SET WINDOWS_SDK_VERSION=v7.1
) ELSE (
    ECHO Unsupported Python version: "%MAJOR_PYTHON_VERSION%"
    EXIT 1
)

IF "%PLATFORM%"=="x64" (
    ECHO Configuring environment to build with MSVC on a 64bit architecture
    ECHO Using Windows SDK %WINDOWS_SDK_VERSION%
    ECHO "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
    CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
    ECHO Windows SDK enabled.
    SET DISTUTILS_USE_SDK=1
    SET MSSdk=1
    REM Alias the x64 miniconda file
    SET MINICONDA=Miniconda-3.6.0-Windows-x86_64.exe
) ELSE (
    ECHO Using Windows SDK %WINDOWS_SDK_VERSION%
    CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x86
    REM Alias the x86 miniconda file
    SET MINICONDA=Miniconda-3.6.0-Windows-x86.exe
    REM TODO Ask continuum to use a "latest" URL for the most recent miniconda
)

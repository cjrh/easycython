REM To build extensions for 64 bit Python 3, we need to configure environment
REM variables to use the MSVC 2010 C++ compilers from GRMSDKX_EN_DVD.iso of:
REM MS Windows SDK for Windows 7 and .NET Framework 4
REM
REM More details at:
REM https://github.com/cython/cython/wiki/64BitCythonExtensionsOnWindows


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
    CMD /E:ON /V:ON /C "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /Release /x64
    ECHO Windows SDK enabled.
    SET DISTUTILS_USE_SDK=1
    SET MSSdk=1
    REM Alias the x64 miniconda file
    SET MINICONDA=Miniconda-3.6.0-Windows-x86_64.exe
) ELSE (
    ECHO Using Windows SDK %WINDOWS_SDK_VERSION%
    CALL "C:\Program Files\Microsoft SDKs\Windows\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /x86 /release
    REM Alias the x86 miniconda file
    SET MINICONDA=Miniconda-3.6.0-Windows-x86.exe
    REM TODO Ask continuum to use a "latest" URL for the most recent miniconda
)

REM Download the miniconda distribution using the system python 2.7
IF NOT EXIST %MINICONDA% (
    ECHO "Downloading %MINICONDA%..."
    python.exe appveyor/dlfile.py http://repo.continuum.io/miniconda/%MINICONDA%
    ECHO "Done."
)
REM Perform a silent install of miniconda
ECHO Perform a silent install of miniconda
%MINICONDA% /InstallationType=AllUsers /S /AddToPath=1 /RegisterPython=0 /D=%PYDIR%
ECHO "Done."
REM Alias conda
SET PATH=%PYDIR%;%PYDIR%/Scripts;%PATH%
SET CONDACMD=%PYDIR%/Scripts/conda.exe
REM Create required conda env
ECHO Create required conda env
%CONDACMD% create --quiet --yes -f -n testenv python=%PYTHON_VERSION% numpy cython pip pytest setuptools
ECHO "Done."
IF "%PYTHON_VERSION%"== "2.6" (
    %CONDACMD% install  --yes -f -p %PYDIR%\envs\testenv argparse py
)

REM To build extensions for 64 bit Python 3, we need to configure environment
REM variables to use the MSVC 2010 C++ compilers from GRMSDKX_EN_DVD.iso of:
REM MS Windows SDK for Windows 7 and .NET Framework 4
REM
REM More details at:
REM https://github.com/cython/cython/wiki/64BitCythonExtensionsOnWindows

:: This must be enabled, otherwise %MINICONDA% and other variables will
:: not get substituted. They are set inside "createenv.cmd"
SETLOCAL EnableDelayedExpansion
ECHO Setting up the required environment variables and paths:
CALL "appveyor\createenv.cmd"
ECHO ...Done.

REM Download the miniconda distribution using the system python 2.7
IF NOT EXIST %MINICONDA% (
    ECHO "Downloading %MINICONDA%..."
    python.exe appveyor/dlfile.py http://repo.continuum.io/miniconda/%MINICONDA%
    ECHO "Done."
)

ECHO ========================================================
ECHO Current list of environment variables:
SET
ECHO ========================================================
ECHO Perform a silent install of miniconda
DIR
start /wait "" %MINICONDA% /InstallationType=AllUsers /S /AddToPath=1 /RegisterPython=0 /D=%PYDIR%
ECHO Done.
ECHO
ECHO Path:
ECHO %PATH%
REM Alias conda
SET PATH=%PYDIR%;%PYDIR%\Scripts;%PATH%
ECHO ========================================================
ECHO Current list of environment variables:
SET
ECHO ========================================================
ECHO Create required conda env
%CONDACMD% create --quiet --yes -f -n testenv python=%PYTHON_VERSION% numpy cython pip py pytest setuptools
ECHO "Done."
IF "%PYTHON_VERSION%"== "2.6" (
    %CONDACMD% install --quiet --yes -f -p %PYDIR%\envs\testenv argparse py
)
ECHO ========================================================
ECHO Installing pip-only packages (inside testenv)
%PATHENV%\Scripts\pip install wheel
ECHO Done.

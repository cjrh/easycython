REM Augment the path so that the correct python gets used.
SET PATH=%PYDIR%\envs\testenv;%PYDIR%\envs\testenv\Scripts;%PATH%
REM Make the wheel
python setup.py bdist_wheel

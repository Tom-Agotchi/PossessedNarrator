
@echo off

setlocal

REM set LOCAL_HOME=E:\Projects\LocalNPNstuff\SS\STARTUP
set PYTHON_PATH="E:\Python3_6\python.exe"

%PYTHON_PATH% generateMIDI.py 

endlocal
pause
:exit
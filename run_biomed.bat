@echo off
title Smart MedWaste AI - Bio-Medical Waste Segregation System
echo ==================================================================
echo   SMART MEDWASTE AI: BIO-MEDICAL WASTE SEGREGATION & IOT SYSTEM
echo   Launching Hospital Command Center...
echo ==================================================================
echo.

set PYTHON_PATH="C:\Users\drona\AppData\Local\Programs\Python\Python313\python.exe"

if exist %PYTHON_PATH% (
    echo Using Python at: %PYTHON_PATH%
    %PYTHON_PATH% biomed_app.py
) else (
    echo Python executable not found at %PYTHON_PATH%. Trying 'python' from PATH...
    python biomed_app.py
)

pause


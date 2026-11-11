@echo off
title AI-Powered Career Guidance System
echo ========================================================
echo   AI-POWERED CAREER GUIDANCE SYSTEM
echo   Launching Web Server & Machine Learning Engine...
echo ========================================================
echo.

set PYTHON_PATH="C:\Users\drona\AppData\Local\Programs\Python\Python313\python.exe"

if exist %PYTHON_PATH% (
    echo Using Python at: %PYTHON_PATH%
    %PYTHON_PATH% app.py
) else (
    echo Python executable not found at %PYTHON_PATH%. Trying 'python' from PATH...
    python app.py
)

pause


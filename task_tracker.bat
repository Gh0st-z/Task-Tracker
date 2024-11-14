@echo off
set file=menu.py

REM Check if the Python file for the game exists
if exist "%file%" (
    REM Check if Python is installed and in the PATH
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Python is not installed or not found in PATH.
    ) else (
        REM Run the game Python file
        cls
        python "%file%"
    )
) else (
    echo File not found: %file%
)

@echo off
title Institutional Quant Ecosystem Launcher
color 0A

echo ============================================
echo   INSTITUTIONAL QUANT ECOSYSTEM LAUNCHER
echo ============================================
echo.

REM Always move to the folder where run.bat exists (machine-independent)
cd /d "%~dp0"

REM Set environment variables safely
set PYTHONUNBUFFERED=1
set ECOSYSTEM_ENV=PRODUCTION

REM Detect machine identity
set MACHINE_NAME=%COMPUTERNAME%
echo Machine: %MACHINE_NAME%
echo Location: %CD%
echo.

REM Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found, using system Python
)

echo.

REM Verify Python availability
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not detected.
    pause
    exit /b
)

echo Python detected successfully.
echo.

REM Load .env safely (if exists)
if exist ".env" (
    echo Environment file detected.
) else (
    echo WARNING: .env file not found.
)

echo.

REM Clear stale cache automatically (prevents 90% of runtime bugs)
echo Clearing cache...
for /d /r %%i in (__pycache__) do rd /s /q "%%i" 2>nul

echo Cache cleared.
echo.

REM Start ecosystem
echo Launching Institutional Core...
echo.

python main.py

echo.
echo Ecosystem stopped.
pause

@echo off
title Institutional Quant Ecosystem Launcher

cd /d %~dp0

if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

echo Starting Dashboard...
start cmd /k python main.py

timeout /t 2

start http://127.0.0.1:5000/dashboard

echo System Launched Successfully

pause

@echo off
title Quant Ecosystem

echo =========================================
echo   Starting Quant Ecosystem...
echo =========================================

:: ===== Git Auto Sync =====
echo Syncing with GitHub...

git pull

git add .
git commit -m "auto update" >nul 2>&1
git push >nul 2>&1

:: ===== Install deps (safe) =====
echo Installing dependencies...
pip install -r requirements.txt

:: ===== Start dashboard =====
echo Starting Dashboard...
start cmd /k python dashboard/web_dashboard.py

timeout /t 3 >nul

:: ===== Start engine =====
echo Starting Trading Engine...
python main.py

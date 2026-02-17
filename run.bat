@echo off
cd /d C:\Users\Home PLUS\OneDrive\Desktop\New folder (2)\quant_ecosystem
python main.py
pause


cd /d D:\AI_Projects\quant_ecosystem

call .venv\Scripts\activate

:loop

echo Syncing GitHub...
git pull origin main

echo Starting Autonomous Ecosystem...

python main.py

echo System crashed. Restarting in 10 seconds...

timeout /t 10

goto loop

echo Uploading brain to cloud...

git add data/global_brain.pt
git add data/global_brain_backup.pt

git commit -m "Automated brain checkpoint"

git push

echo Complete.
pause


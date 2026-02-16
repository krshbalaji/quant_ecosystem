@echo off

cd /d D:\AI_Projects\quant_ecosystem

call .venv\Scripts\activate

echo Syncing GitHub...

git pull origin main

echo Starting system...

python main.py

echo Pushing updates...

git add .
git commit -m "Auto update"
git push origin main

pause
:loop

python main.py

echo Restarting after crash...

timeout /t 5

goto loop

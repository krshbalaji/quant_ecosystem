@echo off

:loop
echo Starting engine...
python main.py

echo Engine crashed. Restarting in 5 seconds...
timeout /t 5
goto loop

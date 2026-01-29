@echo off
python "%~dp0..\..\generator.py" --length 12 --safe-symbols
timeout /t 5 >nul


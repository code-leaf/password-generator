@echo off
python "%~dp0..\..\generator.py" --length 10 --no-symbols
timeout /t 5 >nul


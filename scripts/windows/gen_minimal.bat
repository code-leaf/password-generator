@echo off
python "%~dp0..\..\generator.py" --length 8 --no-symbols
timeout /t 5 >nul


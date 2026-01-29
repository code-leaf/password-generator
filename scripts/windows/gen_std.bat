@echo off
python "%~dp0..\..\generator.py" --length 12
timeout /t 5 >nul


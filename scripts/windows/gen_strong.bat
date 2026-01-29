@echo off
python "%~dp0..\..\generator.py" --length 16
timeout /t 5 >nul


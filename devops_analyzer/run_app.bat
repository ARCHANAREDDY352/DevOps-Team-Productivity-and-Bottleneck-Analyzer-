@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python -m streamlit run devops_analyzer\app.py --server.headless false
pause

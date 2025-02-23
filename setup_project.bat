@echo off
echo Setting up the Python project...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Setup complete! Run `call venv\Scripts\activate` to activate the environment.
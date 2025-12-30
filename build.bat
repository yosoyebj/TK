@echo off
TITLE Token Split Calculator Builder
COLOR 0A

echo ========================================================
echo      TOKEN SPLIT CALCULATOR - AUTOMATED BUILDER
echo ========================================================
echo.

echo 1. Checking for Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed. Please install from python.org.
    pause
    exit /b
)
echo Python found.

echo.
echo 2. Installing Requirements (PyInstaller & Pillow)...
pip install pyinstaller Pillow
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install requirements.
    pause
    exit /b
)

echo.
echo 3. Converting Icon (PNG to ICO)...
python -c "from PIL import Image; Image.open('icon.png').save('icon.ico')"
IF %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Could not convert icon.png. The app will have default icon.
) ELSE (
    echo Icon converted successfully.
)

echo.
echo 4. Building TokenSplitter.exe...
echo This might take a minute...
if exist icon.ico (
    pyinstaller --onefile --noconsole --icon=icon.ico --name "TokenSplitter" calculator.py
) else (
    pyinstaller --onefile --noconsole --name "TokenSplitter" calculator.py
)

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build failed.
    pause
    exit /b
)

echo.
echo ========================================================
echo              BUILD SUCCESSFUL!
echo ========================================================
echo.
echo Your app is ready with the new Logo!
echo Opening 'dist' folder now...
start dist
pause

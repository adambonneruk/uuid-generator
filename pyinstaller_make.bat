REM clear-down the ./dist/ folder
IF EXIST dist ( ERASE /F /Q dist )

REM copy unique.py to unique.pyw (we'll delete again at the end)
COPY unique\unique_gui.py unique\unique_gui.pyw

REM copy images and icons
XCOPY unique\icon\ dist\icon\ /E

REM run pyinstaller for unique.py to create .exe
pyinstaller.exe --onefile --icon=.\unique\icon\icon.ico unique\unique.py

REM run pyinstaller for unique_gui.pyw to create .exe (with no cli)
pyinstaller.exe --onefile --hidden-import tkinter --icon=.\unique\icon\icon.ico unique\unique_gui.pyw

REM remove the .pyw file
ERASE unique\unique_gui.pyw
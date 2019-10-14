@ECHO OFF

cd ..\..\PySystem\PySystem\Python3\Scripts
pyinstaller.exe --onefile --noconsole --noupx ..\..\..\..\Programs\TextToSpeech\FunnStuf.py
Pause

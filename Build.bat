rem ŠÂ‹«•Ï” ANACONDA_ROOT: C:\Users\ƒ†[ƒU[\Anaconda3
pushd Scripts
call %ANACONDA_ROOT%\Scripts\activate.bat
call activate KanColleImageProcessor
pyinstaller Window.py --name HamColle.exe --onefile --distpath ../build/dist --workpath ../build/build --clean --noconsole --icon=../icon.ico
popd

rem ���ϐ� ANACONDA_ROOT: C:\Users\���[�U�[\Anaconda3
pushd Scripts
call %ANACONDA_ROOT%\Scripts\activate.bat
call activate KanColleImageProcessor
pyinstaller Window.py --name HamColle.exe --onefile --distpath ../build/dist --workpath ../build/build --clean --noconsole --icon=../icon.ico
popd

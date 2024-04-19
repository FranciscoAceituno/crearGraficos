@ECHO OFF

@REM rem Activar el entorno virtual
@REM call Scripts/activate

pip install -r requirements.txt

rem Ejecutar el script Python
python.exe main.py
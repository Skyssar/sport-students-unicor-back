@echo off
ECHO Borrando base de datos SQLite
DEL "db.sqlite3" /f > NUL

SET "keepfile=__init__.py"
for /D %%f in (*) do (
   IF exist "%%~nxf/migrations" ( 
      cd "%%~nxf/migrations"
      ECHO Borrando migraciones en %%f
      FOR /d %%a IN (*) DO RD /S /Q "%%a"
      FOR %%a IN (*) DO  IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
      cd ../..
   )
)

python manage.py makemigrations
python manage.py migrate

echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser("admin", "admin@example.com", "admin"); | python manage.py shell

echo "RESET SUCCESFULLY"
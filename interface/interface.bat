@echo off
:Menu
cls
echo Seleccione su opcion tecleando el numero respectivo.
echo.
echo 1. Iniciar Analizador
echo 2. Generar Plot de archivo
echo 3. Salir
set /p var=
if %var%==1 goto :Primero
if %var%==2 goto :Segundo
if %var%==3 goto exit
if %var% GTR 3 echo Error
goto :Menu
:Primero
cls 
color a
Echo Conecte Interface-FDR... entonces presione enter
Pause>Nul
Echo Ejecutando analizador... 
start interface.py
Echo Precione una tecla para volver al menu
Pause>Nul
goto :Menu
:Segundo
cls 
color a
Echo Ejecutando generador de Plot
start plot.py
Echo Precione una tecla para volver al menu
Pause>Nul
goto :Menu
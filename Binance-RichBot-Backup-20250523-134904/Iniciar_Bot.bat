@echo off
setlocal enabledelayedexpansion

echo ###############################################
echo #          BINANCE REDPACKET BOT             #
echo #  Verificando e instalando dependencias...  #
echo ###############################################
echo.

:: === VERIFICAR PYTHON ===
echo [1/4] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado o no está en el PATH.
    echo.
    echo Por favor, instala Python desde: https://www.python.org/downloads/
    echo IMPORTANTE: Durante la instalación, MARCA la opción "Add Python to PATH"
    echo.
    start "" "https://www.python.org/downloads/"
    pause
    exit /b 1
) else (
    for /f "tokens=2" %%a in ('python --version 2^>^&1') do set PYTHON_VERSION=%%a
    echo [OK] Python !PYTHON_VERSION! detectado.
)

:: === VERIFICAR PIP ===
echo.
echo [2/4] Verificando pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip no está disponible. Intentando instalar...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo [ERROR] No se pudo instalar pip. Por favor, reinstala Python.
        pause
        exit /b 1
    )
    echo [OK] pip instalado correctamente.
) else (
    for /f "tokens=2" %%a in ('pip --version 2^>^&1') do set PIP_VERSION=%%a
    echo [OK] pip !PIP_VERSION! detectado.
)

:: === ACTUALIZAR PIP ===
echo.
echo [3/4] Actualizando pip a la versión más reciente...
python -m pip install --upgrade pip >nul 2>&1
if %errorlevel% neq 0 (
    echo [ADVERTENCIA] No se pudo actualizar pip. Continuando con la versión actual...
) else (
    echo [OK] pip actualizado correctamente.
)

:: === INSTALAR DEPENDENCIAS ===
echo.
echo [4/4] Instalando dependencias necesarias...
echo.

set PACKAGES=telethon colorama httpx

for %%p in (%PACKAGES%) do (
    echo Verificando %%p...
    pip show %%p >nul 2>&1
    if !errorlevel! equ 0 (
        echo [OK] %%p ya está instalado.
    ) else (
        echo Instalando %%p...
        pip install %%p --user
        if !errorlevel! neq 0 (
            echo [ERROR] No se pudo instalar %%p.
            echo Intentando con privilegios de administrador...
            pip install %%p --user
            if !errorlevel! neq 0 (
                echo [ERROR] No se pudo instalar %%p. El bot podría no funcionar correctamente.
                pause
            )
        )
    )
)

:: === INICIAR EL BOT ===
echo.
echo ###############################################
echo #       INICIANDO BINANCE REDPACKET BOT       #
echo ###############################################
echo.
echo [INFO] Presiona Ctrl+C para detener el bot.
echo [INFO] Revisa la ventana para ver el progreso.
echo ===============================================
echo.

:start_bot
python main.py
set BOT_EXIT_CODE=!errorlevel!

if !BOT_EXIT_CODE! equ 0 (
    echo.
    echo [INFO] El bot se ha cerrado correctamente.
) else (
    echo.
    echo [ERROR] El bot se ha cerrado inesperadamente con código !BOT_EXIT_CODE!.
    echo [INFO] Reintentando en 5 segundos...
    timeout /t 5 /nobreak >nul
    goto start_bot
)

echo.
pause

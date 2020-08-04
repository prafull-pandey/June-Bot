@echo off

if not "%VIRTUAL_ENV%" == "" (

	goto gotHome

) else (

	cd ..

)

set "VIRTUAL_ENV=%cd%"

set "FLASK_APP=%cd%/app/http/api/endpoints.py"

cd "%CURRENT_DIR%"

:gotHome

if exist "%VIRTUAL_ENV%\Scripts\activate.bat" (

	goto okHome

) else (

	goto end

)

:okHome

echo %VIRTUAL_ENV%

echo %FLASK_APP%

set "CURRENT_DIR=%cd%"echo %CURRENT_DIR%
if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    if not defined PROMPT (
        set "PROMPT=$P$G"
    )
    if not defined VIRTUAL_ENV_DISABLE_PROMPT (
        set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
    )
)
if not defined VIRTUAL_ENV_DISABLE_PROMPT (
    set "ENV_PROMPT="
    if NOT DEFINED ENV_PROMPT (
        for %%d in ("%VIRTUAL_ENV%") do set "ENV_PROMPT=(%%~nxd) "
    )
    )
    set "PROMPT=%ENV_PROMPT%%PROMPT%"
)

REM Don't use () to avoid problems with them in %PATH%
if defined _OLD_VIRTUAL_PYTHONHOME goto ENDIFVHOME
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
:ENDIFVHOME

set PYTHONHOME=

REM if defined _OLD_VIRTUAL_PATH (
if not defined _OLD_VIRTUAL_PATH goto ENDIFVPATH1
    set "PATH=%_OLD_VIRTUAL_PATH%"
:ENDIFVPATH1
REM ) else (
if defined _OLD_VIRTUAL_PATH goto ENDIFVPATH2
    set "_OLD_VIRTUAL_PATH=%PATH%"
:ENDIFVPATH2

set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"
set "PATH=%VIRTUAL_ENV%;%PATH%"
:end

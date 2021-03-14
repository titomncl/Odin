echo off

set EXEC_PATH=%~dp0

set IPM_src="%EXEC_PATH%\ISART_PROJECT_MANAGER"
set ENV_SCRIPT_src="%EXEC_PATH%\Maya\init_env.py"

set IPM_dst="%userprofile%\ISART_PROJECT_MANAGER\"
set ENV_SCRIPT_dst="%userprofile%\Documents\maya\2019\scripts"

xcopy %IPM_src% %IPM_dst% /E
xcopy %ENV_SCRIPT_src% %ENV_SCRIPT_dst%

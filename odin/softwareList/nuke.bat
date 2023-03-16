SET NUKE_TEMP_DIR=D:\TMP\localize
MKDIR %NUKE_TEMP_DIR%

set HOME=C:\Users\%USERNAME%\
set NUKE_PATH=P:/Nuke/Custom/root

set PYTHONPATH=%PYTHONPATH%;%ROOT_PATH%;%PFE_ENV%;%DEV_ENV%;
set OCIO=%DEV_ENV%/OpenColorIO/aces_1.2/config.ocio

start "" %1 --nukex

set PYTHONPATH=%PYTHONPATH%;%ROOT_PATH%;%PFE_ENV%;%DEV_ENV%;
set OCIO=%DEV_ENV%/OpenColorIO/aces_1.2/config.ocio

start "" %1 --nukex

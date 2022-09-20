:: PYTHON 3.8 PATH
set GUERILLA_PYTHON_LIBRARY=%DEV_ENV%\Odin\venv\27\Scripts\python27.dll

set PYTHONHOME=%DEV_ENV%\Odin\venv\27
set PYTHONPATH=%DEV_ENV%\Odin\venv\27\Lib;%DEV_ENV%
set PATH=%PYTHONHOME%;%PATH%

set GUERILLA_SAMPLES=%1\samples

:: ADD TO PATH
::set PYTHONHOME=%DEV_ENV%\Odin\venv\27\Lib;%DEV_ENV%
::set PYTHONPATH=%PYTHONPATH%;%ROOT_PATH%;%PROJECT_ENV%;%DEV_ENV%
::set PATH=%PYTHONHOME%;%PATH%;%MAYA_INSTALL%\bin;%MAYA_INSTALL%\plug-ins\xgen\bin;

set VSPA=%PROJECT_ENV%
set OCIO=%DEV_ENV%/OpenColorIO/aces_1.2/config.ocio
set GUERILLA_CONF=%DEV_ENV%/Guerilla/Conf/guerilla.conf

start "" %1

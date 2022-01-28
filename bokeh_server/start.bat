
@REM EDIT SETTINGS HERE
@REM ----------------------------------------------------

@SET ENVNAME=base
@SET PY_APP_NAME=bokeh_app.py

@REM ----------------------------------------------------

@ECHO Activating conda environment %ENVNAME%...
@CALL %USERPROFILE%\Anaconda3\Scripts\activate.bat %USERPROFILE%\Anaconda3\envs\%ENVNAME%

@ECHO Serving bokeh app %PY_APP_NAME%
@bokeh serve --show %PY_APP_NAME%


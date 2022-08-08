@echo off
set "SOAR_HOME=%~dp0SoarSuite_9.6.0-Multiplatform_64bit\bin"
set "PATH=%SOAR_HOME%;%PATH%"

java -Djava.library.path="%SOAR_HOME%" -jar %~dp0test-domains\Mario-Soar.jar %1 %2

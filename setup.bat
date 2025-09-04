@echo off
echo Downloading the requirements

pip install numpy

echo Job well done, goodbye

(del "%~f0") >nul 2>&1

exit

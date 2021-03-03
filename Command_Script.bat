@ECHO OFF

SET Pass=sm20st07
SET HOSTNAME=smst@192.168.180.20
SET HOST=192.168.180.20

ECHO Welcome to DSS Command tool

SET COMMAND_PATH=%1
SET COMMAND_NAME=%2
SET ARGUMENTS=%3
SET SUDO=%4
echo ARG = %ARGUMENTS%
if %ARGUMENTS% equ false (SET ARGUMENTS="")

if %COMMAND_PATH% equ false (SET COMMAND=%COMMAND_NAME% %ARGUMENTS%
)else (SET COMMAND=%COMMAND_PATH%%COMMAND_NAME% %ARGUMENTS%)

if %SUDO% equ true (SET COMMAND=plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command%"
) else (SET COMMAND=plink -batch -ssh %HOSTNAME% -t -pw %Pass% %Command%)

%COMMAND% > C:\command\file.txt

exit





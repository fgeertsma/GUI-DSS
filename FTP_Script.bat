@ECHO OFF

SET Pass=sm20st07
SET HOSTNAME=smst@192.168.180.20
SET HOST=192.168.180.20

ECHO Welcome to DSS Command tool

SET COMMAND_PATH=%1
SET COMMAND_NAME=%2
SET ARGUMENTS=%3
SET SUDO=%4


pscp.exe -r -P 22 -pw %Pass% "%HOSTNAME%:/home/smst/influxdb/share/%Database_Name%" "%Backup_Path%%Database_Name%"


exit





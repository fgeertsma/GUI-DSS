

SET Pass=sm20st07
SET HOSTNAME=smst@192.168.180.20
SET HOST=192.168.180.20


SET Database_Path=%1
SET Database_Name=%2

@ECHO OFF
ECHO Welcome to DSS Export tool, Please login:

pscp.exe -r -P 22 -pw %Pass% %Database_Path%%Database_Name% %HOSTNAME%:/home/smst
SET Command=/home/smst/Restore_Backup_DB -p "/home/smst/" -n %Database_Name%
plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command%"

SET Command=/home/smst/Switch_DB -n %Database_Name%
plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command%"

SET Command_Remove="rm -r /home/smst/influxdb/share/%Database_Name%"
plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command_Remove%"

ECHO Finished exporting: %Database_Name%


EXIT



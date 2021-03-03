

SET Pass=sm20st07
SET HOSTNAME=smst@192.168.180.20
SET HOST=192.168.180.20

SET Backup_Path=C:\backup\


SET Start_Date=%1
SET End_Date=%2
SET Database_Name=dss

@ECHO OFF
ECHO Welcome to DSS Export tool, Please login:

SET Command_Backup="/home/smst/Create_Backup_DB -s %Start_Date% -e %End_Date% -d %Database_Name%"

if not exist %Backup_Path% mkdir %Backup_Path%																			


plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command_Backup%"					

plink -batch -ssh %HOSTNAME% -t -pw %Pass% ls /home/smst/influxdb/share/ > C:\backup\file.txt						


SET /p Database_Name=<C:\backup\file.txt
del C:\backup\file.txt


pscp.exe -r -P 22 -pw %Pass% "%HOSTNAME%:/home/smst/influxdb/share/%Database_Name%" "%Backup_Path%%Database_Name%"

SET Command_Remove="rm -r /home/smst/influxdb/share/%Database_Name%"

plink -batch -ssh %HOSTNAME% -t -pw %Pass% "echo -e %Pass% | sudo -S -i && sudo %Command_Remove%"						


ECHO Finished exporting: %Database_Name%


EXIT



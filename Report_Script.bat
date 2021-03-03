

SET Pass=sm20st07
SET HOSTNAME=smst@192.168.180.20
SET HOST=192.168.180.20

SET Report_Path=C:\Report\


SET Start_Date=%1
SET Start_Time=%2
SET End_Date=%3
SET End_Time=%4

echo %1

@ECHO OFF
ECHO Welcome to DSS Export tool, Please login:

SET Command="/home/smst/Creater -s %Start_Date% -t %Start_Time% -e %End_Date% -z %End_Time%"
SET File_Name="out.pdf"

if not exist %Report_Path% mkdir %Report_Path%


plink -batch -ssh %HOSTNAME% -t -pw %Pass% %Command%

pscp.exe -r -P 22 -pw %Pass% %HOSTNAME%:/home/smst/go/bin/%File_name% %Report_Path%

ECHO Finished exporting: Report


EXIT



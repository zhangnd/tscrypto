@echo off
type nul > input.txt
setlocal enabledelayedexpansion
set /a index=0
for /r tmp %1 %%i in (*) do (
    set /a index+=1
    openssl aes-128-cbc -d -in %%i -out tmp/!index!.ts -nosalt -K c7719993cb5b81ceb148f4a205d48f05 -iv 00000000000000000000000000000000
    echo file 'tmp/!index!.ts'>> input.txt
)
endlocal
pause

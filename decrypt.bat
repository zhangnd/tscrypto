@echo off
type nul > input.txt
setlocal enabledelayedexpansion
set /a index=0
for /r tmp %1 %%i in (*) do (
    set /a index+=1
    openssl aes-128-cbc -d -in %%i -out tmp/!index!.ts -nosalt -K 0b53fbec72cb3a6d4d9c8efbc23a025e -iv 00000000000000000000000000000000
    echo file 'tmp/!index!.ts'>> input.txt
)
endlocal
pause

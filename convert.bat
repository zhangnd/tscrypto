@echo off
ffmpeg -f concat -i input.txt -c copy out.mp4
pause

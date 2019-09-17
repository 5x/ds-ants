@echo off
mode con: cols=160 lines=30
Pushd "%~dp0"/../dist/run
run.exe
Pause&Exit
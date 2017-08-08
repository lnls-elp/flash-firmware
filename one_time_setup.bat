@echo off
SETLOCAL
SETLOCAL ENABLEDELAYEDEXPANSION


  
    CMD /C dpinst_64_eng.exe /SE /SW /SA /PATH %~dp0\ccs_base/emulation/windows/xds100_drivers/ftdi
  

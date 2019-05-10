@echo off
color 0a

netsh wlan show profile
set /p red = "[-] WiFi > "
netsh wlan show profile name=%red% key=clear

**[![ ](https://github.com/senkawolf/Software-List/blob/main/media/icons/prev25.png?raw=true) Back](/README.md)**

# How To Setup Windows 11 PC Without Microsoft Account

### Windows 11 23H2 and Windows 11 24H2

> [!IMPORTANT]
> Method last tested 01/01/2025

1. First Install Windows 11.
2. When the select a region dialogue screen appears press _SHIFT + F10_ this will bring up the command prompt Window.
3. Click on the Window to make it the active window (or you won't be able to type anything).
4. Now we can tell Windows 11 to create a new user account with this command:
    - `net user (insert name here) /add`
    - e.g `net user SenkaWolf /add`
5. Next we need to make this account an Administrator with this command:
    - `net localgroup Administrators (insert same name here) /add`
    - e.g `net localgroup Administrators SenkaWolf /add`
6. Next we need to continue the Windows out of Box experience with this command:
    - `cd OOBE`
7. Then type:
    - `msoobe.exe && shutdown.exe -r`
8. This will restart Windows 11.

9. When windows reboots there will be a password error, click ok.
10. Finally select your username from the bottom left and Windows 11 will continue the rest of the installation process.
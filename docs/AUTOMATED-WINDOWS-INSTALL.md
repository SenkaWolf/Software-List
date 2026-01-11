**[![ ](https://github.com/senkawolf/Software-List/blob/main/media/icons/prev25.png?raw=true) Back](/README.md)**

# Automated Windows Installation Guide

> [!IMPORTANT]
> Method last tested 11/01/2026

### Creating `unattend.xml` or `autounattend.xml` File

> [!CAUTION]
> Do not change or enable settings you don't understand!

1. Nevigate to [schneegans.de Unattend Generator](https://schneegans.de/windows/unattend-generator/) website.
2. Go through each section and setup as you desire. I will list the settings that I change and share some tips along the way. If I don't mention a setting below then leave it on the default! This isn't fully comprehensive guide and only outlines the most commonly needed features.
    - Select your Windows display language
    - Select your language preferences and keyboard layouts
    - Select your Home location and device setup region
    - Select your Processor architectures, this is most commonly `Intel/AMD 64-bit`. You can add more by Ctrl + Clicking the other options.
    - Setup settings
        - `☐ Bypass Windows 11 requirements check (TPM, Secure Boot, etc.)` - Tick this if your PC does not meet the Windows 11 requirements. You can check to see if your PC is compatable by going [here](https://support.microsoft.com/en-us/windows/windows-11-system-requirements-86c11283-ea52-4782-9efd-7674389a7ba3).
        - `☐ Hide any PowerShell windows during Windows Setup` - Tick this as long as you are not using interactive prompts. For beginners this is safe to tick.
    - Computer name - This option you can pick whatever suits your use case. The second option where you set a static name only use this is you only plan to intall on a single PC or Virtual Machine. If you wish to use this on multiple devices options one or two are best.
    - Compact OS - I recommend you select `☐ Do not use Compact OS`.
    - Windows edition - Pick from either of the following:
        - If you are installing onto a PC or virtual machine which has never had Windows on it before then I recommend selecting `☐ Use a generic product key` and picking the `home` or `Pro` depending on your use case.
        - If you are reformatting a PC which has Windows on it then select `☐ Use product key stored in BIOS/UEFI firmware`.
    - User accounts - 
        - Select `Let Windows Setup create the following local (“offline”) accounts` option if you wish you use a static user account, this is good for a single PC or testing virtual machines. Delete the `User` and rename the Admin account to suit your needs. I recommend that you don't set a password here and wait until you get into Windows.
        - Select ` Add a local (“offline”) user account interactively during Windows Setup` if you wish to use this installer across multiple computers.
    - File Explorer tweaks
        - Choose which files are hidden in File Explorer select `☐ Hide protected operating system files`.
        - Enable `☐ Always show file extensions`.
        - Enable `☐ Use classic context (right-click) menu in Windows 11`.
        - Enable `☐ Open File Explorer to This PC instead of Quick access`.
        - Enable `☐ Show End task command in the taskbar`.
    - Start menu and taskbar
        - Choose how to display the search box in the taskbar select either `☐ Icon` or `☐ Hide`.
        - Choose icons to display in the taskbar select `☐ Remove all icons`.
        - Enable `☐ Disable widgets`.
        - Enable `☐ Do not show Bing results when searching in the Start menu or the search box`.
        - Windows 10 Tiles enable `☐ Remove all tiles`.
        - Windows 11 pins enable `☐ Remove all pins`.
    - System tweaks
        - Enable `☐ Prevent Windows Update from rebooting your computer`.
        - Enable `☐ Disable app suggestions / Content Delivery Manager`.
        - Enable `☐ Hide Edge First Run Experience`.
        - Enable `☐ Disable Edge Startup Boost and Background mode`.
    - Desktop icons
        - Enable `☐ Delete Edge shortcut on desktop`.
        - Enable `☐ Show these desktop icons` then select:
            - Home
            - Recycle bin
    - Sticky keys - Enable `☐ Disable Sticky keys altogether`.
    - Personalization settings
        - Colors - Select `☐ Use custom color theme` then choose:
            - Set `Choose color theme for taskbar and Start menu` to Dark.
            - Set `Choose color theme for apps` to Dark.
            - Pick a accent color you like.
            - Enable `Show accent color on Start menu and taskbar ☐`.
            - Enable `Show accent color on title bars and window borders ☐`.
            - Enable `Windows and surfaces appear translucent ☐`.
    - Remove bloatware - Select All then uncheck:
        - Facial recognition (Windows Hello) - Unless you are on a desktop then leave checked.
        - Game Assist
        - Movies & TV
        - Photos
        - Remote Desktop Client
        - Windows Media Player (modern)
        - Xbox Apps
        - Paint 3D
        - Windows Terminal
        - Calculator
        - Notepad (modern)
        - Snipping Tool

Now download the .xml file.

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Adding the .xml file to a Windows ISO

1. Go to Microsoft website [here](https://www.microsoft.com/en-gb/software-download/windows11) and go to the section `Download Windows 11 Disk Image (ISO) for x64 devices` and download the file.
2. Go to AnyBurn website [here](https://anyburn.com/download.php) and download the free version and install.
3. Launch AnyBurn and select `Edit Image file`.
4. Then browse to the Windows IOS you downloaded in step 1.
5. Press next.
6. Press the add button and browse to the xml file you downloaded
7. Press next.
8. Rename the file to whatever you wish.
9. The press Create Now.

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)


Now you can launch a virtual machine off the ISO file or make a bootable USB drive to install Windows onto a computer using your custom ISO file.

You can always repeat the Adding the .xml file to a Windows ISO step when Microsoft releases new ISOs alongside Window updates.
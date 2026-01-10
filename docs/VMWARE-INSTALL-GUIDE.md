**[![ ](https://github.com/senkawolf/Software-List/blob/main/media/icons/prev25.png?raw=true) Back](/README.md)**

# VMware Workstation Pro Install Guide

> [!IMPORTANT]
> Method last tested 10/01/2026

### Download
1. Download the software from [here](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion).
2.  You will be redirected to Broadcom's website. Create an account or login if you have an account already.
3. Once logged in go to the 'My Downloads' section down the left hand side of the web page.
4. Then click on the 'Free Software Downloads available [HERE](https://support.broadcom.com/group/ecx/free-downloads)'
5. Scroll down the page and to go '[VMware Workstation Pro](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true)'
6. Then select the latest version then select the latest release.
7. You will now see a screen with '☐ I agree to the [Terms and Conditions](https://www.broadcom.com/company/legal/licensing)' you can't tick this until you have opened the Terms and Conditions page. Click the link and they will open in a new tab. Close the tab and you will now be able to tick the Terms and Conditions.
8. Now you will be able to click the download button (cloud icon ![Broadcoom download icon](https://github.com/senkawolf/Software-List/blob/main/media/guides/broadcoom-download-icon.png?raw=true)).
9. You will then get a popup stating additional verification is required. Click yes then fill in the form.
10. You will be returned to the previous page. Press the download button (cloud icon ![Broadcoom download icon](https://github.com/senkawolf/Software-List/blob/main/media/guides/broadcoom-download-icon.png?raw=true)) again and now the download will begin.
11. Before installing the file move onto the next section!

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Before installing
Some of these steps help prevent issues when installing/setting up virtual machines.

#### Windows Features
If you have either of the below enabled on your PC then VMWare won't be able to use CPU hardware virtualilasion directly so your virtual machines will run slower.
- Windows Hyper-V
- Virtual Machine Platform
- Windows Hypervisor Platform
- Windows Sandbox
- Windows Subsystem for Linux

To do this:
1. Search for 'Turn Windows features on or off' from your taskbar/menu.
2. Then scroll through the list and ensure the above options are unchecked then press Ok.
3. Reboot your PC.

#### BIOS
Ensure you have CPU Virtualisation enabled in your BIOS, check this by:
1. Opening Task Manager by right clicking your taskbar.
2. Go to the ![Performance Icon](https://github.com/senkawolf/Software-List/blob/main/media/guides/windows-performance-icon.png?raw=true) performance tab.
3. Under CPU it should say Virtualisation followed by enabled or disabled. If it is enabled you don't need to do anything however if it is disabled continue with the steps.
4. Restart your PC and access your BIOS.
5. In the BIOS you need to look for either of the following:
    - Intel CPU: Intel Virttualisation Technology or Intel VT-x.
    - AMD CPU: Secure Virtual Machine, or AMD-V, or AMD SVM.

> [!INFORMATION]
> Consult your motherboard manufactures website on how to access the BIOS and locate the CPU Virtualisation setting if you need further assistance.

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Install VMware Workstation Pro from the file downloaded earlier.
# pi-setup

### INITIAL SETUP FOR A RASPBERRY PI

Open chromium and install lastpass

### Update and Change hostname an preferences.

- run updates in upper right corner
- open preferences -> Raspberry pi configuration
- change the hostname (you'll need to reboot)
- turn on VNC and I2C
- set the keyboard to apple


### Connect Remotely

**TigerVNC**  
hostname.local

**VSCode or Cursor**  
Log into pi using SSH   
user@hostname.local

You may need to configure hosts first in VSCode. Remove the old ones. Then add a new host with the username and address.
You may also need to remove the hosts from .ssh at 
```
cd /Users/mm/.ssh/
sudo subl known_hosts
```

Clone this repo
```
git clone https://github.com/itaki/pi-setup.git
```

### Install Pi-Apps

```
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
```

### Install Software

**Preferences -> Recommended Software**
- VSCode

**Accessories -> Pi-Apps**
- Sublime Text
- ~~BetterChromium~~
- Conky
- More RAM




---
## SETUP FILE SHARING


**Install Samba**
```
sudo apt update
sudo apt install samba
```

**Edit the etc/samba/smb.config file**
```
sudo subl /etc/samba/smb.config
```

**Use this**

```
#======================= Global Settings =======================

[global]

## Browsing/Identification ###
   workgroup = WORKGROUP

#### Networking ####
# The specific set of interfaces / networks to bind to
# This can be either the interface name or an IP address/netmask;
# interface names are normally preferred
;   interfaces = 127.0.0.0/8 eth0

# Only bind to the named interfaces and/or networks; you must use the
# 'interfaces' option above to use this.
;   bind interfaces only = yes

#### Debugging/Accounting ####
   log file = /var/log/samba/log.%m
   max log size = 1000
   logging = file
   panic action = /usr/share/samba/panic-action %d

####### Authentication #######
   server role = standalone server
   obey pam restrictions = yes
   unix password sync = yes
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
   pam password change = yes
   map to guest = bad user

############ Misc ############
   usershare allow guests = yes

#======================= Share Definitions =======================

[homes]
   comment = Home Directories
   browseable = no
   read only = yes
   create mask = 0700
   directory mask = 0700
   valid users = %S

[printers]
   comment = All Printers
   browseable = no
   path = /var/tmp
   printable = yes
   guest ok = no
   read only = yes
   create mask = 0700

[print$]
   comment = Printer Drivers
   path = /var/lib/samba/printers
   browseable = yes
   read only = yes
   guest ok = no

# Your new share definition
[mm]
   comment = MM's Home Directory
   path = /home/mm
   browseable = yes
   read only = no
   create mask = 0755
   directory mask = 0755
   valid users = mm
   force user = mm
   force group = mm
```
Setup password and restart samba

```
sudo smbpasswd -a mm
sudo systemctl restart smbd
```

Connect from your mac with cmd+k

---

### Install the command line stuff

This should work automatically in remote vscode since menslo is installed. But for local you need to install fonts. Run this script generate by AI
```

```
logout and log back in
prompt

**zsh**
https://divinenanny.nl/blog/2021-08-07-install-oh-my-zsh-on-raspberry-pi/

**ohmyzsh**
https://github.com/ohmyzsh/ohmyzsh

**powerlevel10K**
https://github.com/romkatv/powerlevel10k




***We should now be connected via VNC and in VSCode Terminal***




When VS Code starts I can link it to my personal settings but this fucks up terminal so 
then I need to setup ohmyzsh and power10k
Have to install zsh on the pi
```
sudo apt install zsh

$ zsh --version

$ echo $SHELL
$ chsh -s $(which zsh) 
or 
$ chsh -s /usr/bin/zsh

```
The restart vscode not just the terminal
Choose system admin settings 

Install the fonts
$ mkdir ~/.local/share/fonts
copy fonts there
$ fc-cache -f -v


Then install powerlevel10k
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```
1. set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.


Visual Studio Code: Open File → Preferences → Settings (PC) or Code → Preferences → Settings (Mac), enter terminal.integrated.fontFamily in the search box at the top of Settings tab and set the value below to MesloLGS NF.


Install Menlo font - note: this would have been done above during the vscode configuration
```
sudo mkdir /usr/share/fonts/truetype/newfonts
sudo cp ./fonts/*  /usr/share/fonts/truetype/newfonts
fc-cache -f -v
fc-list

#may need to install 
sudo apt install libsdl2-ttf-2.0-0
```

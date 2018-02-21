#!/bin/bash
# -*- coding: UTF-8 -*-

# Tested On Linux Operation System

# [
#   Developer: Sir Uidops
#   Email    : Sir.u1d0p5@gmail.com
#   Github   : https://github.com/siruidops/knowmail/
# ]

clear
echo
echo "    [+] Installing The KnowMail Script | Update System ..."
echo
apt-get update -y
clear
echo
echo "    [+] Installing The KnowMail Script | Install Python ..."
echo
apt-get install python python-dev python-pip -y
clear
echo
echo "    [+] Installing The KnowMail Script | Install Library ..."
echo
pip install validate_email==1.3
clear
echo
echo "    [+] Installing The KnowMail Script | Copy To /opt/knowmail/"
echo
mkdir /opt/knowmail
cp * /opt/knowmail/
sleep 3s
clear
echo
echo "    [+] Installing The KnowMail Script | Creat Symlink To /usr/bin/knowmail"
echo
cp run.sh /usr/bin/knowmail
sleep 3s
clear
echo
echo "    [!] Finished! | Run KnowMail With Command 'knowmail'"
echo
sleep 3s
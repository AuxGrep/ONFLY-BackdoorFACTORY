#!/usr/bin/bash
#Written by AuxGrep
#2022

BOLD="\033[01;01m"     
RED="\033[01;31m"      
GREEN="\033[01;32m"    
YELLOW="\033[01;33m"   
RESET="\033[00m"
UBlack='\033[4;30m'       # Black
URed='\033[4;31m'         # Red
UGreen='\033[4;32m'       # Green
UYellow='\033[4;33m'      # Yellow
UBlue='\033[4;34m'        # Blue
UPurple='\033[4;35m'      # Purple
UCyan='\033[4;36m'        # Cyan
UWhite='\033[4;37m'       # White

if [ $EUID -ne 0 ]; then # Super User Check
  echo -e "\\033[31mAborted, please execute the script as root!!Damn!!!\\033[0m"; exit 1
fi

if [  -e /usr/bin/pv ]; then
    echo -e $GREEN "[ ✔ ] pv ................[ found ]"
else 
	echo -e $RED "[ X ] pv -> not found "
	echo -e "\n [*] ${YELLOW} Installing pv ${RESET}\n"
	sudo apt-get install pv
fi

if [ -e /usr/bin/winexe ]; then
    echo -e $GREEN "[ ✔ ] wine ................[ found ]"
else
	echo -e $RED "[ X ] wine -> not found "
	echo -e "\n [*] ${YELLOW} Installing wine ${RESET}\n"
	sudo apt-get install wine
fi
sleep 2
clear
echo -e "INSTALLING autoit-v3"
echo ""
sudo wine setup.exe
clear
echo -e $YELLOW"GOOD LUCKY!!!" $RESET


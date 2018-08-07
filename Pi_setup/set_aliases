#!/usr/bin/env bash
#This script sets user made aliases
FILE=~/.bashrc
sudo echo -e "\n#User set Aliases
alias r=\"rm *~\"
alias cl=\"clear && ls -v1\"
alias bashrestart=\". ~/.bashrc\"" | sudo tee -a $FILE
sudo rm ~/.bashrc~
. ~/.bashrc

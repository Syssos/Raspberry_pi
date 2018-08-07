#!/usr/bin/env bash
# Create's script that creates scripts
FILE=~/.create_shell_script
touch $FILE
chmod u+x $FILE
sudo echo -e "#!/usr/bin/env bash
# Create's script
FILE = \"$1\"
touch $FILE
chmod $FILE" | sudo tee -a $FILE
#ADD AILIAS
ALIAS=~/.bashrc
sudo echo -e "alias excre=\"~/.create_shell_script\"
" | sudo tee -a $ALIAS
sudo rm ~/.bashrc~
. ~/.bashrc

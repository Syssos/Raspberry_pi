#!/usr/bin/env bash
# Create's script that creates scripts
FILE=~/.gitcom
touch $FILE
chmod u+x $FILE
sudo echo -e "#!/usr/bin/env bash
# add/commit file to git
git add \"\$1\"
git commit -m \"\$2\"
" | sudo tee -a $FILE

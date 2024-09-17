#!/usr/bin/bash

# 
# Sets everything up to start coding the new js projects.
# You can either run the whole script or copy and paste parts of it to bash.
# If you run the whole script make sure to be in the js repo.
# I have no idea if nvm installs npm automatically, you should check that it
# does.
# 
# To run files you have to be inside the folder where node_modules is,
# if it doesn't coincide with the script you must provide the path to the
# script.
# 
# Example:
# Instead of
# npm run dev 0-main.js
# You might use
# npm run dev ES6_basic/0-main.js
# 
# Made by Matias Davezac <matiasdavezac@gmail.com>
# 


# Installs nvm to handle nodejs version control
# Script taken from https://github.com/nvm-sh/nvm?tab=readme-ov-file#manual-install

export NVM_DIR="$HOME/.nvm" && (
  git clone https://github.com/nvm-sh/nvm.git "$NVM_DIR"
  cd "$NVM_DIR"
  git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`
) && \. "$NVM_DIR/nvm.sh"

echo -e '\n' >> $HOME/.bashrc
echo 'export NVM_DIR="$HOME/.nvm"' >> $HOME/.bashrc
echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> $HOME/.bashrc
echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"' >> $HOME/.bashrc

# Installs nodejs and also npm apparently

nvm install 12.11.1

# Adds the node_modules folder to be ignored as there is going to be more than
# a million files inside of it that are going to break git. It may break
# anyway though. Restart vs code if it does.
# Make sure to be in the new repo's root.

echo -e "\nnode_modules" >> .gitignore

# Installs everything that the summary asks in project ES6 Basics.

npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint


# Installs dependencies in node_modules

npm install

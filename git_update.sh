#!/bin/sh

#git remote set-url --delete origin git@github.com:fastec02/tools
#git remote set-url --add origin git@github.com:fastec02/tools
#git remote set-url --delete origin git://github.com/fastec02/tools
git add *
git commit -a -m "update $(date)"
git pull origin master
git push

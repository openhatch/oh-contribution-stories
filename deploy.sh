#!/bin/sh
set -e   # if there's an error, stop running
set -x   # print each command as it runs
bin/pelican content -s settings.py
bin/ghp-import output -m "Regenerate site"
git checkout gh-pages
echo "mergestories.com" > CNAME
git add CNAME
git commit -m "commit CNAME file"
git checkout master
git push origin gh-pages


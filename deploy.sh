#!/bin/sh

bin/pelican content -s settings.py
bin/ghp-import output -m "Regenerate site"
git push origin gh-pages


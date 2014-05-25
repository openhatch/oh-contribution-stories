#!/bin/sh

bin/pelican content
bin/ghp-import output -m "Regenerate site"
git push origin gh-pages


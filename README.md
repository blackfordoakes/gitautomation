# Git Automation

Automated git process using python

## Prerequesites

GitPython needs to be installed via pip

`# pip install GitPython`

## Release.py

This script will tag the current commit with the given version number and move the QA tag to point to it.

## Hotfix.py

This script will branch from the given tag so you can create a hotfix from a certain release.
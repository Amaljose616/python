#! /usr/bin/bash

echo "new line" > test

git status
git add .
git commit -m "new line added to test"

git push -u origin main
#!/bin/bash

git add .
git merge
git commit -m "$@"
git push
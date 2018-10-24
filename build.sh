#!/bin/bash
rm -rf get_posts/build/
pipenv lock -r > requirements.txt
pip install -r requirements.txt -t  get_posts/build/
cp -R get_posts/app.py get_posts/build/

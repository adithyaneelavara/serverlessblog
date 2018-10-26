#!/bin/bash
rm -rf get_posts/build/
pipenv lock -r > requirements.txt
pip install -r requirements.txt -t  get_posts/build/
cp -R get_posts/app.py get_posts/build/

rm -rf put_posts/build/
pipenv lock -r > requirements.txt
pip install -r requirements.txt -t  put_posts/build/
cp -R put_posts/app.py put_posts/build/


#!/bin/bash

rm -Rf ../*/env/
virtualenv env
env/bin/pip install -r requirements.txt
rm helpers.py
rm structures.py
rm primes.py
rm primes.txt
ln -s ../default/primes.py ./
ln -s ../default/primes.txt ./
ln -s ../default/helpers.py ./
ln -s ../default/structures.py ./

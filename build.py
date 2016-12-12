"""
Author: Eric J. Ma
Date: 12 December 2016
Purpose: This script will do the following things:
1. If there is no hash record of a PDF file in the `figures/` directory, then
   the script will create a hash and store it.
2. If there is a hash record, then the script will compare the current file
   hash against the existing file hash, and return whether the hash has
   changed or not.
"""

import logging
import os
import hashlib
import yaml

logging.basicConfig(level=logging.INFO)


def hashfile(f, hasher, blocksize=65536):
    buf = f.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = f.read(blocksize)
    return hasher.hexdigest()


figures = [
    'collaborative-filtering',
    'influenza',
    'networks',
    'panama',
    'recommender',
]

hashes = dict()
for fig in figures:
    with open('figures/{0}.pdf'.format(fig), 'rb') as f:
        fhash = hashfile(f, hashlib.sha256())
        hashes[fig] = fhash

with open('hash.log', 'w+') as f:
    yaml.dump(hashes, f, canonical=False, default_flow_style=False)
# logging.info(yaml.dump(hashes))

with open('hash.log', 'r+') as f:
    loaded_hashes = yaml.load(f)
    logging.info(loaded_hashes)

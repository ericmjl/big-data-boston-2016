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

logging.basicConfig(level=logging.DEBUG)


def hashfile(f, hasher, blocksize=65536):
    buf = f.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = f.read(blocksize)
    return hasher.hexdigest()


files = [
    'figures/networks.pdf',
    'figures/recommender.pdf',
    'figures/collaborative-filtering.pdf',
    'figures/panama.pdf',
    'figures/influenza.pdf',
    'figures/convolutions.pdf',
    'figures/hairballs.pdf',
    'figures/rational-viz.pdf',
    'slides.md',
]

hashes = dict()
for fname in files:
    with open('{0}'.format(fname), 'rb') as f:
        fhash = hashfile(f, hashlib.sha256())
        hashes[fname] = fhash

print(hashes)
# If hash log doesn't exist, write to disk.
if 'hash.log' not in os.listdir():
    print('hash.log' in os.listdir())
    with open('hash.log', 'w+') as f:
        yaml.dump(hashes, f, canonical=False, default_flow_style=False)


with open('hash.log', 'r+') as f:
    prev_hashes = yaml.load(f)


# Check if hashes are identical or not. Priority order is as such:
# 1. If any images or the slides are changed, rebuild slides.
# 2. If none of the images are changed and
no_files_changed = True
for f in files:
    logging.debug(f)
    if hashes[f] == prev_hashes[f]:
        logging.info('file {0} unchanged.'.format(f))
    else:
        no_files_changed = False
        logging.info('file {0} has changed'.format(f))
        if f[-4:] == '.pdf':
            fstr = f[:-4]
            os.system("convert -density 300 -resize 50% {0} \
                {1}.png".format(f, fstr))

if not no_files_changed:
    logging.info('converting slides to PDF...')
    os.system("pandoc slides.md -t beamer -o slides.pdf \
        --template=default.beamer")

    logging.info('converting slides to HTML...')
    os.system("pandoc slides.md -o index.html -H docs/css/styles.css \
        --template=default.html")

# Write new hashes to disk.
with open('hash.log', 'w+') as f:
    yaml.dump(hashes, f, canonical=False, default_flow_style=False)
    logging.info('file hashes are:')
    logging.info(hashes)



logging.info('checking status of the repository')
os.system('git status')

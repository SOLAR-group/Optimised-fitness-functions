#!/bin/sh

cp data/random1.png data/random1_tmp.png
gzip data/random1_tmp.png
gzip -d data/random1_tmp.png.gz
rm data/random1_tmp.png

cp data/random1.txt data/random1_tmp.txt
gzip data/random1_tmp.txt
gzip -d data/random1_tmp.txt.gz
rm data/random1_tmp.txt
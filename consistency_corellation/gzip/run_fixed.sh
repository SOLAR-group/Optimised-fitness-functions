#!/bin/sh

bzip2 data/random1.txt
bzip2 -d data/random1.txt.bz2
[ -f 'data/random1.txt.bz2'  ] && rm data/random1.txt.bz2 



bzip2 data/random1.png
bzip2 -d data/random1.png.bz2
[ -f 'data/random1.png.bz2'  ] && rm data/random1.png.bz2 
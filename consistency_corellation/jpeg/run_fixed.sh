#!/bin/sh
jpeg-6a/cjpeg -dct int -progressive -opt -outfile dim2.jpeg data/random4.ppm
jpeg-6a/djpeg -dct int -ppm -outfile dim2.ppm data/random4.jpeg
rm dim2.jpeg
rm dim2.ppm
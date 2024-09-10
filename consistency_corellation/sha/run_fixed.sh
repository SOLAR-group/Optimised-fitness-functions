#!/bin/bash
for i in {1..14}; do
  ./sha random1.asc
  # ./sha random2.asc
  ./sha input_large.asc
  ./sha input_small.asc
done
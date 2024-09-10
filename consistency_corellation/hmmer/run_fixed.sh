#!/bin/bash
for i in {1..10}; do
  hmmsearch fn3.hmm uniprot_sprot.fasta
done
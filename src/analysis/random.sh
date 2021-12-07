#!/bin/bash
rm -f ../data/random.dat
touch ../data/random.dat
for i in {1..9}
do
   echo -n "$RANDOM," >> ../data/random.dat
done
echo -n "$RANDOM" >> ../data/random.dat
#!/bin/bash

for f in **/*.md; do
  out=$(dirname $f)/$(basename $f .md).html
  echo $out
  pandoc -s -c ../tufte.css $f -o $out
done

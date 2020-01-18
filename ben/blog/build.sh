#!/bin/bash

for f in **/*.md; do
  out=$(dirname $f)/$(basename $f .md).html
  echo $out
  pandoc -s -c ../../style.css $f -o $out
done

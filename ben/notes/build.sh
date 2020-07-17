#!/bin/bash

for f in ~/notes/*.org; do
    base_file=$(basename "$f" .org)
    out=$base_file.html
    echo "$out"
    pandoc -s -c ../style.css "$f" -o "$out" --metadata pagetitle="$base_file"
done

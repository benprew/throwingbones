#!/bin/bash

rsync -aiv -e 'ssh -p 2200' *.html *.css root@tuo.throwingbones.com:/var/www/html/throwingbones/ben/blog/
for f in 20*; do
  rsync -aiv -e 'ssh -p 2200' $f root@tuo.throwingbones.com:/var/www/html/throwingbones/ben/blog/
done

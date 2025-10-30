#!/bin/bash

# Blog publishing script with tag support
# This script publishes the blog and generates tag pages

cd ~/src/throwingbones/blog_src

echo "Publishing blog..."
emacs --batch -q --load ~/dotfiles/blog/init.el --eval "(org-publish-all)"

echo "Generating tag pages and index..."
emacs --batch -q --load ~/dotfiles/blog/init.el --eval "(progn (clrhash my-blog-tags-table) (clrhash my-blog-posts-table) (dolist (file (directory-files \"~/src/throwingbones/blog_src/org\" t \"\\.org$\")) (my-blog-collect-tags file \"~/src/throwingbones/ben/blog\")) (my-blog-generate-tag-pages \"~/src/throwingbones/ben/blog\") (my-blog-generate-index-page \"~/src/throwingbones/ben/blog\"))"

echo "Blog published successfully!"
echo "Generated files:"
ls -la ~/src/throwingbones/ben/blog/
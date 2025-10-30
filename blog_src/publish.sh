#!/bin/bash

# Blog publishing script with tag support
# This script publishes the blog and generates tag pages

cd ~/blog

echo "Publishing blog..."
emacs --batch -q --load ~/dotfiles/blog/init.el --eval "(org-publish-all)"

echo "Generating tag pages and index..."
emacs --batch -q --load ~/dotfiles/blog/init.el --eval "(progn (clrhash my-blog-tags-table) (clrhash my-blog-posts-table) (dolist (file (directory-files \"~/blog/org\" t \"\\.org$\")) (my-blog-collect-tags file \"~/blog/public\")) (my-blog-generate-tag-pages \"~/blog/public\") (my-blog-generate-index-page \"~/blog/public\"))"

echo "Blog published successfully!"
echo "Generated files:"
ls -la ~/blog/public/
#!/bin/bash

# Blog publishing script with tag support
# This script publishes the blog and generates tag pages
#
# Usage: ./publish.sh [-f|--force]
#   -f, --force    Force republish all files (clears timestamp cache)

FORCE=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -f|--force)
      FORCE=true
      shift
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: ./publish.sh [-f|--force]"
      exit 1
      ;;
  esac
done

# Clear cache if force flag is set
if [ "$FORCE" = true ]; then
  echo "Force republish: clearing timestamp cache..."
  rm -rf ~/.org-timestamps/
fi

echo "Publishing blog (with tags and index)..."
emacs --batch -q --load elisp/init.el --eval "(org-publish-all)"

echo "Blog published successfully!"
echo "Generated files:"
ls -la ../ben/blog/

#!/bin/bash

# Deploy script to integrate org blog into throwingbones
set -e

echo "Building blog..."
./publish.sh

echo "Copying blog files to throwingbones..."
# Copy all generated files from public/ to throwingbones/ben/blog/
rsync -av --delete ~/blog/public/ ~/src/throwingbones/ben/blog/

echo "Deploying to server..."
cd ~/src/throwingbones
make deploy

echo "Blog deployed successfully!"
echo "Available at: https://throwingbones.com/ben/blog/"
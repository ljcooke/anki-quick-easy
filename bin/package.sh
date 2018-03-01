#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o xtrace

anki20=$PWD/dist/anki20
anki21=$PWD/dist/anki21

mkdir -p "$anki20"
mkdir -p "$anki21"

# Copy the contents of the package to a temporary directory
tmp=$(mktemp -d)
cp quick_easy/*.* "$tmp"

# Copy a single file for Anki 2.0
cp "$tmp"/quick_easy.py "$anki20"

# Zip the files for Anki 2.1
(cd "$tmp" && zip -X quick_easy.zip ./*.*)
mv "$tmp"/quick_easy.zip "$anki21"

# Clean up
rm "$tmp"/*.*
rmdir "$tmp"

find dist -type f

#!/bin/bash

# Convert all SVG files to PNG with uppercase filenames
cd "$(dirname "$0")/.." || exit 1

for file in svg/*.svg; do
    filename=$(basename "$file" .svg)
    uppercase=$(echo "$filename" | tr '[:lower:]' '[:upper:]')
    echo "Converting $filename to $uppercase.png (144x144)"
    rsvg-convert -w 144 -h 144 "$file" -o "png/${uppercase}.png"
done

echo "All SVG files converted to PNG!"

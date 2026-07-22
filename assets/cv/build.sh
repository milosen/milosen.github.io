#!/bin/sh
# Compile CV and copy to assets/cv.pdf for the website.
# Run from anywhere in the repo: sh assets/cv/build.sh
set -e
cd "$(dirname "$0")"
mkdir -p build
pdflatex -output-directory=build -interaction=nonstopmode main.tex
pdflatex -output-directory=build -interaction=nonstopmode main.tex
cp build/main.pdf ../cv.pdf
echo "Done — assets/cv.pdf updated."

#!/bin/bash
# Build ZKAuth paper with tectonic
set -e
cd "$(dirname "$0")/../paper"
echo "[ZKAuth] Building paper with tectonic..."
tectonic main.tex
echo "[ZKAuth] PDF generated: main.pdf"

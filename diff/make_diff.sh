#!/bin/bash
# Regenerate diff/main-diff.{tex,pdf}: content changes between the USENIX
# camera-ready version (commit e2e18cd) and the current TDSC version.
# The old sections are rendered with the current TDSC main.tex, so the diff
# shows content changes rather than the template switch.
set -e
BASE=${1:-e2e18cd}
ROOT=$(git rev-parse --show-toplevel)
W=$(mktemp -d)
mkdir -p "$W/old" "$W/new" "$W/build"
git -C "$ROOT" archive "$BASE" | tar -x -C "$W/old"
git -C "$ROOT" archive HEAD    | tar -x -C "$W/new"
cp "$W/new/main.tex" "$W/old/main.tex"
latexdiff --flatten --type=UNDERLINE \
  --config="PICTUREENV=(?:picture|DIFnomarkup|tabular|tabularx)[\w\d*@]*" \
  "$W/old/main.tex" "$W/new/main.tex" > "$W/build/main-diff.tex"
cp -r "$W/old/img" "$W/build/" && cp -rn "$W/new/img/"* "$W/build/img/"
cp "$W/new/library.bib" "$W/build/"
( cd "$W/build" && pdflatex -interaction=nonstopmode main-diff.tex >/dev/null \
  && bibtex main-diff >/dev/null && pdflatex -interaction=nonstopmode main-diff.tex >/dev/null \
  && pdflatex -interaction=nonstopmode main-diff.tex >/dev/null )
cp "$W/build/main-diff.tex" "$W/build/main-diff.pdf" "$ROOT/diff/"
echo "written: $ROOT/diff/main-diff.pdf"

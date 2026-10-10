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
# Relative paths keep latexdiff's \input resolution working on Windows.
( cd "$W" && latexdiff --flatten --type=UNDERLINE \
  --config="PICTUREENV=(?:picture|DIFnomarkup|tabular|tabularx)[\w\d*@]*" \
  old/main.tex new/main.tex > build/main-diff.tex )
cp -r "$W/old/img" "$W/build/" && cp -rn "$W/new/img/"* "$W/build/img/"
cp "$W/new/library.bib" "$W/build/"
# pdflatex and bibtex return non-zero on warnings; check the PDF instead.
( cd "$W/build"
  pdflatex -interaction=nonstopmode main-diff.tex >/dev/null || true
  bibtex main-diff >/dev/null || true
  pdflatex -interaction=nonstopmode main-diff.tex >/dev/null || true
  pdflatex -interaction=nonstopmode main-diff.tex >/dev/null || true )
test -s "$W/build/main-diff.pdf"
cp "$W/build/main-diff.tex" "$W/build/main-diff.pdf" "$ROOT/diff/"
echo "written: $ROOT/diff/main-diff.pdf"

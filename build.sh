# python build.py

# pandoc slides.md -t beamer -o slides.pdf \
#     --template=default.beamer
#
# pandoc slides.md -o index.html -H docs/css/styles.css \
#     --template=default.html
#
pandoc slides.md --section-divs -t revealjs -o slides.html \
    --template=default.revealjs \
    -c styles.css -s

git status

# python build.py

# pandoc slides.md -t beamer -o slides.pdf \
#     --template=default.beamer
#
# pandoc slides.md -o index.html -H docs/css/styles.css \
#     --template=default.html
#
pandoc slides.md \
    --section-divs \
    -t revealjs \
    --template=default.revealjs \
    -c styles.css \
    -s \
    -o slides.html

git add .
git commit
git push

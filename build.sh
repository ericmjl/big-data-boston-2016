python build.py

# Make PDF version of slides
# pandoc slides.md -t beamer -o slides.pdf \
#     --template=default.beamer

# Make HTML notes version of slides
pandoc slides.md -o index.html -H docs/css/styles.css \
    --template=default.html

# Make revealjs version of slides
pandoc --section-divs -t revealjs -s --template template.revealjs -o slides.html slides.md

# Automatically add and commit
git add .
git commit
git push

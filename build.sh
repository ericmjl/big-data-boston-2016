convert -density 300 -resize 50% figures/networks.pdf figures/networks.png
convert -density 300 -resize 50% figures/recommender.pdf figures/recommender.png
convert -density 300 -resize 50% figures/collaborative-filtering.pdf figures/collaborative-filtering.png

pandoc slides.md -t beamer -o slides.pdf
pandoc slides.md -o index.html -H docs/css/styles.css

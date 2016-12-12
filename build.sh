convert -density 300 -resize 50% figures/networks.pdf figures/networks.png
convert -density 300 -resize 50% figures/recommender.pdf figures/recommender.png
convert -density 300 -resize 50% figures/collaborative-filtering.pdf figures/collaborative-filtering.png
convert -density 300 -resize 50% figures/panama.pdf figures/panama.png
convert -density 300 -resize 50% figures/influenza.pdf figures/influenza.png
convert -density 300 -resize 50% figures/convolutions.pdf figures/convolutions.png
convert -density 300 -resize 50% figures/hairballs.pdf figures/hairballs.png
convert -density 300 -resize 50% figures/rational-viz.pdf figures/rational-viz.png


pandoc slides.md -t beamer -o slides.pdf\
    --template=default.beamer
pandoc slides.md -o index.html -H docs/css/styles.css\
    --template=default.html

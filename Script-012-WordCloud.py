#!/usr/bin/env python
# coding: utf-8
import os
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# create a list of word
text = open('Wordcloud-Mariana.txt').read()
fish_mask = np.array(Image.open(path.join(d, "fish-1.jpg")
                                )
                     )

# create wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0,
                      background_color="white", mask=fish_mask,
                      contour_width=1, contour_color='grey',
                      colormap='viridis'
                      ).generate(text)

# plotting
plt.imshow(wordcloud, interpolation='bilinear', cmap=plt.cm.gray)
plt.axis("off")
plt.margins(x=0, y=0)

# visualizing and saving
plt.savefig('plot_WordC.png', dpi=300)
plt.show()

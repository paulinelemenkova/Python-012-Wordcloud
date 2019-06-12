#!/usr/bin/env python
# coding: utf-8
#
from wordcloud import WordCloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
#
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#
# Create a list of word
text = open('Wordcloud-Sea.txt').read()
fish_mask = np.array(Image.open(path.join(d, "fish-3.jpg")))
#
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0,
                      background_color="white", mask=fish_mask, contour_width=1, contour_color='grey', colormap='winter').generate(text)
#
# Display image:
plt.imshow(wordcloud, interpolation='bilinear', cmap=plt.cm.gray)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

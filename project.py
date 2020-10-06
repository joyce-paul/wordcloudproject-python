# Import libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of words for the wordcloud
text=("mySkills mySkills mySkills mySkills HTML HTML HTML CSS CSS CSS Coding Python Python JavaScript SQL Matplotlib Pandas Visualization Visualization pageLayout inDesign Dataviz Wordcloud Barcharts Writing Writing Editing Editing projectManagement")

# Wordcloud object
wordcloud = WordCloud(width=540, height=540, margin=0, background_color="orange", max_words=12, colormap="Blues").generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
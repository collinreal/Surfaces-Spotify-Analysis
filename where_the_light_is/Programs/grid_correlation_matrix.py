import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = 'C:\\Users\\12103\\Documents\\Surfaces Data\\extracted_spotify_data.xlsx'

dataframe = pd.read_excel(open(path, 'rb'),
                          sheet_name='Where_the_Light_Is')

dataframe = dataframe[['danceability', 'energy', 'speechiness',
                       'acousticness', 'instrumentalness', 'liveness', 'valence', 'song_name']]

dataframe = dataframe.set_index('song_name')

corrmat = dataframe.corr()

cg = sns.clustermap(corrmat, cmap="YlGnBu", linewidths=0.1)
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)

plt.savefig(
    'C:\\Users\\12103\\Documents\\Surfaces Data\\where_the_light_is\\Grid Correlation Matrix.pdf')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = 'C:\\Users\\12103\\Documents\\Surfaces Data\\extracted_spotify_data.xlsx'

dataframe = pd.read_excel(open(path, 'rb'),
                          sheet_name='Where_the_Light_Is')
dataframe = dataframe[['danceability', 'valence']]
sns.regplot('danceability', 'valence', data=dataframe)
plt.title('danceability vs. valence correlation')
plt.savefig(
    'C:\\Users\\12103\\Documents\\Surfaces Data\\WTLI - danceability vs. valence.pdf')

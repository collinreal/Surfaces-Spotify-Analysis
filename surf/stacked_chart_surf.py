import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

path = 'C:\\Users\\12103\\Documents\\Surfaces Data\\surfaces_data.xlsx'

dataframe = dataframe = pd.read_excel(open(path, 'rb'),
                                      sheet_name='Surf')
labels = ['The Way', 'Be Alright', '24/7/365', 'Falling', 'Alone',
          'Seattle Interlude', 'Loving', 'Stay', 'Islands', 'Ocean Breeze', 'Kid Kingdoms']
index = np.arange(11)
dataframe.plot(kind='bar', stacked=True)
plt.title('"Surf" Attribute Chart', color='gray')
plt.axis([1, 10, 0.0, 5.5])
plt.xticks(index, labels, rotation='horizontal', fontsize=4,)
plt.savefig('C:\\Users\\12103\\Documents\\Surfaces Data\\stacked_chart_surf.pdf')

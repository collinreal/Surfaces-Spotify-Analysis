import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

path = 'C:\\Users\\12103\\Documents\\Surfaces Data\\surfaces_data.xlsx'

dataframe = dataframe = pd.read_excel(open(path, 'rb'),
                                      sheet_name='Where_the_Light_Is')
labels = ['Beautiful Day', 'Shine on Top', 'Heaven Falls', 'This View',
          'Grace', 'Outside Interlude', 'Sunday Best', 'Where the Light Is', 'Someday', 'Home']
index = np.arange(10)
dataframe.plot(kind='bar', stacked=True)
plt.title('"Where the Light Is" Attribute Chart', color='gray')
plt.axis([1, 9, 0.0, 5.5])
plt.xticks(index, labels, rotation='horizontal', fontsize=4,)
plt.savefig('C:\\Users\\12103\\Documents\\Surfaces Data\\stacked_chart_wtli.pdf')

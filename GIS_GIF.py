# Import modules

import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import mapclassify as mpc
import imageio as img
from matplotlib.colors import Normalize

mpl.use('TkAgg')
plt.ioff()

# Import CSVs

countiesNE_fp = 'H:/work/coding/python/GIStraining/shapeFiles/tl_2020_31_county20.shp'

countiesNE = gpd.read_file(countiesNE_fp)
countiesNE['County'] = countiesNE['NAME20']

popGr_fp = 'H:/work/coding/python/populationGrowth/populationGrowth.csv'

popGrowth = pd.read_csv(popGr_fp, index_col=0)

std = np.std(popGrowth.iloc[1::1, 1:11:1])
std_0 = np.mean(std)

popGrowth_transitions_dic = {'County': popGrowth['County']}
popGrowth_transitions_dic['2011'] = popGrowth['2011']

slices = 35
years_t = []
years_png = ['2011.png']

for n in range(2011, 2019):
    for i in range(1, (slices+1)):
        m = str(n) + "_t" + str(i)
        popGrowth_transitions_dic[str(m)] = popGrowth[str(n)] + \
            (((popGrowth[str(n+1)] - popGrowth[str(n)]) / slices) * i)
        years_t.append(m)
        years_png.append(str(m) + ".png")


popGrowth_transitions = pd.DataFrame(
    popGrowth_transitions_dic)

# Merge population data with counties GeoDatabase

county_gDb = countiesNE.merge(popGrowth_transitions, on="County")

# Map creation

years = \
    [
        '2011', '2011_t35',  '2012_t35', '2013_t35', '2014_t35', '2015_t35', '2016_t35',
        '2017_t35', '2018_t35'
    ]

years_std = \
    [
        '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'
    ]

my_dpi = 96

cColors = []

for i in range(0, 257, 1):
    m = [(256/256), (i/256), (0/256), 1]
    cColors.append(m)

for i in reversed(range(0, 257, 1)):
    m = [(i/256), (256/256), (0/256), 1]
    cColors.append(m)

for i in reversed(range(125, 257, 1)):
    m = [(0/256), (i/256), (0/256), 1]
    cColors.append(m)

Colors = np.array(cColors)

RYG = mpl.colors.ListedColormap(Colors)

for year in years_t:
    fig, ax = plt.subplots()
    county_gDb.plot(column=year,
                    norm=Normalize(-std_0, std_0),
                    ax=ax,
                    cmap=RYG,
                    edgecolor='k',
                    legend=True,
                    legend_kwds={
                        'label': 'Annual Population Growth Rate from 2011 to 2019',
                        'orientation': 'horizontal'
                    }
                    )

    png_filepath = 'H:/work/coding/python/GIF/pngs/' + str(year) + '.png'

    plt.savefig(png_filepath,
                dpi=my_dpi*1.75)

for i in range(0, 9):
    fig, ax = plt.subplots()
    ax.set_title(years_std[i], fontsize=25)
    county_gDb.plot(column=(years[i]),
                    norm=Normalize(-std_0, std_0),
                    ax=ax,
                    cmap=RYG,
                    edgecolor='k',
                    legend=True,
                    legend_kwds={
                        'label': 'Annual Population Growth from 2011 to 2019 (%)',
                        'orientation': 'horizontal'
                    }
                    )


    png_filepath = 'H:/work/coding/python/GIF/pngs/' + str(years[i]) + '.png'

    plt.savefig(png_filepath,
                dpi=my_dpi * 1.75)

m = \
[
    2.0, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.5, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.5, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.5, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.0, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 1.5, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 1.5, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.5, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 1.5, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    .15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 2.0,
]

with img.get_writer('H:/work/coding/python/GIF/pngs/popGrowth.gif',
                    mode='I',
                    duration=m) as writer:
    for filename in years_png:
        image = img.imread('H:/work/coding/python/GIF/pngs/' + str(filename))
        writer.append_data(image)


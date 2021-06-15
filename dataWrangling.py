import numpy as np
import pandas as pd


a = \
    pd.read_csv('H:/work/coding/python/populationGrowth/countyPopulationGrowth.csv',
                index_col=0)

b = pd.concat\
        ([a.iloc[:, 0:2:1],
        pd.DataFrame
            (
            np.diff
                (
                a.iloc[0:93:1, 1:11:1],
                    axis=1
                ),
            columns=['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            )
        ],
         axis=1)

e = \
    pd.concat(
        [
            a.iloc[0:93:1, 0:1:1],
            (
                (b.iloc[:, 1:11:1] / a.iloc[:, 1:11:1])*100
            )
        ],
        axis=1
    )

populationGrowth = e.drop('2010', axis=1)

populationGrowth.to_csv('H:/work/coding/python/populationGrowth/populationGrowth.csv')

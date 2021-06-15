import census
import us
import pandas as pd

c = census.Census("dbb980e692045b1025be742842054df41c98a2c8")

dataBase_countyPops = []

for i in range(2010, 2020):
    dataBase_countyPops.append(pd.DataFrame(c.acs5.state_county(('NAME', 'B01003_001E'), us.states.NE.fips,
                                                                 census.Census.ALL, year=i)))

populations_2010 = \
    pd.DataFrame(
        (dataBase_countyPops[0].iloc[0:93:1, 0:2:1]))

populations_2010.columns = ["County", "Population"]

populations_2011 = \
    pd.DataFrame(
        (dataBase_countyPops[1].iloc
        [0:93:1, 0:2:1])
    )

populations_2011.columns = ["County", "Population"]

populations_2012 = \
    pd.DataFrame(
        dataBase_countyPops[2].iloc
        [0:93:1, 0:2:1]
    )

populations_2012.columns = ["County", "Population"]

populations_2013 = \
    pd.DataFrame(
        dataBase_countyPops[3].iloc
        [0:93:1, 0:2:1]
    )

populations_2013.columns = ["County", "Population"]

populations_2014 = \
    pd.DataFrame(
        dataBase_countyPops[4].iloc
        [0:93:1, 0:2:1]
    )

populations_2014.columns = ["County", "Population"]

populations_2015 = \
    pd.DataFrame(
        dataBase_countyPops[5].iloc
        [0:93:1, 0:2:1]
    )

populations_2015.columns = ["County", "Population"]

populations_2016 = \
    pd.DataFrame(
        dataBase_countyPops[6].iloc
        [0:93:1, 0:2:1]
    )

populations_2016.columns = ["County", "Population"]

populations_2017 = \
    pd.DataFrame(
        dataBase_countyPops[7].iloc
        [0:93:1, 0:2:1]
    )

populations_2017.columns = ["County", "Population"]

populations_2018 = \
    pd.DataFrame(
        dataBase_countyPops[8].iloc
        [0:93:1, 0:2:1]
    )

populations_2018.columns = ["County", "Population"]

populations_2019 = \
    pd.DataFrame(
        dataBase_countyPops[9].iloc
        [0:93:1, 0:2:1]
    )

populations_2019.columns = ["County", "Population"]

yearsPops = \
    [
        populations_2012,
        populations_2013,
        populations_2014,
        populations_2015,
        populations_2016,
        populations_2017,
        populations_2018,
        populations_2019
    ]

populationCounties = \
    populations_2010.merge(
        populations_2011,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2012,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2013,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2014,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2015,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2016,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2017,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2018,
        on="County")

populationCounties = \
    populationCounties.merge(
        populations_2019,
        on="County")

populationCounties.columns = ["County", 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

listCounties = \
    [
        'Adams', 'Antelope', 'Arthur', 'Banner', 'Blaine', 'Boone', 'Box Butte', 'Boyd', 'Brown', 'Buffalo',
        'Burt', 'Butler', 'Cass', 'Cedar', 'Chase', 'Cherry', 'Cheyenne', 'Clay', 'Colfax', 'Cuming', 'Custer',
        'Dakota', 'Dawes', 'Dawson', 'Deuel', 'Dixon', 'Dodge', 'Douglas', 'Dundy', 'Fillmore', 'Franklin', 'Frontier',
        'Furnas', 'Gage', 'Garden', 'Garfield', 'Gosper', 'Grant', 'Greeley', 'Hall', 'Hamilton', 'Harlan', 'Hayes',
        'Hitchcock', 'Holt', 'Hooker', 'Howard', 'Jefferson', 'Johnson', 'Kearney', 'Keith', 'Keya Paha', 'Kimball',
        'Knox', 'Lancaster', 'Lincoln', 'Logan', 'Loup', 'McPherson', 'Madison', 'Merrick', 'Morrill', 'Nance',
        'Nemaha', 'Nuckolls', 'Otoe', 'Pawnee', 'Perkins', 'Phelps', 'Pierce', 'Platte', 'Polk', 'Red Willow',
        'Richardson', 'Rock', 'Saline', 'Sarpy', 'Saunders', 'Scotts Bluff', 'Seward', 'Sheridan', 'Sherman',
        'Sioux', 'Stanton', 'Thayer', 'Thomas', 'Thurston', 'Valley', 'Washington', 'Wayne', 'Webster', 'Wheeler',
        'York'
    ]

counties = pd.Series(data=listCounties,
                     name='County')

populationCounties.update(counties)

populationCounties.to_csv('H:/work/coding/python/populationGrowth/countyPopulationGrowth.csv')

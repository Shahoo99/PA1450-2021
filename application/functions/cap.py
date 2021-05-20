import pandas as pd
from flask import render_template

def per_cap(country1, country2):

    country_list1 = []
    country_list2 = []
    population_list = []
    population_list2 = []

    df = pd.read_csv('time_series_covid19_confirmed_global.csv')
    df_1 = pd.read_csv('UID_ISO_FIPS_LookUp_Table.csv')
    which_country = country1
    which_country2 = country2

    specific_country = df.loc[df['Country/Region']== which_country]
    specific_country2 = df.loc[df['Country/Region']== which_country2]

    specific_country_values = specific_country.values
    specific_country_values2 = specific_country2.values

    country_values1 = specific_country_values.tolist()
    country_values2 = specific_country_values2.tolist()

    for x in country_values1:
        for y in x:
            country_list1.append(y)
    for x in country_values2:
        for y in x:
            country_list2.append(y)

    cases_country1 = country_list1[-1]
    cases_country2 = country_list2[-1]

    spec_country = df_1.loc[df_1['Country_Region']==which_country]
    spec_country2 = df_1.loc[df_1['Country_Region']==which_country2]

    for x in spec_country.Population:
        population_list.append(x)
    for x in spec_country2.Population:
        population_list2.append(x)

    cap_country1 = population_list[0]
    cap_country2 = population_list2[0]

    per_cap1 = cases_country1/cap_country1
    per_cap2 = cases_country2/cap_country2


    a = 'in', country1, 'the covid per capita is', str(per_cap1)
    b = 'in', country2, 'the covid per capita is', str(per_cap2)
    a_string = str(a)
    b_string = str(b)
    

    return render_template('page3.html', value1 = a_string, value2 = b_string, country1 = country1, country2 = country2)
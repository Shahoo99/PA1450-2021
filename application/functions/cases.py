import pandas as pd
from flask import render_template

def cases_in_time(country, from_date, to_date):
    df = pd.read_csv('time_series_covid19_confirmed_global.csv')
    date_list = []
    case_list = []
    plot_list_case = []
    plot_list_date = []
    final_list = []
    which_country = country
    specific_country = df.loc[df['Country/Region']== which_country]
    spec_count_value = specific_country.values
    b = spec_count_value.tolist()
    for x in b:
        for i in x:
            case_list.append(str(i))
    for y in specific_country:
        date_list.append(str(y))
    final_date_list = date_list[4 : ]
    final_case_list = case_list[4 : ]
    choice_from_date = from_date
    choice_to_date = to_date
    choice_from_date = choice_from_date.replace('.', '/')
    choice_to_date = choice_to_date.replace('.', '/')
    from_index = final_date_list.index(choice_from_date)
    to_index = final_date_list.index(choice_to_date)

    for x in range(from_index, to_index +1):
        a = final_date_list[x]
        plot_list_date.append(a)

    for x in range(from_index, to_index +1):
        a = final_case_list[x]
        plot_list_case.append(a)
    
    for x in range(len(plot_list_case)-1):
        final_list.append('at' + ' ' + plot_list_date[x] + ' ' + 'there were' + ' ' + plot_list_case[x] + ' ' + 'cases')
    
    return render_template('page2.html', content = final_list, first = from_date, second = to_date)



# def cases_in_time():
#     df = pd.read_csv('time_series_covid19_confirmed_global.csv')
#     date_list = []
#     case_list = []
#     date_death_list = []
#     specific_country = df.loc[df['Country/Region']== 'China']
#     spec_count_value = specific_country.values
#     b = spec_count_value.tolist()
#     for x in b:
#         for i in x:
#             case_list.append(i)
#     for y in specific_country:
#         date_list.append(y)
#     final_date_list = date_list[4 : ]
#     final_case_list = case_list[4 : ]
#     from_index = final_date_list.index('1/1/21')
#     to_index = final_date_list.index('1/15/21')
#     new_cases_in_period = final_case_list[to_index] - final_case_list[from_index]
#     for h in range(from_index +1, to_index):
#         a = 'At', final_date_list[h], 'total amount of cases was', final_case_list[h]
#         date_death_list.append(a)
#     return str(date_death_list)
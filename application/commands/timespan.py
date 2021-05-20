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

# def create_parser(subparsers):
#     """"""
#     parser = subparsers.add_parser("cases_in_time")
#     parser.set_defaults(command=cases_in_time)
#     # Add a required parameter to specify the user to greet
#     parser.add_argument("-cases_in_time", required=True, help="n/a")
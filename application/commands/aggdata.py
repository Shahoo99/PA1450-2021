# def aggregated_data():
#     args = request.args
#     df = pd.read_csv('time_series_covid19_deaths_global.csv')
#     death_list = []
#     province_list = []
#     country_list = []
#     final_list = []
#     infile = open('time_series_covid19_deaths_global.csv')
#     reader = csv.reader(infile)
#     for row in reader:
#         death_list.append(row[-1])
#         final_death_list = death_list[1 : ]
#     for x in df['Country/Region']:
#         country_list.append(x)
#     for y in df['Province/State']:
#         province_list.append(y)
#     for i in range(len(death_list)-1):
#         a = 'In', country_list[i], province_list[i], final_death_list[i], 'have died',
#         final_list.append(str(a))
#     return ("\n".join(final_list))

# def create_parser(subparsers):
#     """"""
#     parser = subparsers.add_parser("aggregated_data")
#     parser.set_defaults(command=aggregated_data)
#     # Add a required parameter to specify the user to greet
#     parser.add_argument("-showdata", required=True, help="n/a")

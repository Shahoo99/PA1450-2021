
from flask import Flask, send_file, render_template, request, Blueprint
import pandas as pd
from flask.helpers import url_for
import csv
import matplotlib.pyplot as plt

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__, static_folder="../static")
    posts = Blueprint("posts", __name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")   

    @app.route("/showdata")
    def aggregated_data():
        df = pd.read_csv('time_series_covid19_deaths_global.csv')
        death_list = []
        province_list = []
        country_list = []
        final_list = []
        infile = open('time_series_covid19_deaths_global.csv')
        reader = csv.reader(infile)
        for row in reader:
            death_list.append(row[-1])
            final_death_list = death_list[1 : ]
        for x in df['Country/Region']:
            country_list.append(x)
        for y in df['Province/State']:
            province_list.append(y)
        for i in range(len(death_list)-1):
            a = 'In', country_list[i], province_list[i], final_death_list[i], 'have died',
            final_list.append(str(a))
        return ("\n".join(final_list))

    @app.route("/cases_in_timespan")
    def cases_in_time():
        df = pd.read_csv('time_series_covid19_confirmed_global.csv')
        date_list = []
        case_list = []
        date_death_list = []
        specific_country = df.loc[df['Country/Region']== 'China']
        spec_count_value = specific_country.values
        b = spec_count_value.tolist()
        for x in b:
            for i in x:
                case_list.append(i)
        for y in specific_country:
            date_list.append(y)
        final_date_list = date_list[4 : ]
        final_case_list = case_list[4 : ]
        from_index = final_date_list.index('1/1/21')
        to_index = final_date_list.index('1/15/21')
        new_cases_in_period = final_case_list[to_index] - final_case_list[from_index]
        for h in range(from_index +1, to_index):
            a = 'At', final_date_list[h], 'total amount of cases was', final_case_list[h]
            date_death_list.append(a)
        return str(date_death_list)

    @app.route("/", methods=['GET', 'POST'])
    def query():
        q = request.form.get("q")
        if q == "show data": 
            return aggregated_data()
        elif q == "cases in timespan":
            return cases_in_time()
        else:
            return send_file("../www/index.html")

    @app.route("/showdata")
    def aggregated_data():
        df = pd.read_csv('time_series_covid19_deaths_global.csv')
        death_list = []
        province_list = []
        country_list = []
        final_list = []
        infile = open('time_series_covid19_deaths_global.csv')
        reader = csv.reader(infile)
        for row in reader:
            death_list.append(row[-1])
            final_death_list = death_list[1 : ]
        for x in df['Country/Region']:
            country_list.append(x)
        for y in df['Province/State']:
            province_list.append(y)
        for i in range(len(death_list)-1):
            a = 'In', country_list[i], province_list[i], final_death_list[i], 'have died',
            final_list.append(str(a))
        return render_template('page.html', content = final_list)




    @app.route('/timespan/<country>/<from_date>/<to_date>')
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


    @app.route('/compare/<country1>/<country2>')
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

    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
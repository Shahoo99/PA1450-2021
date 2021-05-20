
#from flask_mysqldb import MySQL
from flask import Flask, send_file, render_template, request, Blueprint
import pandas as pd
import csv
#import aggdata problem med import
#import timespan

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__, static_folder="../static")
    posts = Blueprint("posts", __name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")
    
    @posts.route("/", methods=["POST", "GET"])
    def posts_list():
        q = request.args.get("q")

        if q:
            posts = Post.query.filter(Post.title.contains(q) | 
            Post.body.cointains(q))
        else:
            posts = Post.query.all()
        return render_template("/www/index.html", posts=posts)    

    # @app.route("/showdata")
    # def agg_data():
    #     return aggdata.aggregated_data()

    # @app.route("/cases_in_timespan")
    # def cases_timespan():
    #     return timespan.cases_in_time()

    # @app.route("/greeting/<name>")
    # def greeting(name):
    #     """Return a greeting for the user."""
    #     return "Hello, {}!".format(name)

    @app.route("/showdata", methods=["GET"])
    def aggregated_data():
        args = request.args
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

    #@app.route("/livesearch", methods=["POST", "GET"])
    #def livesearch():
    #    searchbox = request.form.get("text")
    
    #@app.route("//")
    #def shahoo():
    #    return send_file("../www/shahoo.html")

    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
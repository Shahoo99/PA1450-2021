
from flask import Flask, send_file, render_template, request
from application.functions import aggdata, cases, cap, plot


def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__, static_folder="../static")

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")   

    @app.route("/plot")
    def plot_graph():
        return plot.plot_graph()
    
    @app.route("/showdata")
    def aggregated_data():
        return aggdata.aggregated_data()

    @app.route("/timespan/<country>/<from_date>/<to_date>")
    def cases_in_time(country, from_date, to_date):
        return cases.cases_in_time(country, from_date, to_date)

    @app.route("/compare/<country1>/<country2>")
    def per_cap(country1, country2):
        return cap.per_cap(country1, country2)

    # @app.route("/", methods=['GET', 'POST'])
    # def query_header():
    #     q = request.form.get("q")
    #     if q == "View aggregated data": 
    #         return aggregated_data()
    #     elif q == "Compare cases per capita between two countries":
    #         return send_file("templates/page4.html")    
    #     elif q == "View cases in timespan":
    #         return send_file("templates/page5.html")                
    #     else:
    #         return send_file("../www/index.html")

    @app.route("/commands/templates/page4.html", methods=['GET', 'POST'])
    def query_form1():
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        if q1 and q2 != 0:
            return per_cap(q1, q2)
        else:
            return send_file("templates/page4.html")

    @app.route("/commands/templates/page4.html")
    def page4():
        return send_file("templates/page4.html")

    @app.route("/commands/templates/page5.html", methods=['GET', 'POST'])
    def query_form2():
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        if q1 and q2 and q3 != 0:
            return cases_in_time(q1, q2, q3)
        else:
            return send_file("templates/page5.html")

    @app.route("/commands/templates/page5.html")
    def page5():
        return send_file("templates/page5.html")
        
    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
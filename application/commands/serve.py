
from flask import Flask, send_file, render_template, request, Blueprint
from flask.helpers import url_for
import pandas as pd
import csv
from application.functions import aggdata, cases


def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__, static_folder="../static")

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")   

    @app.route("/showdata")
    def aggregated_data():
        return aggdata.aggregated_data()

    @app.route("/cases_in_timespan")
    def cases_in_time():
        return cases.cases_in_time()

    @app.route("/", methods=['GET', 'POST'])
    def query():
        q = request.form.get("q")
        if q == "show data": 
            return aggregated_data()
        elif q == "cases in timespan":
            return cases_in_time()
        else:
            return send_file("../www/index.html")

    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
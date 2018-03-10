from flask import Flask, render_template, request
from source.classes.CarDatabase import CarDatabase
from source.algorithms import *
import time

# The flask app
app = Flask(__name__)

# The path to the CSV file comtaining the data
CSV_PATH = "data/nsfmw2/cars_short.csv"

# Reverses all sort algorithms
db_reversed = False

# The whole DB
car_database = CarDatabase(CSV_PATH)


def process_get():
    # The default values
    sort_checkbox = False, False, False
    sort_agregate = "sum"
    sort_algorithm = "naive"
    agregate_func = agregate_sum_func
    sort_quantity = 3

    # Obtain the GET parameters
    if request.method == "GET":
        # Values of checkboxes
        sort_checkbox = request.args.getlist('sort')
        # The sorting function
        sort_agregate = request.args.get('agregate')
        # The algorithm to get the top-k
        sort_algorithm = request.args.get('alorithm')
        # The treshold quantity
        sort_quantity = request.args.get('quantity', type=int)

    # Process the obtained parameters
    checkbox_dict = {'accel': "accel" in sort_checkbox,
                     'speed': "speed" in sort_checkbox,
                     'handl': "handl" in sort_checkbox}
    if sort_agregate == "sum":
        agregate_func = agregate_sum_func
    elif sort_agregate == "max":
        agregate_func = agregate_max_func

    return checkbox_dict, sort_agregate, sort_algorithm, agregate_func, sort_quantity


########################################################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    # Get the processed GET parameters and settings
    checkbox_dict, sort_agregate, sort_algorithm, agregate_func, sort_quantity = process_get()

    # Return the correct database and template
    if sort_algorithm == "treshold":
        start = time.time()
        db = car_database.top_k_treshold(checkbox_dict, agregate_func, sort_quantity)
        q_time = time.time() - start
        # Render the website
        return render_template("index.html", title='Index - treshold top-k',
                               database=db, checkdict=checkbox_dict, algorithm=sort_algorithm, agregate=sort_agregate,
                               quantity=sort_quantity, querytime=q_time)
    else:  # elif sort_algorithm == "naive":
        start = time.time()
        db = car_database.naive_k(checkbox_dict, agregate_func, sort_quantity)
        q_time = time.time() - start
        # Render the website
        return render_template("index.html", title='Index - treshold naive-k',
                               database=db, checkdict=checkbox_dict, algorithm=sort_algorithm, agregate=sort_agregate,
                               quantity=sort_quantity, querytime=q_time)


########################################################################################################################
@app.route('/about')
def about():
    return render_template("about.html", title='About')


########################################################################################################################
@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

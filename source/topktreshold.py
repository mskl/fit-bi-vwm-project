from flask import Flask, render_template, request
from source.classes.CarDatabase import CarDatabase
from source.algorithms import *
import time

# The flask app
app = Flask(__name__)

# The path to the CSV file comtaining the data
csv_path = "data/nsfmw2/cars_short.csv"

# Reverses all sort algorithms
db_reversed = False

# The whole DB
car_database = CarDatabase(csv_path)


@app.route('/', methods=['GET', 'POST'])
def index():
    sort_checkbox = False, False, False
    sort_agregate = "sum"
    sort_algorithm = "naive"
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
    a, s, h = ash_from_post_list(sort_checkbox)
    checkbox_dict = {'accel':a, 'speed':s, 'handl':h}
    agregate_func = agregate_sum_func
    if sort_agregate == "sum":
        agregate_func = agregate_sum_func
    elif sort_agregate == "max":
        agregate_func = agregate_max_func

    # Return the correct database and webpage
    if sort_algorithm == "treshold":
        start = time.time()
        db = car_database.top_k_treshold(a, s, h, agregate_func, sort_quantity)
        q_time = time.time() - start
        return render_template("index.html", title='Index - treshold top-k', database=db,
                               checkdict=checkbox_dict, algorithm=sort_algorithm, agregate=sort_agregate,
                               quantity=sort_quantity, querytime=q_time)
    else: # sort_algorithm == "naive":
        start = time.time()
        db = car_database.naive_k(a, s, h, agregate_func, sort_quantity)
        q_time = time.time() - start
        return render_template("index.html", title='Index - treshold naive-k', database=db,
                               checkdict=checkbox_dict, algorithm=sort_algorithm, agregate=sort_agregate,
                               quantity=sort_quantity, querytime=q_time)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

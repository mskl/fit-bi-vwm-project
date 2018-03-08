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
    sort_quantity = 3
    if request.method == "GET":
        # Values of checkboxes
        sort_checkbox = request.args.getlist('sort')
        # The sorting function
        sort_agregate = request.args.get('agregate')
        # The treshold quantity
        sort_quantity = request.args.get('quantity', type=int)

    a, s, h = ash_from_post_list(sort_checkbox)
    checkbox_dict = {'accel':a, 'speed':s, 'handl':h}

    if sort_agregate == "sum":
        start = time.time()
        db = car_database.naive_rank_sort(a, s, h, agregate_sum_func)
        qtime = time.time()-start
        return render_template("index.html",
                               title='Index - naive sum',
                               database=db,
                               checkdict=checkbox_dict,
                               agregate=sort_agregate,
                               quantity=sort_quantity,
                               querytime=qtime)
    elif sort_agregate == "max":
        start = time.time()
        db = car_database.naive_rank_sort(a, s, h, agregate_max_func)
        qtime = time.time() - start
        return render_template("index.html",
                               title='Index - max',
                               database=db,
                               checkdict=checkbox_dict,
                               agregate=sort_agregate,
                               quantity=sort_quantity,
                               querytime=qtime)
    elif sort_agregate == "naivek":
        start = time.time()
        db = car_database.naive_k(a, s, h, agregate_sum_func, sort_quantity)
        qtime = time.time() - start
        return render_template("index.html",
                               title='Index - naive k',
                               database=db,
                               checkdict=checkbox_dict,
                               agregate=sort_agregate,
                               quantity=sort_quantity,
                               querytime=qtime)
    else:
        start = time.time()
        db = car_database.get_names()
        qtime = time.time() - start
        return render_template("index.html",
                               title='Index - name',
                               database=db,
                               checkdict=checkbox_dict,
                               quantity=sort_quantity,
                               querytime=qtime)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

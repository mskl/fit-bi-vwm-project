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
    if request.method == "GET":
        sort_checkbox = request.args.getlist('sort')
        sort_agregate = request.args.get('agregate')

    a, s, h = ash_from_post_list(sort_checkbox)
    checkdict = {'accel':a, 'speed':s, 'handl':h}

    #if sort_agregate == "sum":
    #    db = car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_sum)
    #    return render_template("index.html",
    #                           title='Index - naive sum',
    #                           database=db,
    #                           checkdict=checkdict,
    #                           agregate=sort_agregate)
    #elif sort_agregate == "max":
    #    db = car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_max)
    #    return render_template("index.html",
    #                           title='Index - naive max',
    #                           database=db,
    #                           checkdict=checkdict,
    #                           agregate=sort_agregate)

    return render_template("index.html",
                           title='Index - by name',
                           database=car_database.get_names(),
                           checkdict=checkdict)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

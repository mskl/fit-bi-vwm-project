from flask import Flask, render_template, request
from topktresholdapp.classes.CarDatabase import CarDatabase
from topktresholdapp.algorithms import *

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
    sortdict = {'accel':a, 'speed':s, 'handl':h}


    if sort_agregate == "sum":
        return render_template("index.html", title='Index',
                               database=car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_sum),
                               checkdict=sortdict, agregate=sort_agregate)
    elif sort_agregate == "max":
        return render_template("index.html", title='Index',
                               database=car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_max),
                               checkdict=sortdict, agregate=sort_agregate)

    return render_template("index.html", title='Index',
                           database=car_database.get_names(),checkdict=sortdict, )


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

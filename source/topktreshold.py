from flask import Flask, render_template
from source.classes.CarDatabase import CarDatabase
from source.algorithms import *

# The flask app
app = Flask(__name__)

# The path to the CSV file comtaining the data
CSV_PATH = "data/nsfmw2/cars_short.csv"

# Reverses all sort algorithms
db_reversed = False

# The whole DB
car_database = CarDatabase(CSV_PATH)


########################################################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    # dict         string         string          function       int             Process GET parameters
    checkbox_dict, sort_agregate, sort_algorithm, agregate_func, sort_quantity = process_get_parameters()

    # Return the correct database and template
    if sort_algorithm == "treshold":
        db, q_time = car_database.top_k_treshold(checkbox_dict, agregate_func, sort_quantity)
        return render_template("index.html", title='Index - treshold top-k',
                               database=db, checkdict=checkbox_dict, algorithm=sort_algorithm, agregate=sort_agregate,
                               quantity=sort_quantity, querytime=q_time)
    else:
        db, q_time = car_database.top_k_naive(checkbox_dict, agregate_func, sort_quantity)
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


########################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)

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
@app.route('/', methods=['GET'])
def index():
    # Obtain the settings from the form
    form_data = get_form_data()

    # Process the agregate function from the get
    if form_data['agregate'] == "sum":
        agregate_func = agregate_sum_func
    else:
        agregate_func = agregate_max_func

    # Return the correct database and template
    if form_data['algorithm'] == "treshold":
        db, q_time = car_database.top_k_treshold(form_data, agregate_func)
        return render_template("index.html", title='Index - treshold top-k',
                               database=db, form_data=form_data, querytime=q_time)
    else:
        db, q_time = car_database.top_k_naive(form_data, agregate_func)
        return render_template("index.html", title='Index - treshold naive-k',
                               database=db, form_data=form_data, querytime=q_time)


########################################################################################################################
@app.route('/about')
def about():
    return render_template("about.html", title='About')


########################################################################################################################
@app.route('/settings', methods=['GET'])
def settings():
    payload = ""
    dataset_get = request.args.get('dataset');

    form_data = {
        'dataset': dataset_get or "NFS",
    }

    if dataset_get is not None:
        payload = "Setting the dataset to %s" %dataset_get

    return render_template("settings.html", payload=payload, form_data=form_data,  title='Settings')


########################################################################################################################
@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


########################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)

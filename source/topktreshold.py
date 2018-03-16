from flask import Flask, render_template
from source.classes.CarDatabase import CarDatabase
from source.algorithms import *

# Paths to the DATASET csv files
dataset_paths = {"NFS": "source/data/cars_nsf.csv",
                 "random": "source/data/cars_random.csv",
                 "wordlist": "source/data/czech_wordlist_randoms.csv"}
current_dataset = "NFS"

# The flask application
app = Flask(__name__)
car_database = CarDatabase(dataset_paths["NFS"])


@app.route('/', methods=['GET'])
def index():
    # Obtain the pointer to an agregate function based on the GET/POST
    agregate_func = get_agregate_function(request.values)

    # Return the correct database and template
    if request.values.get('algorithm') == "treshold":
        db, q_time = car_database.top_k_treshold(request.values, agregate_func)
        return render_template("index.html", title='Index - treshold top-k',
                               database=db, querytime=q_time)
    else:
        db, q_time = car_database.top_k_naive(request.values, agregate_func)
        return render_template("index.html", title='Index - treshold naive-k',
                               database=db, querytime=q_time)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.route('/settings', methods=['GET'])
def settings():
    global current_dataset
    payload = "Current datset is %s. Which dataset would you like to select?" % current_dataset
    new_dataset = request.args.get('dataset')

    if new_dataset is not None:
        current_dataset = new_dataset
        car_database.set_database(dataset_paths[new_dataset])
        payload = "Setting the dataset to %s" % new_dataset

    return render_template("settings.html", payload=payload, dataset=new_dataset,  title='Settings')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from source.classes.CarDatabase import CarDatabase
from source.algorithms import *


dataset_paths = { "NFS": "data/cars_nfs.csv",
                  "random": "data/cars_random.csv"}

app = Flask(__name__)
car_database = CarDatabase(dataset_paths["NFS"])


@app.route('/', methods=['GET'])
def index():
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
    payload = ""
    dataset_get = request.args.get('dataset') or "NFS"

    if dataset_get is not None:
        car_database = CarDatabase(dataset_paths[dataset_get])
        payload = "Setting the dataset to %s" % dataset_get

    return render_template("settings.html", payload=payload, dataset=dataset_get,  title='Settings')


@app.errorhandler(404)
def error(e):
    return render_template("error.html", title='404'), 404


########################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)

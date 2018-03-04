from enum import Enum
from flask import Flask, render_template, request
from car_database import CarDatabase
import operator

# The flask app
app = Flask(__name__)

# The path to the CSV file comtaining the data
csv_path = "data/nsfmw2/cars_short.csv"

db_reversed = False

# The whole DB
car_database = CarDatabase(csv_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    sort_parameter = ""
    if request.method == "GET":
        sort_parameter = request.args.get('sortby')

    # cars_db = car_database.all_cars

    # if sort_parameter == "name":
    #     cars_db.sort(key=operator.itemgetter('name'), reverse=False)
    #if sort_parameter == "acceleration":
    #    return render_template("index.html", title='Index', database=car_database.get_accel())
    #elif sort_parameter == "speed":
    #    return render_template("index.html", title='Index', database=car_database.get_speed())
    #elif sort_parameter == "handling":
    #    return render_template("index.html", title='Index', database=car_database.get_handl())
    #    # cars_db.sort(key=operator.itemgetter('handling'), reverse=True)

    return render_template("index.html", title='Index', database=car_database.get_accel())


# @app.route('/about')
# def about():
#     return render_template("about.html", title='About')


# @app.route('/param', methods=['GET'])
# def param():
#     sort_parameter = ""
#     if request.method == "GET":
#         sort_parameter = request.args.get('single')
#
#     if sort_parameter == "accel":
#         return render_template("param.html", title='Acceleration', data=car_database.get_accel())
#     elif sort_parameter == "speed":
#         return render_template("param.html", title='Speed', data=car_database.get_speed())
#     elif sort_parameter == "handl":
#         return render_template("param.html", title='Handling', data=car_database.get_handl())



if __name__ == '__main__':
    app.run(debug=True)

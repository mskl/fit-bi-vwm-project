from flask import Flask, render_template, request
from parse_cars import parse_csv, parse_csv_classes
from pprint import pprint
import operator
app = Flask(__name__)

# The database containing the info about the cars
database = []
db_reversed = False

def check_reversed(inparam):
    if inparam == "true":
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    sort_parameter = ""
    db_reversed_in = "False"
    if request.method == "GET":
        sort_parameter = request.args.get('sortby')
        db_reversed_in = request.args.get('reverse')

    db_reserved = check_reversed(db_reversed_in)
    print(db_reversed)
    cars_db = parse_csv()

    if sort_parameter == "name":
        cars_db.sort(key=operator.itemgetter('name'), reverse=db_reversed)
    elif sort_parameter == "acceleration":
        cars_db.sort(key=operator.itemgetter('acceleration'), reverse=(not db_reversed))
    elif sort_parameter == "speed":
        cars_db.sort(key=operator.itemgetter('speed'), reverse=(not db_reversed))
    elif sort_parameter == "handling":
        cars_db.sort(key=operator.itemgetter('handling'), reverse=(not db_reversed))

    return render_template("index.html", title='Index', database=cars_db)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.route('/param', methods=['GET'])
def param():
    sort_parameter = ""
    cars, cars_accel, cars_speed, cars_handl = parse_csv_classes()

    if request.method == "GET":
        sort_parameter = request.args.get('p')

    if sort_parameter == "acceleration":
        return render_template("param.html", title='Acceleration', data=cars_accel)
    elif sort_parameter == "speed":
        return render_template("param.html", title='Speed', data=cars_speed)
    elif sort_parameter == "handling":
        return render_template("param.html", title='Handling', data=cars_handl)


if __name__ == '__main__':
    database = parse_csv()
    app.run(debug=True)

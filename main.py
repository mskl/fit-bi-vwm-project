from flask import Flask, render_template, request
from parse_cars import parse_csv
from pprint import pprint
import operator
app = Flask(__name__)

# The database containing the info about the cars
database = []

@app.route('/', methods=['GET', 'POST'])
def index():
    sort_parameter = ""
    if request.method == "GET":
        sort_parameter = request.args.get('sortby')

    database = parse_csv()

    if sort_parameter == "name":
        database.sort(key=operator.itemgetter('name'), reverse=False)
    elif sort_parameter == "acceleration":
        database.sort(key=operator.itemgetter('acceleration'), reverse=True)
    elif sort_parameter == "speed":
        database.sort(key=operator.itemgetter('speed'), reverse=True)
    elif sort_parameter == "handling":
        database.sort(key=operator.itemgetter('handling'), reverse=True)

    return render_template("index.html", title='Index', database=database)

@app.route('/about')
def about():
    return render_template("about.html", title='About')


if __name__ == '__main__':
    database = parse_csv()
    app.run(debug=True)

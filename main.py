from flask import Flask, render_template, request
from parse_cars import parse_csv
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    content = ""
    if request.method == "GET":
        content = request.args.get('search')

    if content is None:
        content = ""

    cars_dict = parse_csv()
    print(cars_dict)

    return render_template("index.html", title='Home', content=content, dictionary=cars_dict, count=len(cars_dict['name']))


if __name__ == '__main__':
    app.run(debug=True)

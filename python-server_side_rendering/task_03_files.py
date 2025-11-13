from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data['items']

    print("Items récupérés:", items_list)
    return render_template('items.html', items=items_list)


@app.route('/source')
def product_list():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    if source == 'json':
        product_list = read_json('product_json')

    else:
        product_list = read_csv('product_csv')

    if product_id:
        product_id = int(product_id)
        product_list = [p for p in product_list if p['id'] == product_id]
        if not product_list:
            return render_template(
                'product_display.html', error="Product not found"
                )
    return render_template('product_display.html', products=product_list)


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_csv(filename):
    product_list = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            product_list.append(row)
    return product_list


if __name__ == '__main__':
    app.run(debug=True, port=5000)

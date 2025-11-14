from flask import Flask, request, render_template
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


def read_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv(filename):
    try:
        product_list = []
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                product_list.append(row)
        return product_list
    except FileNotFoundError:
        return None
    except ValueError:
        return None


@app.route('/products')
def product_list():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    if source == 'json':
        products = read_json('products.json')

    else:
        products = read_csv('products.csv')

    if products is None:
        return render_template(
            'product_display.html', error="Error reading file"
            )

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                return render_template(
                    'product_display.html', error="Product not found"
                    )
        except ValueError:
            return render_template('product_display.html', error="Invalid ID")
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

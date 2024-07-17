from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def read_csv(file_path):
    data = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data


def read_sqlite():
    data = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        data = []
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except Exception as e:
            error = "Error reading JSON file."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception as e:
            error = "Error reading CSV file."
    elif source == 'sql':
        try:
            products = read_sqlite()
        except Exception as e:
            error = "Error reading database."
    else:
        error = "Wrong source"

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products
                        if product['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid product ID"

    return render_template('product_display.html',
                           products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

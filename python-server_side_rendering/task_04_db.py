from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

def read_sqlite_database():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_database()
        if products is None:
            error = "Database error"
    else:
        error = "Wrong source"
    
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"
    
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

FASTAPI_BASE_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    response = requests.get(f"{FASTAPI_BASE_URL}/products")
    products = []
    if response.status_code == 200:
        products = response.json()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        data = {"name": name, "price": price, "quantity": quantity}
        response = requests.post(f"{FASTAPI_BASE_URL}/products", json=data)
        if response.status_code == 200:
            return redirect(url_for('index'))
        else:
            # Handle error, e.g., display a message
            return f"Error: {response.status_code} {response.text}"
    return render_template('add_product.html')

@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        data = {"name": name, "price": price, "quantity": quantity}
        response = requests.put(f"{FASTAPI_BASE_URL}/products/{product_id}", json=data)
        if response.status_code == 200:
            return redirect(url_for('index'))
        else:
            return f"Error: {response.status_code} {response.text}"
    
    response = requests.get(f"{FASTAPI_BASE_URL}/products/{product_id}")
    product = None
    if response.status_code == 200:
        product = response.json()
    else:
        return f"Error: {response.status_code} {response.text}"

    if product is None:
        return "Product not found", 404
    return render_template('edit_product.html', product=product)

@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    response = requests.delete(f"{FASTAPI_BASE_URL}/products/{product_id}")
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return f"Error: {response.status_code} {response.text}"

if __name__ == '__main__':
    app.run(debug=True) 
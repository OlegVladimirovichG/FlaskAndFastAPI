from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница категории товаров
@app.route('/category/<category_name>')
def category(category_name):
    return render_template('category.html', category_name=category_name)

# Страница категории товаров
@app.route('/contacts/<map_name>')
def contacts(map_name):
    return render_template('contacts.html', map_name=map_name)

# Страница отдельного товара
@app.route('/product/<product_name>')
def product(product_name):
    return render_template('product.html', product_name=product_name)

if __name__ == '__main__':
    app.run(debug=True)

from app import app, render_template
import requests


@app.get('/')
@app.get('/home')
def home():
    res = requests.get('https://fakestoreapi.com/products')
    data = res.json()
    products = data
    return render_template('front/home.html', products=products)

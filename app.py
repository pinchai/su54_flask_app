from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def hello_world():
    product = [
        {
            'id': 1,
            'name': 'Product 1',
            'price': 10.0,
            'in_stock': True
        }
    ]
    return render_template('index.html')
    # return product
    # return '<h1 style="color: red">Hello su54 123123!</h1>'


if __name__ == '__main__':
    app.run()

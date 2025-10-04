from app import app, render_template
from flask import request


@app.get('/detail')
def detail():
    product_name = request.args.get('name', '*')
    return render_template('front/detail.html', module='detail')

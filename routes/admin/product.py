from app import app, render_template
from flask import request, redirect, abort


@app.get('/admin/product')
def product():
    module = 'product'
    return render_template('admin/product/index.html', module=module)


@app.get('/admin/product/form')
def add_product():
    module = 'product'
    action = request.args.get('action', 'add')
    if action not in ['add', 'edit']:
       return abort(404)
    pro_id = request.args.get('pro_id', 0)
    status = 'add' if action == 'add' else 'edit'

    return render_template(
        'admin/product/form.html',
        module=module,
        status=status,
        pro_id=pro_id,
    )


@app.get('/admin/product/confirm')
def confirm_product():
    module = 'product'
    return render_template('admin/product/confirm.html', module=module)



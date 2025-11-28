from app import app, render_template
from flask import request


@app.get('/contact')
def contact():
    return render_template('front/contact.html')


@app.post('/contact/submit')
def contact_submit():
    form = request.form
    name = form.get('name')
    phone = form.get('phone')
    email = form.get('email')
    subject = form.get('subject')
    message = form.get('message')
    assert False, f"{name}, {phone}, {email}, {subject}, {message}"
    # Handle form submission logic here

    return "Form submitted!"

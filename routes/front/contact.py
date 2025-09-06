from app import app, render_template


@app.get('/contact')
def contact():
    return render_template('contact.html')

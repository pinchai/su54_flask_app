from app import app, render_template


@app.get('/admin')
def admin():
    return render_template('admin/starter.html')

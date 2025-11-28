from app import app, render_template


@app.get('/summernote')
def summernote():
    return render_template('admin/summernote.html')

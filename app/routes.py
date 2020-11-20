from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Isaac'}
    posts = [
        {
            'author': {'username': 'Some User'},
            'body': 'This is a post of some description'
        },
        {
            'author': {'username': 'Another User'},
            'body': 'I have thoughts I think people care about!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

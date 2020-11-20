from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Isaac'}
    return '''
<html>
    <head>
        <title>Home Page - Test Flask Application</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

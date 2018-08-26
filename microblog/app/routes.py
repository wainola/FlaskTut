from app import app

@app.route('/')
@app.route('/index')

# VIEW FUNCTION 
def index():
    return 'Hello World!'
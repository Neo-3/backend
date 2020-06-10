from api import app, jsonify

@app.route("/")
def index(): 
    return jsonify({'data': "Hello from forms!"})

from api import app, jsonify
from api.models import Teste

@app.route("/")
def index():
    teste = Teste.objects()
    return teste.to_json()

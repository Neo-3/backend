from api import app, jsonify, request
from api.models import Teste


@app.route("/api/v1.0/test")
def index():
    teste = Teste.objects()
    return teste.to_json()


@app.route("/api/v1.0/register/test", methods=["POST"])
def testPost():
    body = request.get_json()

    teste = Teste(name=body.get("name"), some_value=body.get("someValue"))

    try:
        teste.save()
        return teste.to_json()
    except Exception as error:
        return jsonify({'Error': str(error)})

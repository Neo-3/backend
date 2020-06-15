from api import app, jsonify, request
from api.models import Teste


@app.route("/api/v1.0/test")
def index():
    teste = Teste.objects()
    return teste.to_json()


@app.route("/api/v1.0/register/test", methods=["POST"])
def testPost():
    body = request.get_json()
    print(body.get("name"))

    teste = Teste(name=body.get("name"))

    try:
        teste.save()
        return jsonify({'data': teste.name})
    except Exception as error:
        return jsonify({'Error': str(error)})

from api import app, jsonify, request
from api.models import Teste

@app.route("/")
def index():
    teste = Teste.objects()
    return teste.to_json()


@app.route("/register/", methods=["POST"])
def testPost():
    body = request.get_json()
    print(body.get("name"))

    test = Teste(teste=body.get("name"))
    try:
        test.save()
        return jsonify({'data': test.teste})
    except Exception as error:
        return jsonify({'Error': error})

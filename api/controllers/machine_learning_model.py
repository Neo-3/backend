from api import app, jsonify, request
from api.models import Model
import datetime


@app.route("/api/v1.0/update/model", methods=["POST"])
def update_Model():
    model = Model(name=request.form.get("name"), created_at=int(datetime.datetime.now(
    ).timestamp()), model_file=request.files.get("model_file"))

    try:
        model.save()
        return model.to_json()
    except Exception as error:
        return jsonify({'Error': str(error)})


@app.route("/api/v1.0/model", methods=["GET"])
def get_model():
    response = Model.objects.order_by('-created_at')[0]
    model_dict = {}

    print("response: ", response.to_mongo().to_dict())
    for key, item in response.to_mongo().to_dict().items():
        model_dict[key] = str(item)

    print("AAAAAAAAAAAAAAA:", model_dict)
    return jsonify({'teste': model_dict})

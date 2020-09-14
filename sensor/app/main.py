from flask import Flask, render_template, jsonify, request
from temp_sensor import get_raw_temp

app = Flask(__name__, template_folder=".")

centigrade_scale = {"base": 0, "scale_factor": 1, "offset": 0}
kelvin_scale = {"base": 273, "scale_factor": 1, "offset": 0}
fahrenheit_scale = {"base": 32, "scale_factor": 0.556, "offset": 0}
config = centigrade_scale


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/sensor/", methods=["GET"])
def read():
    reading = (
        config["base"] + (get_raw_temp() - config["offset"]) / config["scale_factor"]
    )
    return jsonify({"temperature": reading})


@app.route("/sensor/config", methods=["GET"])
def get_config():
    return jsonify(config)


@app.route("/sensor/config", methods=["PUT"])
def update_config():
    mods = {}
    print("Recd: ", request.json)
    for param in ["base", "scale_factor", "offset"]:
        if param in request.json:
            mods[param] = request.json[param]
    config.update(mods)  # TODO: if mods not empty ?
    return jsonify(config), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # For debugging locally.

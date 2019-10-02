from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
# list available routes
    return "/api/v1.0/precipatation, /api/v1.0/stations, /api/v1.0/tobs, /api/v1.0/<start>, /api/v1.0/<start>/<end>"

@app.route("/api/v1.0/precipatation")
    return "stations"

@app.route("/api/v1.0/stations")
def stations():
    return "stations"

@app.route("/api/v1.0/tobs")
def tobs():
    return "tobs"

@app.route("/api/v1.0/<start>")
def start():
    return "start"

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return "start_end"

if __name__ == "__main__":
    app.run(debug=True)

# From cdQa, modified for testing
from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import pickle

from cdqa.pipeline import QAPipeline

cdqa_pipeline = pickle.load(open('gamekit_model.sav', 'rb'))

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["GET"])
def api():

    query = request.args.get("query")
    prediction = cdqa_pipeline.predict(query=query)

    return jsonify(
        query=query, answer=prediction[0], title=prediction[1], paragraph=prediction[2]
    )
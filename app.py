from flask import Flask, jsonify, request
import pandas as pd
from pandas_profiling import ProfileReport
import json



app = Flask(__name__)


@app.route('/profiling', methods=["POST"])
def index():
    if request.method == 'POST':
        req = request.json
        data = req["data"]
        data = pd.DataFrame.from_dict(json.loads(data))
        file_name = req["file_name"]
        profile = ProfileReport(data, title=f"{file_name} Profiling Report", explorative=True)
        profile.to_file(f"{file_name}.html")

    return jsonify({"status": "File Saved"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
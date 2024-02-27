from flask import Flask, jsonify, request
import requests
import datetime

app = Flask(__name__)

AVALANCHE_API_URL = 'https://api.avalanche.org/v2/public/products/map-layer/SAC'


def get_avalanche_data():
    response = requests.get(AVALANCHE_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/avalanche', methods=['GET'])
def check_status():
    avalanche_forecast = get_avalanche_data()
    if avalanche_forecast and avalanche_forecast.get('features', []):
        first_feature_properties = avalanche_forecast['features'][0]['properties']
        start_date_str = first_feature_properties.get('start_date')

        if start_date_str:
            updated_time = datetime.datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S")
            if updated_time.date() == datetime.datetime.now().date():
                return jsonify({"success": True, "message": "Avalanche forecast retrieved.",
                                "data": first_feature_properties}), 200
            else:
                return jsonify(
                    {"success": False, "message": "Avalanche forecast not updated today. Try again later"}), 200
        else:
            return jsonify({"success": False, "message": "Avalanche forecast start date unknown."}), 200
    else:
        return jsonify({"success": False, "message": "Connection failed or no data is available."}), 500


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # CORS támogatás importálása

app = Flask(__name__)
CORS(app)  # Engedélyezzük a CORS kéréseket az alkalmazásra

@app.route('/get_token', methods=['POST'])
def get_token():
    data = request.json  # JSON kérés fogadása
    form_data = {
        'grant_type': data.get('grant_type', 'password'),
        'client_id': data.get('client_id'),
        'client_secret': data.get('client_secret'),
        'username': data.get('username'),
        'password': data.get('password')
    }
    
    # Kérés elküldése ServiceNow felé application/x-www-form-urlencoded formátumban
    response = requests.post('https://dev227667.service-now.com/oauth_token.do',
                             data=form_data)
    
    return jsonify(response.json())  # Válasz visszaküldése JSON formátumban

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, 
            template_folder='.',
            static_folder='.',
            static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/rankings', methods=['GET'])
def get_rankings():
    # Get API key from environment variable (set in Railway dashboard)
    api_key = os.environ.get('KENPOM_API_KEY')
    season = request.args.get('y', '2026')
    
    if not api_key:
        return jsonify({'error': 'API key not configured on server'}), 401
    
    try:
        response = requests.get(
            f'https://kenpom.com/api.php?endpoint=ratings&y={season}',
            headers={'Authorization': f'Bearer {api_key}'}
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)

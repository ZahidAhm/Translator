# app.py
import os
import json
from flask import Flask, request, jsonify
from translator import english_to_french, french_to_english


app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    lang = data['lang']

    if lang == 'en-fr':
        result = english_to_french(text)
    elif lang == 'fr-en':
        result = french_to_english(text)
    else:
        return jsonify({'error': 'Invalid language pair. Supported pairs: en-fr, fr-en'}), 400

    return jsonify({'result': result}), 200


app.run(debug=True)

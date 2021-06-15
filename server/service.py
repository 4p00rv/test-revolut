from flask import Flask, request, jsonify
import os

from . import app

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<username>', methods=['GET', 'PUT'])
def setBirthday(username):
    data = request.get_json()
    app.logger.info('data: %s', data)
    return "Hello, %s!" % (username)

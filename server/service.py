from flask import Flask, request, jsonify
import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

from . import app
from server.user import User

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<username>', methods=['PUT'])
def setBirthday(username):
    user = None
    data = request.get_json(force=True)
    dateOfBirth = datetime.strptime(data['dateOfBirth'], '%Y-%m-%d')

    # Do not allow future DOB
    if datetime.now() + relativedelta(days=1) < dateOfBirth:
        return "Future date is not allowed", 400

    # Update the DOB if user exists
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username)

    user.dateOfBirth = dateOfBirth
    # Add the birthday to database
    user.save()
    app.logger.info(f"user: {user.dateOfBirth}")
    return "", 204

@app.route('/hello/<username>', methods=['GET'])
def getBirthday(username):
    # Find user
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "Mr. Holmes has been notified of missing user"}), 404

    days = User.calculate_days(datetime.now(), user.dateOfBirth)

    if days == 0:
        return jsonify({"message": f"Hello, {username}! Happy birthday!"})

    return jsonify({"message": f"Hello, {username}! Your birthday is in {days} day(s)"})

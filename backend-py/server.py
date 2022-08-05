#!/usr/bin/env python3

from flask import Flask, request, redirect
from pymongo import MongoClient
from time import time


app = Flask(__name__, static_url_path='', static_folder='../frontend')
mongo_client = MongoClient('mongodb://127.0.0.1:27017/')
troops_collection = mongo_client['troopMap']['troops']

unit_types = ('infantry', 'guerilla', 'paratrooper', 'artillery', 'tank', 'combat-vehicle', 'vehicle', 'other')


@app.route('/report-troops', methods=['POST'])
def store_troop_report():
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])
    unit_type = request.form['unitType']
    num_units = int(request.form['numUnits'])
    mins_ago = int(request.form['minsAgo'])
    notes = request.form['notes']
    assert 0 <= lat < 90
    assert -180 < lng <= 180
    assert unit_type in unit_types
    assert 1 <= num_units <= 1000
    assert 0 <= mins_ago <= 1000
    assert len(notes) < 150
    notes = notes.replace('\t', ' ').replace('  ', ' ')
    epoch_ms = int(time() * 1000) - mins_ago * 60 * 1000
    oid = troops_collection.insert_one({'u': unit_type[0], 'c': num_units, 't': epoch_ms, 'n': notes, 'x': lng, 'y': lat})
    return {'id': str(oid), 'u':unit_type[0], 'c':num_units, 't': epoch_ms, 'n': notes, 'x': lng, 'y': lat}


@app.route('/load-troops')
def load_troop_reports():
    docs = troops_collection.find()
    troops = []
    for i,d in enumerate(docs):
        if i > 1000:
            break
        d['id'] = str(d['_id'])
        del d['_id']
        troops.append(d)
    return {'troops': troops}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

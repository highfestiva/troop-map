#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect


app = Flask(__name__, static_url_path='', static_folder='../frontend')


@app.route('/report', methods=['POST'])
def store_troop_report():
    return {}


@app.route('/load')
def load_all():
    return {}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

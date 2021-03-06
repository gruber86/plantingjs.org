# -*- coding: utf-8 -*-

u"""
module: planting
"""

from flask import Flask
from flask import render_template

from save import save
from get_planting import get_planting


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return render_template('index.html', name=None)


save = app.route('/save', methods=['POST'])(save)
get_planting = app.route('/get_planting/<path:path>')(get_planting)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

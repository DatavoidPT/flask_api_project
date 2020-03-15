"""Imports"""
import datetime
from flask import Flask, render_template
from libs.string_functions import set_text_to_upper

APP = Flask(__name__)

@APP.route("/")
def hello():
    """
        This is the hello world awesomeness API
    """
    return render_template('index.html'
                            , cur_time=datetime.datetime.now()
                            , txt=set_text_to_upper('Its working mate!'))


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000)

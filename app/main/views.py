from flask import render_template, redirect, url_for

from . import main


@main.route('/')
def index():
    return 'Hello World'



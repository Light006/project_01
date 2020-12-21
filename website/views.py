from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')
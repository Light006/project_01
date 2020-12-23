from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('about', __name__)

@bp.route('/about')
def about():
    return render_template('about.html')
from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('services', __name__)

@bp.route('/services')
def services():
    return render_template('services.html')
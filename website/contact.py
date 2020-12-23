from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('contact', __name__)

@bp.route('/contact')
def contact():
    return render_template('contact.html')
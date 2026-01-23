from flask import render_template, Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    current_punches = []

    return render_template('dashboard/base.html', punch_history=current_punches)
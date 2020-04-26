#set FLASK_APP=flasky.py
#set FLASK_DEBUG=1
##remove all db stuff, clear migrations folder, delete data-dev.sqlite
#flask db init
#flask db migrate
#flask db upgrade
#flask shell
#>Role.insert_roles()
#>User.insert_users()
#>ctrl+z
#flask run --host=172.18.30.60

from flask import render_template, session, redirect, url_for, current_app
import datetime
#from ..models import User
#from ..email import send_email
from . import main
from .forms import DeviceForm

from flask_login import login_user, logout_user, login_required, current_user
from ..decorators import admin_required

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    session.clear()

    return render_template('index.html')

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from forms import ContactForm

home = Blueprint('home', __name__)

@home.route('/')
def HomePage():
    return render_template("home_page.html")

@home.route('/login', methods=['POST'])
def login(arg):
    pass

@home.route('/Profile')
@login_required
def Profile():
    return render_template("profile.html", amount=current_user.amount, name=current_user.name)

@home.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)

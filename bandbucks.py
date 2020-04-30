from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from models import User
from __init__ import db

bb = Blueprint('bb', __name__)

@bb.route('/manage')
@login_required
def manage():
    return render_template('manage.html')

@bb.route('/manage/add')
def add():
    return render_template('add.html')

@bb.route('/manage/add', methods=['POST'])
def add_post():
    name = request.form.get('name')
    amount = request.form.get('amount')

    user = User.query.filter_by(name=name).first()

    if not user:
        flash('User does\'t exist.')
        return redirect(url_for('bb.add'))


    user.amount = user.amount + int(amount)
    db.session.commit()

    return redirect(url_for('bb.manage'))

@bb.route('/manage/remove')
def remove():
    return render_template('remove.html')

@bb.route('/manage/remove', methods=['POST'])
def remove_post():
    name = request.form.get('name')
    amount = request.form.get('amount')

    user = User.query.filter_by(name=name).first()

    if not user:
        flash('User does\'t exist.')
        return redirect(url_for('bb.remove'))


    user.amount = user.amount - int(amount)
    db.session.commit()

    return redirect(url_for('bb.manage'))

@bb.route('/manage_success')
def success():
    return render_template('Success.html')

@bb.route('/store')
def store():
    return render_template('store.html')
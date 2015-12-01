from flask import Blueprint, render_template, request
from flask.ext.login import login_required
from flask.ext.login import current_user

from models.item import *

index = Blueprint('index', __name__)

@index.route('/')
def show():
    login = False
    name = None
    items = None
    completed = None
    if current_user.is_authenticated:
        login = True 
        if current_user.name:
            name = current_user.name
        else:
            name = current_user.username
        items = current_user.items.filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    return render_template('index.html',login=login,name=name,
                           items=items,completed=completed)

@index.route('/add',methods=['POST'])
@login_required
def add():
    item = Item('')
    item.user = current_user
    db.session.add(item)
    db.session.commit()
    items = current_user.items.filter_by(completed=False).order_by(Item.due)
    completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    return render_template('items.html',items=items,completed=completed)

@index.route('/edit-text',methods=['POST'])
@login_required
def editText():
    item = Item.get(id=request.form['pk'])
    item.text = request.form['value']
    db.session.add(item)
    db.session.commit()
    return "",200

@index.route('/edit-date',methods=['POST'])
@login_required
def editDate():
    item = Item.get(id=request.form['pk'])
    item.due = datetime.date(datetime.strptime(request.form['value'],"%Y-%m-%d"))
    db.session.add(item)
    db.session.commit()
    return "",200


@index.route('/delete',methods=['POST'])
@login_required
def delete():
    search = request.args.get('search','')
    item = Item.get(id=request.form['id'])
    db.session.delete(item)
    db.session.commit()
    if not search:
        items = current_user.items.filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    else:
        items = current_user.items.filter(Item.text.contains(search)).filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter(Item.text.contains(search)).filter_by(completed=True).order_by(Item.due)
    return render_template('items.html',items=items,completed=completed,search=search)

@index.route('/search',methods=['GET'])
@login_required
def search():
    search = request.args.get('search','')
    name = current_user.username
    if not search:
        items = current_user.items.filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    else:
        items = current_user.items.filter(Item.text.contains(search)).filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter(Item.text.contains(search)).filter_by(completed=True).order_by(Item.due)
    return render_template('index.html',login=True,name=name,items=items,completed=completed,search=search)

@index.route('/done',methods=['POST'])
@login_required
def done():
    search = request.form['search']
    item = Item.get(id=request.form['id'])
    item.completed = True
    db.session.add(item)
    db.session.commit()
    if not search:
        items = current_user.items.filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    else:
        items = current_user.items.filter(Item.text.contains(search)).filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter(Item.text.contains(search)).filter_by(completed=True).order_by(Item.due)
    return render_template('items.html',items=items,completed=completed,search=search)

@index.route('/undo',methods=['POST'])
@login_required
def undo():
    search = request.form['search']
    item = Item.get(id=request.form['id'])
    item.completed = False
    db.session.add(item)
    db.session.commit()
    if not search:
        items = current_user.items.filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter_by(completed=True).order_by(Item.due)
    else:
        items = current_user.items.filter(Item.text.contains(search)).filter_by(completed=False).order_by(Item.due)
        completed = current_user.items.filter(Item.text.contains(search)).filter_by(completed=True).order_by(Item.due)
    return render_template('items.html',items=items,completed=completed,search=search)

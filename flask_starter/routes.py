"""Route declaration."""
from flask import current_app as app
from flask import render_template, flash, redirect, url_for
from datetime import datetime as dt
from .models import db, User
from .forms import UserForm


@app.route('/')
@app.route('/index')
def home():
    """Example home page."""
    return render_template(
        'home.html',
        users=User.query.all(),
        title="Starter home page",
        description="Example how to list all users from database."
    )


@app.route('/about')
def about():
    """Example about page."""
    return render_template(
        'about.html',
        title="Starter about page",
        description="Example about page"
    )


@app.route('/adduser', methods=['GET', 'POST'])
def add_user():

    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            created=dt.now())
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        flash('New user added!')
        return redirect(url_for('home'))

    return render_template('adduser.html',
                           form=form,
                           title="Add user",
                           description="Example how to use Flask-WTForms to add Users to a database",
                           )


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html', title="Success", description="Sucessfully added a new user!")


@app.route('/failure', methods=('GET', 'POST'))
def failure():
    return render_template('failure.html', title="Success", description="Failed to add a new user!")

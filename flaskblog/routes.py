import secrets , os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm , UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Ilham Adhim',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 20, 2019'
    },
    {
        'author': 'Adhim Ilham',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('mainpage.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# register route
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

        # Takes RegistrationForm from forms.py
    form = RegistrationForm()

    if form.validate_on_submit():
        # convert password from string type to hash. then return it to string again
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # use hashed_password to pass into user variables in User class in models.py
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Add to database
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()

    if form.validate_on_submit():
        # which user to be logged in, we should match it with database
        user = User.query.filter_by(email=form.email.data).first()
        # Pass user variable to condition
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # use to let user logged in by class inside the flask_login module
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'You are logged in as {user.username} !' , 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', Loginform=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    # we want to make a hex random to the saved picture from user just to avoid
    # collision if the original name is already in our folder
    random_hex = secrets.token_hex(8)
    # pass in the picture that user uploaded to parameter
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    # Move the picture uploaded to our storage
    picture_path = os.path.join(app.root_path,'static/profile_pics/', picture_fn)

    # from pillow modules, resize the uploaded image to 125 px
    # resize, so that we can make our website faster to load and save storages
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # save picture to picture_path directory (earlier)
    # form_picture.save(picture_path)
    i.save(picture_path)

    return picture_fn

@app.route("/account",methods=['GET', 'POST'])
# login_required is a modules from flask-login
# below this comment, is used to make user logged in first before they can access account.html
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file


        # change the username and email of logged in user 
        current_user.username = form.username.data
        current_user.email = form.email.data
        # not use session.add because we want to change database , not add a new record
        db.session.commit()
        flash('Your account has been updated' , 'success')
        # reason why we put redirect to account here is to prevent unsaved changes of data when we render
        # account.html again. bcs it will send new get request
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static',filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file = image_file , form = form)
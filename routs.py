from flask import render_template , redirect
from os import path
from forms import AddNews, EditNews, Reg, LoginForm , FeedbackForm, AddComment
from flask_login import login_user, logout_user, login_required, current_user
from models import  Product , User, Feedback, Comment
from ext import app, db
products = [
    {"title": "Some news about Georgia", "paragraph": "some dummy text about news", "img": "../static/georgia.png", "id":0},
    {"title": "Some news about world", "paragraph": "some dummy text about news", "img": "../static/earth.jpg", "id":1},
    {"title": "Some news about Tbilisi", "paragraph": "some dummy text about news", "img": "../static/tbilisi.jpg", "id":2},
]

@app.route("/")
def home():

    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/add_news", methods=["POST", "GET"])
@login_required
def add_news():
    if current_user.role != "admin":
        return redirect("/")
    form = AddNews()
    if form.validate_on_submit():

        new_news = Product(title=form.title.data, paragraph=form.paragraph.data, img= form.img.data.filename)
        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        db.session.add(new_news)
        db.session.commit()
        return redirect("/")




    return render_template("add_news.html", form=form)




@app.route("/edit/<int:index>", methods=["GET","POST"])
@login_required
def edit_news(index):
    if current_user.role != "admin":
        return redirect("/")

    product = Product.query.get(index)
    form = EditNews(title=product.title, paragraph=product.paragraph, img=product.img)
    if form.validate_on_submit():
        product.name = form.title.data
        product.paragraph = form.paragraph.data
        product.img = form.img.data.filename

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)


        db.session.commit()
        return redirect("/")

    return  render_template("edit.html", form=form)


@app.route("/delete_news/<int:index>", methods=["GET","POST"])
@login_required
def delete_news(index):
    if current_user.role != "admin":
        return redirect("/")

    product = Product.query.get(index)

    db.session.delete(product)
    db.session.commit()
    return redirect("/")


    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = Reg()
    if form.validate_on_submit():

        user = User(username=form.username.data, password=form.password.data)
        user.create()
        db.session.commit()

    return render_template('register.html', form=form)



@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html",form=form)

@app.route("/logout")
def logout():
    logout_user()

    return redirect("/")


@app.route('/feedback', methods=["GET","POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feed_back = Feedback(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(feed_back)
        db.session.commit()

        return redirect("/feedback")
    return render_template("feedback.html", form=form)

@app.route('/view_product/<int:index>', methods=["GET", "POST"])
def view_product(index):
    news = Product.query.get(index)
    form = AddComment()

    if form.validate_on_submit():
        new_comment = Comment(name=form.comment_name.data, product_id=index)


        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(product_id=index).all()


    return render_template("product.html", news=news, form=form, comments=comments)






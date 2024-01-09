from ext import  db, app, login_manager

from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
class User(db.Model, BaseModel, UserMixin):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    comments = db.relationship('Comment', backref='author', lazy=True)


    def __init__(self, username, password, role="guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self,password):
        return check_password_hash(self.password, password)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    paragraph = db.Column(db.String)
    img = db.Column(db.String)
    comments = db.relationship('Comment', backref='product', lazy=True)
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    message = db.Column(db.String)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        new_user = User(username="admin", password="password", role="admin")
        new_user.create()



        normal_user = User(username="guest", password="password", role="guest")
        normal_user.create()




class Edit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    paragraph = db.Column(db.String)
    img = db.Column(db.String)
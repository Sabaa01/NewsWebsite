from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired , Length
class AddNews(FlaskForm):
    title = StringField("სათაური", validators=[DataRequired()])
    paragraph = StringField("აღწერა", validators=[DataRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired()])
    submit = SubmitField("დამატება")

class EditNews(FlaskForm):
    title = StringField("სათაური", validators=[DataRequired()])
    paragraph = StringField("აღწერა", validators=[DataRequired()])
    img = FileField("სურათის სახელი")

    submit = SubmitField("დამატება")

class FeedbackForm(FlaskForm):
    name = StringField("სახელი", validators=[DataRequired()])
    email = StringField("მეილი", validators=[DataRequired()])
    message = StringField("კომენტარი")

    submit = SubmitField("გაგზავნა")
class Reg(FlaskForm):
    username = StringField("სახელი", validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("პაროლი", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired()])
    mail = StringField("მეილი", validators=[DataRequired()])

    submit = SubmitField("დარეგისტრირება")

class LoginForm(FlaskForm):
    username = StringField("სახელი",validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired()])

    submit = SubmitField("ავტორიზაცია")


class AddComment(FlaskForm):
    comment_name = StringField("კომენტარი", validators=[DataRequired()])

    submit = SubmitField("დამატება")



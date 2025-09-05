from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Creates a RegisterForm to register new users

class RegisterForm(FlaskForm):
    Email = StringField("Email",validators=[DataRequired()])
    Password = StringField("Password", validators=[DataRequired()])
    Name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign up")


# Creates a LoginForm to login existing users

class LoginForm(FlaskForm):
    Email = StringField("Email",validators=[DataRequired()])
    Password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Creates a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_editor = CKEditorField("Comment field", validators=[DataRequired()])
    #comment_editor = StringField("Comment field", validators=[DataRequired()])
    submit = SubmitField("Upload comment")
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()], render_kw={"placeholder": "Blog Post Title"})
    subtitle = StringField("Subtitle", validators=[DataRequired()], render_kw={"placeholder": "Subtitle"})
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()], render_kw={"placeholder": "Blog Image URL"})
    body = CKEditorField("Blog Content", validators=[DataRequired()], render_kw={"placeholder": "Blog Content"})
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "someone@example.com"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder":
                                                                                     "A_Really_Str0ng_Password_4U!"})
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Coolest Name Ever!"})
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
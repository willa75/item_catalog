from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, URL

from .models import User

class OpenIDForm(FlaskForm):
	openid = StringField('OpenID Url', [DataRequired(), URL()])

class LoginForm(FlaskForm):
	username = StringField('Username', [
		DataRequired(), Length(max=255)
	])
	password = PasswordField('Password', [DataRequired()])
	remember = BooleanField("Remember Me")

	def validate(self):
		check_validate = super(LoginForm, self).validate()

		# if our validators do not pass
		if not check_validate:
			return False

		# if user doesn't exist
		user = User.query.filter_by(
			username=self.username.data
		).first()
		if not user:
			self.username.errors.append(
				'Invalid username or password'
			)
			return False

		# Do passwords match
		if not user.check_password(self.password.data):
			self.username.errors.append(
				'Invalid username or password'
			)
			return False

		return True

class RegisterForm(FlaskForm):
	username = StringField( 'username', [
		DataRequired(),
		Length(max=255)
	])
	password = PasswordField('password', [
		DataRequired(),
		Length(min=8)
	])
	confirm = PasswordField('Confirm Password', [
		DataRequired(),
		EqualTo('password')
	])
	recaptcha = RecaptchaField()

	def validate(self):
		check_validate = super(RegisterForm, self).validate()

		#if validation fails
		if not check_validate:
			return False

		user = User.query.filter_by(
			username=self.username.data
		).first()

		# Is the username already in use?
		if user:
			self.username.errors.append(
				"User with that username already exists"
			)
			return False

		return True

class PostForm(FlaskForm):
	title = StringField('Title', [
		DataRequired(),
		Length(max=255)
	])
	text = TextAreaField('Content', [DataRequired()])

class CommentForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])
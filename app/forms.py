from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class Create_quiz(Form):
	question_text = TextAreaField('question_text')
	oA = StringField('oA')
	oB = StringField('oB')
	oC = StringField('oC')
	oD = StringField('oD')
	correct_answer = RadioField('correct_answer', choices = [('A','A'), ('B','B'), ('C','C'), ('D','D')])
	category = StringField('category')

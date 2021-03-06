from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, RadioField
from wtforms import validators, ValidationError
from flask_wtf.file import FileField, FileRequired

#Form for adding questions to a quiz
class Create_quiz(Form):
	question_text = TextAreaField('question_text', [validators.Required("Field Required")]) # Input for question text
	oA = StringField('oA', [validators.Required("Field Required")]) # Input for option A
	oB = StringField('oB', [validators.Required("Field Required")]) # Input for option B
	oC = StringField('oC', [validators.Required("Field Required")]) # Input for option C
	oD = StringField('oD', [validators.Required("Field Required")]) # Input for option D
	#file_path=StringField('file_path',[validators.Required("Field Required")])
	correct_answer = RadioField('correct_answer', choices = [('A','A'), ('B','B'), ('C','C'), ('D','D')]) # Radio Button to select the correct answer
	category = StringField('category', [validators.Required("Field Required")]) # Input for question category

# Form for taking response for a question
class Display_question(Form):
	submission = RadioField('submission')
# form for creating a quiz
class Add_quiz(Form):
	name=StringField('name', [validators.Required("Field Required")])

class Display_quiz(Form):
	name = RadioField('name')

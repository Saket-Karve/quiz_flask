from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, RadioField
from wtforms.validators import DataRequired

#Form for adding questions to a quiz
class Create_quiz(Form):
	question_text = TextAreaField('question_text') # Input for question text
	oA = StringField('oA') # Input for option A
	oB = StringField('oB') # Input for option B
	oC = StringField('oC') # Input for option C
	oD = StringField('oD') # Input for option D
	correct_answer = RadioField('correct_answer', choices = [('A','A'), ('B','B'), ('C','C'), ('D','D')]) # Radio Button to select the correct answer
	category = StringField('category') # Input for question category

# Form for taking response for a question
class Display_question(Form):
	submission = RadioField('submission')
# form for creating a quiz
class Add_quiz(Form):
	name=StringField('name')

class Display_quiz(Form):
	name = RadioField('name')

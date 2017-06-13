from app import db
#from sqlAlchemy.orm import relationship

class quiz(db.Model):
	quiz_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Integer)
	questions = db.relationship('question', backref='que', lazy='dynamic')
	responses = db.relationship('response', backref='res', lazy='dynamic')

class question(db.Model):
	question_id = db.Column(db.Integer, primary_key=True)
	quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id')) #Foreign Key to refer to corresponding quiz
	q_text = db.Column(db.String) #Text of the question to be solved
	#myfile = db.Column(db.String) #Object of type File which stores link and alt text to image
	option1 = db.Column(db.String) #option A
	option2 = db.Column(db.String) #option B
	option3 = db.Column(db.String) #option C
	option4 = db.Column(db.String) #option D
	answer = db.Column(db.String) #correct answer to the question (A/B/C/D)
	category = db.Column(db.String) #category to which question belongs to
	responses = db.relationship('response', backref='res', lazy='dynamic')

class user(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	responses = db.relationship('response', backref='res', lazy='dynamic')

class response(db.Model):
	response_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id')) #Foriegn key to the user of the response
	quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id')) #Foriegn key to the corresponding quiz for the response
	question_id = db.Column(db.Integer, db.ForeignKey('question.question_id')) #Foriegn key to the corresponding question for the response
	response = db.Column(db.String) #Response submitted by the user
	result = db.Column(db.Boolean) #True if matches correct answer, False if does not match correct answer
	


	

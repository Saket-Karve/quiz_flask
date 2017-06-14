from flask import render_template, session
from flask import request, redirect, url_for
from app import app, db, questions
from .questions import question,quiz
from .forms import Create_quiz
from .forms import Display_question, Add_quiz

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/addquestions', methods=['GET', 'POST'])
def quiz_form():
	form = Create_quiz() # Fetch appropriate form from forms.py
	if request.method == "POST":
		#collecting data from forms.py
		que=form.question_text.data #collect the entered question text
		option_A=form.oA.data #collect entered option A text
		option_B=form.oB.data #collect entered option B text
		option_C=form.oC.data #collect entered option C text
		option_D=form.oD.data #collect entered option D text
		correct_answer=form.correct_answer.data #collect entered correct answer
		category=form.category.data #collect entered question category
		q=question(q_text=que,option1=option_A,option2=option_B,option3=option_C,option4=option_D,answer=correct_answer,category=category)# Create object of class question from questions.py
		db.session.add(q) # Add object q to db.session
		db.session.commit() # Commit changes to app.db
	return render_template("create_quiz.html", title = "Add Question", form=form) # Render form template 

@app.route('/displayquestion', methods=['GET', 'POST'])
def display_question():
	form = Display_question() # Fetch appropriate form to get user response
	if request.method == "POST":
		#Collect user submisstion
		submission = form.submission.data
		if submission==session['correct_answer']:
			result=True
		else:
			result=False
		q=response(quiz_id=session['quiz_id'],question_id=session['question_id'],response=submission,result=result)
		db.session.add(q)
		db.session.commit()	
		# Display Next Question
		if session['q_no'] != 0:
			session['q_no'] = session['q_no'] + 1
		else:
			session['q_no'] = 1
		q = questions.question.query.get(session['q_no'])
		if q:
			form.submission.choices = [(q.option1, q.option1), (q.option2, q.option2), (q.option3, q.option3), (q.option4, q.option4)]
			session['question_id']=q.question_id
			session['correct_answer']=q.answer
			return render_template("display_question.html", q = q, quiz_name=session['quiz_nzme'], form=form)

		else:
			session['quiz_id']=-1;
			user = {'nickname': 'Miguel'}
			return render_template('index.html', title="Hello", user=user, posts=[])
	else:
		q = questions.question.query.get(1)
		form.submission.choices = [(q.option1, q.option1), (q.option2, q.option2), (q.option3, q.option3), (q.option4, q.option4)]
		session['question_id']=q.question_id
		session['correct_answer']=q.answer
		session['q_no']=1;
		return render_template("display_question.html", q = q, form=form)


# create Quiz

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
	form = Add_quiz()
	if request.method == "POST":
		quiz_name=form.name.data
		q=quiz(name=quiz_name)
		db.session.add(q)
		db.session.commit()
		session['quiz_name']=quiz_name
		session['quiz_id'] = questions.quiz.query.filter_by(name=quiz_name).first()
		return redirect(url_for('display_question')) 
	return render_template("add_quiz.html", title = "create quiz", form=form)

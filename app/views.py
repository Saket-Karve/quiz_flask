from flask import render_template, session
from flask import request, redirect, url_for
from app import app, db, questions
from .questions import question,quiz, response
from .forms import Create_quiz, Display_quiz
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
	if request.method == "POST" and form.validate():
		#collecting data from forms.py
		que=form.question_text.data #collect the entered question text
		option_A=form.oA.data #collect entered option A text
		option_B=form.oB.data #collect entered option B text
		option_C=form.oC.data #collect entered option C text
		option_D=form.oD.data #collect entered option D text
		correct_answer=form.correct_answer.data #collect entered correct answer
        	# Based on entered answer, store the option text in the answer field in the database
        	if correct_answer == 'A':
            		correct_answer = option_A
        	elif correct_answer == 'B':
            		correct_answer = option_B
        	elif correct_answer == 'C':
            		correct_answer = option_C
       		elif correct_answer == 'D':
            		correct_answer = option_D
        	category=form.category.data #collect entered question category
        	q=question(quiz_id = session['quiz_id'],q_text=que,option1=option_A,option2=option_B,option3=option_C,option4=option_D,answer=correct_answer,category=category)# Create object of class question from questions.py
        	db.session.add(q) # Add object q to db.session
        	db.session.commit() # Commit changes to app.db
		if request.form['submit'] == 'ADD':
            		return redirect(url_for('quiz_form'))
		elif request.form['submit'] == 'SUBMIT':
			return redirect(url_for('display_quiz'))
    	return render_template("create_quiz.html", title = "Add Question", quiz_name = session['quiz_name'], form=form) # Render form template
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
		if session['question_id'] != 0:
			session['question_id'] = session['question_id'] + 1
		else:
			session['question_id'] = 1
		q = questions.question.query.filter_by(quiz_id=session['quiz_id'],question_id=session['question_id']).first()
		if q:
			form.submission.choices = [(q.option1, q.option1), (q.option2, q.option2), (q.option3, q.option3), (q.option4, q.option4)]
			session['question_id']=q.question_id
			session['correct_answer']=q.answer
			return render_template("display_question.html", q = q, quiz_name=session['quiz_name'], form=form)

		else:
		#	session['quiz_id']=-1;
			user = {'nickname': 'Miguel'}
			return redirect(url_for('display_result'))
	else:
		q = questions.question.query.filter_by(quiz_id=session['quiz_id']).first()
		form.submission.choices = [(q.option1, q.option1), (q.option2, q.option2), (q.option3, q.option3), (q.option4, q.option4)]
		session['question_id']=q.question_id
		session['correct_answer']=q.answer
		#session['q_no']=1;
		return render_template("display_question.html", q = q, form=form)


# create Quiz

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
	form = Add_quiz()
	if request.method == "POST" and form.validate():
		quiz_name=form.name.data
		q=quiz(name=quiz_name)
		db.session.add(q)
		db.session.commit()
		session['quiz_name']=quiz_name
		session['quiz_id'] = questions.quiz.query.filter_by(name=quiz_name).first().quiz_id
		return redirect(url_for('quiz_form'))
	return render_template("add_quiz.html", title = "create quiz", form=form)

@app.route('/displayquiz', methods=['GET', 'POST'])
def display_quiz():
    form = Display_quiz()
    if request.method == "POST":
        quiz_name = form.name.data
        session['quiz_name'] = quiz_name
        session['quiz_id'] = questions.quiz.query.filter_by(name=quiz_name).first().quiz_id
        return redirect(url_for('display_question'))
    q = questions.quiz.query.all()
    form.name.choices = []
    for quiz in q:
        form.name.choices.append((quiz.name, quiz.name))
    return render_template("display_quiz.html", title="Display Quiz", form=form)

@app.route('/displayresult')
def display_result():
        total=len(questions.response.query.filter_by(quiz_id=session['quiz_id']).all())
        correct=len(questions.response.query.filter_by(result=True,quiz_id=session['quiz_id']).all())
        marks=(correct*100.0)/total;
        session['quiz_id']=-1
        return render_template("display_result.html",title="display result",marks=marks,total=total,correct=correct)

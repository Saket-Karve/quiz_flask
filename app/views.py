from flask import render_template, session
from flask import request, redirect, url_for
from app import app, db
from .questions import question
from .forms import Create_quiz

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
	form = Create_quiz()
	if request.method == "POST":
		#collecting data from forms.py
		que=form.question_text.data #collect the question
		option_A=form.oA.data
		option_B=form.oB.data
		option_C=form.oC.data
		option_D=form.oD.data
		correct_answer=form.correct_answer.data
		print(correct_answer)
		category=form.category.data
		q=question(q_text=que,option1=option_A,option2=option_B,option3=option_C,option4=option_D,answer=correct_answer,category=category)
		db.session.add(q)
		db.session.commit()
	return render_template("create_quiz.html", title = "Add Question", form=form)

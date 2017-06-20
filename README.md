###################Add plugin to a pybossa###################### 

plugins are used to add your own custome feature to a running pybossa server without the need of touching the server code.

pybossa plugins are written in flask.

####################User Evaluation Plugin ####################

put all your files into a folder and put it inside the plugin folder of pybossa server. our folder name is quiz which has following heirarchy

quiz
|-- __init__.py
|-- models.py
|-- info.json
|-- forms.py
|-- config.py
|-- views.py
|-- templates
    |-- add_quiz.html
    |-- base.html
    |-- create_quiz.html
    |-- display_question.html
    |-- display_quiz.html
    |-- display_result.html
    |-- index.html
    |-- quiz.html

1. __init__.py import the flask plugin from flask.ext.plugin and from views import blueprint now register blueprint with its url_prefix "/user_evaluation"

2. info.json will contain following schema
	{
		"identifier":"quiz",
		"name":"Quiz",
		"author":"author_name",
		"license":"AGPLv3",
		"description":"Quiz for user evaluation",
		"version":"0.0.1"
	}

3. models.py consists schema for the different tables of the database there are following schemas
A. quiz(int quiz_id primary key,name string) relationship with question and response schema
B. question(question_id int primary key,int quiz_id foreign key of quiz schema,q_text string, option1 string, option2 string, option3 string, option4 string, answer string,category string) relationship with response
C. response(response_id int primary key,quiz_id int foreign key from quiz, question_id int foreign key from question schema,response string,result boolean)

4. views.py implemnets all the functionalities and help us to route through our application.
it has following set of methods 
A. index() to redirect @ home page
B. path="user_evaluation/create_quiz" create_quiz() to redirect to a page where we can create a quiz. in this step we will create a quiz and one entry is created in the quiz schema.
C. path="user_evaluation/addquestions" quiz_form() quiz name is stored using session in the above step now in that we will add questions to our existing quiz.
D. path="user_evaluation/displayquiz" display_quiz() will show all the existing quiz to the user he can choose one from the set of quiz and solve the questions.
E. path="user_evaluation/displayquestion" display_question() will display all the questions one by one.
F.  path="user_evaluation/displayresult" display_result() will display the result in percentage marks.

forms.py 

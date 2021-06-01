from flask import Flask, request, render_template
from flask_mail import Mail, Message


app = Flask(__name__)

	
@app.route('/',methods=['POST','GET'])
def index():
	return render_template('MyMailProjForm.html')


@app.route('/sent', methods=['POST','GET'])
def login():

	subjects = ['AFL', 'COA', 'DBMS', 'OS', 'PDC', 'WT', 'B_COM', 'DBMS_LAB', 'OS_LAB', 'WT_LAB']
	credits = [4, 4, 4, 3, 4, 3, 1, 1, 1, 1]
	credits_got = 0
	credits_total = 0
	l = len(subjects)
	for i in range(l):
		marks_string = request.form[subjects[i]]
		if marks_string != '':
			marks = int(marks_string)
			if(marks==100)
				credits_got+=10*credits[i]
				credits_total += credits[i]
			else	
				credits_got += ((marks // 10) + 1) * (credits[i])
				credits_total += credits[i]
	SGPA = credits_got / credits_total
	print('Your SGPA Calculated is:', SGPA)

	return f"<center><h1><br><br><br>SGPA Calculated: {SGPA}</h1></center>"

if __name__ == '__main__':
	app.run(debug=True)


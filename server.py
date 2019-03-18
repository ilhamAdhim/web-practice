#import flask
# render_template digunakan untuk merender html dan css . 
# url_for digunakan di file layout.html untuk mencari file css
from flask import Flask ,jsonify ,request,render_template, url_for , flash , redirect
from forms import RegistrationForm , LoginForm
#membuat aplikasi flask 	 	
app = Flask(__name__)


app.config['SECRET_KEY'] = '3ac9f1844e2e16c02698d86c05047fde'



biodata = [	
    {
        "nama": "budi",
        "alamat": "malang"
    },
    {
        "nama": "ananta",
        "alamat": "malang"
    }
]

posts = [
	{
		"author" 		: "Ilham",
		"post_date" 	: "August 20, 2019",
		"content_title"	: "First post",
		"content"		: "lorem ipsum dolor si amet"
	},

	{
		"author" 		: "Adhim Mc",
		"post_date" 	: "July 12, 2019",
		"content_title"	: "Second post",
		"content"		: "lorem ipsum dolor si amet second"
	},

	{
		"author" 		: "ilhamm179",
		"post_date" 	: "March 18, 2019",
		"content_title"	: "Third post",
		"content"		: "lorem ipsum dolor si amet third"
	},
	
	{
		"author" 		: "TestUser",
		"post_date" 	: "July 20, 2019",
		"content_title"	: "Fourth post",
		"content"		: "lorem ipsum dolor si amet Fourth"
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('mainpage.html' , posts = posts)


@app.route("/about")
def about():
  return render_template('about.html') 

@app.route("/biodata")
def index():
    return jsonify(biodata)


@app.route("/register" , methods = ['GET','POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
  		flash(f'Account created for { form.username.data }! ' , 'success')
  		return redirect('home')
  # else :
  # 		flash(f'Account cannot be created ! check registration rules correctly ' , 'danger')

  		

# below Python 3.6 use this one :
# flash('Account created for {}!'.format({form.username.data}))

  return render_template('register.html' , title='Register' , form = form)


@app.route("/login" , methods = ['GET','POST'])
def login():
  Loginform = LoginForm()

  if Loginform.validate_on_submit():
  		flash(f'You are signed in as { Loginform.username.data }! ' , 'success')
  		return redirect('home')
  
  return render_template('login.html' , title='Login' , Loginform = Loginform)



app.run()

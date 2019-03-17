#import flask
from flask import Flask ,jsonify ,request,render_template, url_for

#membuat aplikasi flask 	 	
app = Flask(__name__)
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
		"content_title"	: "first post",
		"content"		: "lorem ipsum dolor si amet"
	},

	{
		"author" 		: "Adhim Mc",
		"post_date" 	: "July 12, 2019",
		"content_title"	: "second post",
		"content"		: "lorem ipsum dolor si amet second"
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

app.run()

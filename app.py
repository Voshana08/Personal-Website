from flask import Flask,render_template,request
#Creating the flask app
app = Flask(__name__)
#Creating the routes to the different pages
#base route

@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('index.html')

#Contact route
@app.route('/contact',methods = ['GET','POST'])
def contact():
    return render_template('contact.html')
#Learning Route
@app.route('/learning',methods = ['GET','POST'])
def learning():
    return render_template('learning.html')


if __name__ == '__main__':
    
    app.run(debug=True,port=5001)
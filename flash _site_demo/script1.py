from flask import Flask, render_template  #Importing the class flask object from the flash libary

app = Flask(__name__) #instantiation of the flask object __name__gets the value of the python script

@app.route('/')
def home():
    return render_template('home.html') #rendering html templates in a Python app

@app.route('/about')
def about():
    return render_template('about.html')

if  __name__ == "__main__":
    app.run(debug = True)

from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('new 1.html')

@app.route('/survey')
def survey():
    return render_template('results.html')

@app.route('/forms_test')
def forms_test():
    return render_template('Survey.html')

@app.route('/receive_form_data',methods=['POST'])
def receive_form_data():
    print(request.form) 
    data = request.form
    return 'apple'

if __name__== "__main__":
    app.run()

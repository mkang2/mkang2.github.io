from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process the form data (you can add your logic here)
        
        return f"Form submitted successfully! <br> Name: {name} <br> Email: {email} <br> Message: {message}"

if __name__ == '__main__':
    app.run(debug=True)

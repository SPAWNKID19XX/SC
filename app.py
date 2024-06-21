from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_request_form')
def send_request_form():
    print(send_request_form)

if __name__ == '__main__':
    app.run(debug=True)

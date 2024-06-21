from flask import Flask, render_template
from form import FormSubscribe
from secret import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormSubscribe()
    if form.validate_on_submit():
        full_name = form.full_name.data
        country = form.countries.data
        wtsapp = form.wtsapp.data
        return f"Thank you for subscribing, {full_name} from {country}! We will contact you at {wtsapp}."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

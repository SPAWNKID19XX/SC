#Python 3.12.3

from flask import Flask, render_template,redirect,url_for, request
from form import FormSubscribe
from secret import SECRET_KEY
from flask_mail import Mail, Message
import my_secret_data
from twilio.rest import Client


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = my_secret_data.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = my_secret_data.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = my_secret_data.MAIL_SENDER
#app.config['EMAIL_HOST_PASSWORD'] = my_secret_data.EMAIL_HOST_PASSWORD
mail=Mail(app)

account_sid = my_secret_data.ACCOUNT_SID
auth_token = my_secret_data.AUTH_TOKEN
client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormSubscribe()
    if form.validate_on_submit():
        full_name = form.full_name.data
        country = form.countries.data
        wtsapp = form.wtsapp.data
        success_msg = f"Thank you for subscribing, {full_name} from {country}! We will contact you at {wtsapp}."
        print(success_msg)
        if request.method == 'POST':
            send_email(full_name, country, wtsapp)
            send_msg_whatsapp(full_name,wtsapp)
        return redirect(url_for('accept'))
    return render_template('index.html', form=form)

@app.route('/accept')
def accept():
    return render_template('accept_appointment_template.html')

def send_email(name, country, whatsapp):
    recipient = my_secret_data.MAIL_SENDER
    subject = "New User Subscribe"
    message_body = f"""New user wont to connect to our webinar
                        Cantact Data:
                            Name :{name}
                            Country :{country} 
                            watsapp {whatsapp}"""

    message = Message(subject=subject,
                        recipients=[recipient],
                        body=message_body)
    
    try:
        mail.send(message)
        print('Email sent successfully!') 
    except Exception as e:
        print('DOES NOT')
        print(str(e))

def send_msg_whatsapp(name, whatsapp):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f'Hello {name}.\n we glad then you wont visit us',
    to=[f'whatsapp:{whatsapp}']
    )

    print(message.sid)

if __name__ == '__main__':
    app.run(debug=True)

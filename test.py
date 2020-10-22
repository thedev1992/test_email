from flask import Flask, render_template, request
import smtplib, ssl

app = Flask(__name__)


def read_creds():
    user = passw = ""
    with open("email_test.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()
    return user, passw

sender, password = read_creds()

port = 465

message= """\

subject: email test

c'est du python pure """


@app.route("/",methods=['GET', 'POST'])
def subscribe():

    if request.method == "POST":
        email = request.form.get("email")
        context = ssl.create_default_context()
        print("starting to send ")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, email, message)
            print("sent email")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
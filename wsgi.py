from flask import Flask
application = Flask(__name__)

@application.route("/<username>")
def hello(username):
    return "Traisca %s!" % username

if __name__ == "__main__":
    application.run()

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hi Cambridge!"

if __name__ == "__main__":
    application.run()

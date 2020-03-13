from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/ready")
def ready():
    return "Ready!"

@application.route("/health")
def healthy():
    return "Healthy!"

if __name__ == "__main__":
    application.run()

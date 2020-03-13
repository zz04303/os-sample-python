import socket
import datetime

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    currentDT = datetime.datetime.now()
    currentDT_formatted = currentDT.strftime("%Y-%m-%d %H:%M:%S")
                                             
    return currentDT_formatted +": Hello World! This is a message from host: " + hostname + " (" + host_ip + ") \n"
                                             
                                             
                                             
@application.route("/ready")
def ready():
    return "Ready!"

@application.route("/health")
def healthy():
    return "Healthy!"

if __name__ == "__main__":
    application.run()

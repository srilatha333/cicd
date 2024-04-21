from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def skill():
    message = "{name} is a Gitlab pro"
    return message.format(name=os.getenv("NAME", "Seetha Ram"))
    
if _name_ == "_main_":
    app.run(host='0.0.0.0', port=8080)

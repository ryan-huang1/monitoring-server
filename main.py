from flask import Flask
from myblueprint import myblueprint

app = Flask(__name__)
app.register_blueprint(myblueprint)

if __name__ == '__main__':
    app.run(debug=True)
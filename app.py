from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	names = {1: "Martin", 2: "Leeping", 3: "Justin", 4: "Mark", 5: "Ernie", 6: "Michael"}
	name = names[random.randint(1,6)]
	return "Hello, " + name + "!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	names = {1: "Yorkie", 2: "Penfold", 3: "Rents", 4: "Dog", 5: "Venners", 6: "Maggie"}
	name = names[random.randint(1,6)]
	return "Hello, " + name + "!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

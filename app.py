from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    output = "HELLO LANDING PAGE!!!"
    print(output)
    return output

    
print("HEllO FROM OCP")
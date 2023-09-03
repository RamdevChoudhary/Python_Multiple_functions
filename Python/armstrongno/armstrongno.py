from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello dude it's just testing"

@app.route('/armstrong/<int:num>')
def armstrong(num):
    sum = 0
    order = len(str(num))
    copy_n = num
    while(num>0):
        digit = num%10
        sum+= digit ** order
        num = num//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong numebr")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "120.126.235.25"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "120.126.235.25"
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
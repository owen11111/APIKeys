from flask import Flask, request, Response

app = Flask(__name__)

validAPIKeys = ['1234', '5678']

@app.route('/API/forms', methods=["GET"])
def apiForm():
    key = request.headers.get('APIkey')
    if key in validAPIKeys:
        response_data = {
            "Question 1": "Example Response",
            "Question 2": "Example Response",
            "Question 3": "Example Response",
            "Question 4": "Example Response",
            "Question 5": "Example Response"
        }
        return jsonify(response_data), 200
    else:
        return Response("Invalid Credentials", status=401)

if __name__ == "__main__":
    app.run()

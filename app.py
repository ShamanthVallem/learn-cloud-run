from flask import Flask, request
from flask_cors import CORS, cross_origin
import traceback
import random


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.get("/")
@cross_origin(supports_credentials=True)
def home():
    return {"status": "server is running"}, 200

@app.post("/get_random_numbers")
def generate_random_numbers():
    '''
    Route to generate random numbers
    '''
    try:
        data = request.json
        if type(data['number']) is not int:
            return {"status": "Error",
                    "message": "Paylod not valid"}
        random_numbers = list()
        for i in range(int(data["number"])):
            random_numbers.append(random.randint(10000, 100000))   
        return {"status": "Success",
                "Numbers_generated": random_numbers}
        
    except Exception as e:
        return {"status": "Error",
                "message": e,
                "Traceback": traceback.format_exc()}

if __name__ == "__main__":
    app.run(debug = True)
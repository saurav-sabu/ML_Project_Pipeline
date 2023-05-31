from flask import Flask 
from src.logger import logging
from src.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("We are testing our custom file")
   
    except Exception as e:
        new =  CustomException(e,sys)
        logging.info(new.error_message)
        return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)




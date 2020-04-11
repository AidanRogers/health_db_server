from flask import Flask, jsonify, request

db = [] # defined in the global section of the module

app = Flask(__name__) #class flask functions are saved to variable app



if __name__ == '__main__':
    app.run()
    
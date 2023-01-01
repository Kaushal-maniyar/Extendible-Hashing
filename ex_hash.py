from flask import Flask
from hashtable import Hash


app = Flask(__name__)


@app.route('/')
def index():
    return h.dis_hash_table
    # return h.hash_table


@app.route('/insert/<int:number>')
def insert(number):
    h.insert(number)
    return h.dis_hash_table
    # return h.hash_table


@app.route('/delete/<int:number>')
def delete(number):
    h.delete_number(number)
    return h.dis_hash_table
    # return h.hash_table


if __name__ == '__main__':
    h = Hash()
    app.run(debug=True)

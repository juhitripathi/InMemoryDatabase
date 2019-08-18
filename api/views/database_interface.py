from flask import Flask

app = Flask(__name__)

@app.route('/store')
def welcome():
    return 'Welcome to in-memory database api'


@app.route('/store/query', methods=['GET'])
def retrieve_database_entry():
    return 'Matching entry'


@app.route('/store/totalentries', methods=['GET'])
def total_entries():
    return 'Total entries in database'


@app.route('/store', methods=['POST'])
def save_entry():
    return 'Entry Saved'


@app.route('/store/modifyentry', methods=['PUT'])
def modify_entry():
    return 'Matching Entry Modified'


@app.route('/store/deleteentry', methods=['DELETE'])
def delete_entry():
    return 'Matching entry deleted'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

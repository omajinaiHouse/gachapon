from flask import Flask
from flask import render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/umeume', methods=['GET'])
def test_get():
    resp = jsonify(
        {
            'message': 'ok',
        }
    )
    return resp, 200

@app.errorhandler(404)
def not_found(err):
    resp = jsonify(
        {
            'id': err.discription['id'],
            'message': 'not found.',
            'result': err.code
        }
    )
    return resp, err.code

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify

from errors import ApiException
from views import AdvViews, OwnerViews

app = Flask('app')


@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
        'status': 'errors',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


app.add_url_rule('/advertisements/<int:adv_id>',
                 view_func=AdvViews.as_view('advertisements'),
                 methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/advertisements/', view_func=AdvViews.as_view('create_adv'), methods=['POST'])

app.add_url_rule('/users/<int:user_id>',
                 view_func=OwnerViews.as_view('users'),
                 methods=['GET'])
app.add_url_rule('/users/',
                 view_func=OwnerViews.as_view('create_users'),
                 methods=['POST'])

app.run()

from os import environ, path
from flask import Flask, got_request_exception

import rollbar
import rollbar.contrib.flask

app = Flask(__name__)

@app.before_first_request
def init_rollbar():
    '''
    init rollbar module
    '''
    rollbar.init(
        environ.get('ROLLBAR_ACCESS_TOKEN'),
        'production',
        # Server root directory, makes tracebacks prettier
        root=path.dirname(path.realpath(__file__)),
        # Flask already sets up logging
        allow_logging_basic_config=False)

    # Send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

@app.route('/')
def hello_world():
    '''
    Return "Hello, World!"
    '''
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

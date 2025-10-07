from flask import Flask
import logging
import sys

app = Flask(__name__)

# Configure logging to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info('Hello Logger!')
    return '<html>Hello Logger!</html>'

if __name__ == '__main__':
    app.run()
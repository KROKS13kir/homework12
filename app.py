from flask import Flask

from main import main
from loader import loader


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

app.register_blueprint(main)
app.register_blueprint(loader)

app.run()

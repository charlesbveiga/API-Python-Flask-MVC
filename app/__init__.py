from .app_class import MyFlaskApp

_flask_app = MyFlaskApp()

app = _flask_app.app
db = _flask_app.db

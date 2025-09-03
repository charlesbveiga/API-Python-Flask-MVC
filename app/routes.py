from app.controllers.carro_controller import carros_bp

def register_routes(app):
    app.register_blueprint(carros_bp)

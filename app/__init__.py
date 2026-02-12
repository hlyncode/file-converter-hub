from flask import Flask
import os

def create_app():
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
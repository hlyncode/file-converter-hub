import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta'
    
    # Pasta para onde os arquivos enviados sobem
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    
    # Pasta onde os arquivos prontos ficarão (ADICIONE ESTA LINHA):
    CONVERTED_FOLDER = os.path.join(basedir, 'converted')
    
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
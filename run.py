"""
Executa o servidor Flask em modo desenvolvimento
"""
from app import create_app
import os 
app = create_app()
if __name__ == '__main__':
    print("=" * 50)
    print("🚀FILE CONVERTER HUB")
    print("=" * 50)
    print(f"📂 Pasta de uploads: {app.config['UPLOAD_FOLDER']}") 
    print(f"📂 Pasta de convertidos: {app.config['CONVERTED_FOLDER']}") 
    print("=" * 50) 
    print(f"🌐 Servidor rodando em: http://localhost:5000") 
    print(f"📝 Para parar: Ctrl+C")
    print("=" * 50)

    app.run (
        debug = True,
        host = '0.0.0.0',
        port = 5000,
        threaded = True 
    )

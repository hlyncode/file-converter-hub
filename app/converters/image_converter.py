from PIL import Image
import os 
from flask import current_app 
class ImageConverter:
    """conversor de imagens PDF""" 
    def __init__(self):
        """inicializa o conversor"""
    def image_to_pdf(self, input_path):
        try:
            image = Image.open(input_path)
            if image.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', image.size,(255,255,255))
                if image.mode == 'RGBA':
                    background.paste(image, mask=image.split()[3])
                else:
                    background.paste(image)
                image = background
            elif image.mode != 'RGB':
                image = image.convert('RGB')
            filename = os.path.basename(input_path)
            name_without_ext = os.path.splitext(filename)[0]
            output_filename = f"{name_without_ext}_converted.pdf"
            output_path = os.path.join(
                current_app.config['CONVERTED_FOLDER'],
                output_filename
)
            image.save(output_path, 'PDF', resolution=100.0)
            return output_path
        except Exception as e:
            raise Exception(f"Erro ao converter imagem para PDF: {str(e)}")
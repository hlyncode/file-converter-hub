"""
TESTES AUTOMATIZADOS - File Converter Hub
Testa cada conversor individualmente
"""
import unittest
import os
import sys
from io import BytesIO
from PIL import Image
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.converters.image_converter import ImageConverter
from app.converters.markdown_converter import MarkdownConverter
from app.converters.pdf_converter import PDFConverter
from app.converters.epub_converter import EPUBConverter

class TestImageConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = ImageConverter()
        self.test_image_path = 'test_image.png'
        img = Image.new('RGB', (100, 100), color='red')
        img.save(self.test_image_path)
    
    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
    
    def test_image_to_pdf(self):
        self.assertIsNotNone(self.converter)
        self.assertEqual(self.converter.supported_formats, ['.png', '.jpg', '.jpeg'])

class TestMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MarkdownConverter()
        self.test_md_path = 'test.md'
        with open(self.test_md_path, 'w', encoding='utf-8') as f:
            f.write('# Título\n\nEste é um parágrafo de teste.')
    
    def tearDown(self):
        if os.path.exists(self.test_md_path):
            os.remove(self.test_md_path)
    
    def test_markdown_instance(self):
        self.assertIsNotNone(self.converter)
        self.assertIsNotNone(self.converter.md)


class TestPDFConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = PDFConverter()
    
    def test_pdf_converter_instance(self):
        self.assertIsNotNone(self.converter)


class TestEPUBConverter(unittest.TestCase):
    def setUp(self):
        self.converter = EPUBConverter()
    
    def test_epub_converter_instance(self):
        self.assertIsNotNone(self.converter)
class TestFileValidation(unittest.TestCase):
    def test_allowed_extensions(self):
        from config import Config
        
        self.assertIn('.pdf', Config.ALLOWED_EXTENSIONS['pdf'])
        self.assertIn('.docx', Config.ALLOWED_EXTENSIONS['docx'])
        self.assertIn('.epub', Config.ALLOWED_EXTENSIONS['epub'])
        self.assertIn('.png', Config.ALLOWED_EXTENSIONS['image'])
        self.assertIn('.md', Config.ALLOWED_EXTENSIONS['markdown'])
    
    def test_conversion_types(self):
        from config import Config
        
        self.assertIn('pdf_to_docx', Config.CONVERSIONS)
        self.assertIn('image_to_pdf', Config.CONVERSIONS)
        self.assertIn('markdown_to_pdf', Config.CONVERSIONS)

if __name__ == '__main__':
    unittest.main(verbosity=2)
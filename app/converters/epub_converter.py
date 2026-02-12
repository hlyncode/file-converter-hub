import ebooklib 
from ebooklib import epub 
from bs4 import BeautifulSoup 
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet 
from PyPDF2 import PdfReader
import os 
from flask import current_app 

class EPUBConverter:
    def epub_to_pdf(self, input_path):
        try: 
            book = epub.read_epub(input_path) 
            filename = os.path.basename(input_path) 
            name_without_ext = os.path.splitext(filename)[0] 
            output_filename = f"{name_without_ext}_converted.pdf" 
            output_path = os.path.join(
                current_app.config['CONVERTED_FOLDER'],
                output_filename
            )

        
            pdf = SimpleDocTemplate(
                output_path, 
                pagesize=letter, 
                rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72
            )
            
        
            styles = getSampleStyleSheet()
            style_norm = styles['Normal']
            style_norm.alignment = 4  
            
            story = []
            
        
            title = book.get_metadata('DC', 'title')
            if title:
                story.append(Paragraph(title[0][0], styles['Title']))
                story.append(Spacer(1, 30))

            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                
                    soup = BeautifulSoup(item.get_content(), 'html.parser')
                    
                    for script in soup(["script", "style"]):
                        script.decompose()
                    
                    text = soup.get_text()
                    
                    if text.strip():
                        for para in text.split('\n'):
                            if para.strip():
                                p = Paragraph(para.strip(), style_norm)
                                story.append(p)
                                story.append(Spacer(1, 12))
                        story.append(PageBreak())

            pdf.build(story)
            return output_path
        except Exception as e:
            raise Exception(f"Erro ao converter EPUB para PDF: {str(e)}")

    def pdf_to_epub(self, input_path):
        try:
            reader = PdfReader(input_path)
            book = epub.EpubBook()
            filename = os.path.basename(input_path)
            name_without_ext = os.path.splitext(filename)[0]
            
            book.set_identifier(f'id_{name_without_ext}')
            book.set_title(name_without_ext)
            book.set_language('pt')
            
            chapters = []
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                if text.strip():
                    chapter = epub.EpubHtml(
                        title=f'Página {page_num}',
                        file_name=f'page_{page_num}.xhtml',
                        lang='pt'
                    )        
                    
                    html_content = f'<h1>Página {page_num}</h1>'
                    for para in text.split('\n\n'):
                        if para.strip():
                            html_content += f'<p>{para.strip()}</p>'
                    
                    chapter.set_content(html_content)
                    book.add_item(chapter)
                    chapters.append(chapter)

            book.toc = chapters 
            book.spine = ['nav'] + chapters 
            book.add_item(epub.EpubNcx())
            book.add_item(epub.EpubNav())
            
            output_filename = f"{name_without_ext}_converted.epub"
            output_path = os.path.join(current_app.config['CONVERTED_FOLDER'], output_filename)
            
            epub.write_epub(output_path, book)
            return output_path 
        except Exception as e:
            raise Exception(f"Erro ao converter PDF para EPUB: {str(e)}")
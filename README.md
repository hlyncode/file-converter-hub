# File Converter Hub

> Conversor profissional de arquivos com interface web moderna

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Sobre o Projeto

**File Converter Hub** é uma aplicação web full-stack desenvolvida em Python/Flask que permite conversão entre múltiplos formatos de arquivo de forma rápida, segura e intuitiva.

### Características

- ✅ **Interface Moderna**: Design responsivo com drag-and-drop
- ✅ **Múltiplos Formatos**: PDF, DOCX, EPUB, Imagens, Markdown
- ✅ **Arquitetura Limpa**: Código organizado e escalável
- ✅ **Segurança**: Validação de arquivos e limpeza automática
- ✅ **Feedback Visual**: Barra de progresso e animações suaves

## Formatos Suportados

### Conversões Disponíveis

| De | Para | Status |
|---|---|---|
| PDF | DOCX | ✅ |
| PDF | EPUB | ✅ |
| DOCX | PDF | ✅ |
| EPUB | PDF | ✅ |
| PNG/JPG | PDF | ✅ |
| Markdown | PDF | ✅ |
| Markdown | DOCX | ✅ |

## Tecnologias Utilizadas

### Backend
- **Python 3.8+**: Linguagem principal
- **Flask**: Framework web
- **PyPDF2**: Manipulação de PDFs
- **python-docx**: Manipulação de DOCX
- **ebooklib**: Manipulação de EPUB
- **Pillow**: Processamento de imagens
- **ReportLab**: Geração de PDFs

### Frontend
- **HTML5**: Estrutura semântica
- **CSS3**: Design moderno com variáveis CSS
- **JavaScript (Vanilla)**: Interatividade sem frameworks
- **Drag & Drop API**: Upload intuitivo

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional)

### Passo a Passo

1. **Clone o repositório** (ou baixe o ZIP)
```bash
git clone https://github.com/seu-usuario/file-converter-hub.git
cd file-converter-hub
```

2. **Crie um ambiente virtual** (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
python run.py
```

5. **Acesse no navegador**
```
http://localhost:5000
```

## Como Usar

1. **Faça upload** do arquivo arrastando ou clicando
2. **Escolha** o formato de saída desejado
3. **Aguarde** a conversão (poucos segundos)
4. **Baixe** o arquivo convertido

### Exemplo em vídeo

![Demo](docs/demo.gif)
*Arraste, converta, baixe - simples assim!*

## Estrutura do Projeto

file-converter-hub/
│
├── app/
│   ├── __init__.py              # Factory da aplicação
│   ├── routes.py                # Endpoints da API
│   │
│   ├── converters/              # Lógica de conversão
│   │   ├── __init__.py
│   │   ├── pdf_converter.py    # Conversões PDF
│   │   ├── epub_converter.py   # Conversões EPUB
│   │   ├── image_converter.py  # Conversões Imagem
│   │   └── markdown_converter.py
│   │
│   ├── static/                  # Arquivos estáticos
│   │   ├── css/
│   │   │   └── style.css       # Estilos
│   │   └── js/
│   │       └── app.js          # JavaScript
│   │
│   └── templates/               # Templates HTML
│       └── index.html
│
├── uploads/                     # Upload temporário
├── converted/                   # Arquivos convertidos
├── tests/                       # Testes automatizados
│
├── config.py                    # Configurações
├── run.py                       # Ponto de entrada
├── requirements.txt             # Dependências
├── .gitignore
└── README.md
```

---

## 🧪 Testes

Execute os testes automatizados:
```bash
# Com unittest
python tests/test_converters.py

# Com pytest (mais detalhado)
pip install pytest
pytest tests/ -v
```

---

## Segurança

- ✅ Validação de tipo e tamanho de arquivo
- ✅ Nome de arquivo sanitizado (previne path traversal)
- ✅ Limpeza automática de arquivos temporários
- ✅ Limite de 16MB por arquivo
- ✅ Extensões restritas por whitelist

## 🚀 Deploy

### Opção 1: Heroku
```bash
# Crie um Procfile
echo "web: gunicorn run:app" > Procfile

# Deploy
heroku create meu-conversor
git push heroku main
```

### Opção 2: PythonAnywhere

1. Faça upload dos arquivos
2. Configure WSGI file apontando para `run:app`
3. Reload da aplicação

### Opção 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
```

## Customização

### Alterar cores do tema

Edite as variáveis CSS em `app/static/css/style.css`:
```css
:root {
    --primary: #6366f1;        /* Cor principal */
    --primary-dark: #4f46e5;   /* Hover */
    --success: #10b981;        /* Sucesso */
}
```

### Adicionar novo formato

1. Crie conversor em `app/converters/`
2. Adicione extensão em `config.py`
3. Registre conversão em `conversionOptions` (app.js)

## Roadmap

- [ ] Conversão em lote (múltiplos arquivos)
- [ ] API REST pública com autenticação
- [ ] OCR para PDFs escaneados
- [ ] Compressão de arquivos
- [ ] Histórico de conversões
- [ ] Tema escuro

## Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

**Hellen**

- GitHub: [@hlyncode](https://github.com/hlyncode)
- Email: hlyncode@gmail.com

---

## Agradecimentos

- Comunidade Python
- Documentação do Flask
- Bibliotecas de código aberto utilizadas

## Status do Projeto

> **Versão 1.0** - Funcional e pronto para produção

**Última atualização**: Fevereiro 2026

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela!**

</div>
```

---

## **ARQUIVO: LICENSE**
```
MIT License

Copyright (c) 2026 Hellen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

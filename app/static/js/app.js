const state = {
    selectedFile: null,
    selectedConversion: null,
    downloadUrl: null
};
const extensionToType = {
    'pdf': 'pdf',
    'docx': 'docx',
    'doc': 'docx',
    'epub': 'epub',
    'png': 'image',
    'jpg': 'image',
    'jpeg': 'image',
    'md': 'markdown',
    'markdown': 'markdown'
}; 
const conversionOptions = {
    'pdf': [
        { type: 'pdf_to_docx', icon: '📝', title: 'Para DOCX', description: 'Documento Word editável' },
        { type: 'pdf_to_epub', icon: '📚', title: 'Para EPUB', description: 'E-book digital' }
    ],
    'docx': [
        { type: 'docx_to_pdf', icon: '📄', title: 'Para PDF', description: 'Documento portátil' }
    ],
    'epub': [
        { type: 'epub_to_pdf', icon: '📄', title: 'Para PDF', description: 'Documento portátil' }
    ],
    'image': [
        { type: 'image_to_pdf', icon: '📄', title: 'Para PDF', description: 'Imagem em documento' }
    ],
    'markdown': [
        { type: 'markdown_to_pdf', icon: '📄', title: 'Para PDF', description: 'Documento formatado' },
        { type: 'markdown_to_docx', icon: '📝', title: 'Para DOCX', description: 'Documento Word' }
    ]
};
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
});

function initializeEventListeners() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const btnRemove = document.getElementById('btnRemove');
    const btnNewConversion = document.getElementById('btnNewConversion');
    fileInput.addEventListener('change', handleFileSelect);
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    btnRemove.addEventListener('click', resetApp);
    btnNewConversion.addEventListener('click', resetApp);
}
function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file);
    }
}
function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    document.getElementById('uploadArea').classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    document.getElementById('uploadArea').classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    document.getElementById('uploadArea').classList.remove('dragover');
    
    const file = e.dataTransfer.files[0];
    if (file) {
        processFile(file);
    }
}

function processFile(file) {
    const maxSize = 16 * 1024 * 1024;
    if (file.size > maxSize) {
        alert('Arquivo muito grande! Tamanho máximo: 16MB');
        return;
    }
    const extension = file.name.split('.').pop().toLowerCase();
    const fileType = extensionToType[extension];

    if (!fileType) {
        alert('Tipo de arquivo não suportado!');
        return;
    }
    state.selectedFile = file;
    state.selectedConversion = null;
    showFilePreview(file);
    showConversionOptions(fileType);
}

function showFilePreview(file) {
    document.getElementById('uploadArea').style.display = 'none';
    
    const preview = document.getElementById('filePreview');
    document.getElementById('fileName').textContent = file.name;
    document.getElementById('fileSize').textContent = formatFileSize(file.size);
    preview.style.display = 'block';
}

function showConversionOptions(fileType) {
    const options = conversionOptions[fileType];
    const grid = document.getElementById('conversionGrid');
    grid.innerHTML = '';

    options.forEach(option => {
        const div = document.createElement('div');
        div.className = 'conversion-option';
        div.innerHTML = `
            <div class="icon">${option.icon}</div>
            <h4>${option.title}</h4>
            <p>${option.description}</p>
        `;
        div.onclick = () => selectConversion(option.type, div);
        grid.appendChild(div);
    });

    document.getElementById('conversionSection').style.display = 'block';
}

function selectConversion(conversionType, element) {
    document.querySelectorAll('.conversion-option').forEach(el => {
        el.classList.remove('selected');
    });
    element.classList.add('selected');
    state.selectedConversion = conversionType;
    setTimeout(() => {
        startConversion();
    }, 500);
}
async function startConversion() {
    document.getElementById('conversionSection').style.display = 'none';
    showProgress();
    const formData = new FormData();
    formData.append('file', state.selectedFile);
    formData.append('conversion_type', state.selectedConversion);

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok && result.success) {
            state.downloadUrl = result.download_url;
            showResult(result);
        } else{
            throw new Error(result.error || 'Erro desconhecido');
        }
    } catch (error) {
        hideProgress();
        alert('Erro na conversão: ' + error.message);
        resetApp();
    }
}

function showProgress() {
    const progressSection = document.getElementById('progressSection');
    progressSection.style.display = 'block';
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 30;
        if (progress > 90) progress = 90;
        
        document.getElementById('progressFill').style.width = progress + '%';
        
        if (progress >= 90) {
            clearInterval(interval);
        }
    }, 300);
    state.progressInterval = interval;
}

function hideProgress() {
    if (state.progressInterval) {
        clearInterval(state.progressInterval);
    }
    document.getElementById('progressSection').style.display = 'none';
}

function showResult(result) {
    hideProgress();
    document.getElementById('progressFill').style.width = '100%';
    setTimeout(() => {
        document.getElementById('progressSection').style.display = 'none';
    }, 500);
    document.getElementById('resultMessage').textContent = 
        `Arquivo "${result.filename}" pronto para download!`;
    
    document.getElementById('btnDownload').onclick = () => {
        window.location.href = result.download_url;
    };

    document.getElementById('resultSection').style.display = 'block';
}
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

function resetApp() {
    state.selectedFile = null;
    state.selectedConversion = null;
    state.downloadUrl = null;
    document.getElementById('fileInput').value = '';
    document.getElementById('filePreview').style.display = 'none';
    document.getElementById('conversionSection').style.display = 'none';
    document.getElementById('progressSection').style.display = 'none';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('uploadArea').style.display = 'block';
}
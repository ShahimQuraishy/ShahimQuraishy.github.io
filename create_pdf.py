#!/usr/bin/env python3
import weasyprint
from pathlib import Path

def create_pdf():
    html_path = Path("index.html")
    pdf_path = Path("lebenslauf.pdf")
    
    # HTML-Datei lesen
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # CSS für PDF-Anpassung hinzufügen
    pdf_css = """
    @page {
        size: A4;
        margin: 1.5cm;
    }
    
    /* Chatbot und andere nicht-druckbare Elemente ausblenden */
    #cw, .lang-switch {
        display: none !important;
    }
    
    /* Druckoptimierungen */
    body {
        background: #fff !important;
        font-size: 10pt;
        line-height: 1.4;
    }
    
    .page {
        max-width: none;
        padding: 0;
        margin: 0;
    }
    
    .header-banner {
        border-radius: 0;
        margin-bottom: 20px;
    }
    
    .body-grid {
        grid-template-columns: 300px 1fr;
        box-shadow: none;
        border-radius: 0;
        border: 1px solid #e2e8f0;
    }
    
    .sidebar {
        border-right: 1px solid #e2e8f0;
    }
    
    .main {
        padding: 20px;
    }
    
    .tl-card {
        page-break-inside: avoid;
        margin-bottom: 12px;
    }
    
    .sec-hd {
        page-break-after: avoid;
        margin-top: 20px;
    }
    
    /* Schriftgrößen für PDF anpassen */
    h1 { font-size: 24pt; }
    .hb-role { font-size: 9pt; }
    .hb-bio { font-size: 9pt; }
    .tl-title { font-size: 11pt; }
    .tl-body { font-size: 9pt; }
    .tag { font-size: 8pt; }
    .pill { font-size: 8pt; }
    """
    
    # PDF erstellen
    html_doc = weasyprint.HTML(string=html_content, base_url=str(html_path.parent))
    css = weasyprint.CSS(string=pdf_css)
    
    html_doc.write_pdf(pdf_path, stylesheets=[css])
    print(f"PDF erstellt: {pdf_path}")

if __name__ == "__main__":
    create_pdf()

#!/usr/bin/env python3
import subprocess
import sys
import os

def create_pdf_with_chrome():
    """PDF mit Chrome/Chromium erstellen, falls verfügbar"""
    try:
        # Prüfen ob Chrome oder Chromium verfügbar ist
        chrome_paths = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            '/Applications/Chromium.app/Contents/MacOS/Chromium',
            '/usr/bin/google-chrome',
            '/usr/bin/chromium-browser'
        ]
        
        chrome_cmd = None
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_cmd = path
                break
        
        if not chrome_cmd:
            print("Kein Chrome/Chromium gefunden. Versuche alternativen Ansatz...")
            return False
        
        # PDF mit Chrome erstellen
        cmd = [
            chrome_cmd,
            '--headless',
            '--disable-gpu',
            '--print-to-pdf=lebenslauf.pdf',
            '--print-to-pdf-no-header',
            '--virtual-time-budget=5000',
            'file:///Users/shahimquraishy/My Drive/GithubClone/ShahimQuraishy.github.io/index.html'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0 and os.path.exists('lebenslauf.pdf'):
            print("PDF erfolgreich mit Chrome erstellt!")
            return True
        else:
            print(f"Chrome Fehler: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Fehler bei Chrome-Methode: {e}")
        return False

def create_pdf_with_safari():
    """PDF mit Safari über AppleScript erstellen"""
    try:
        applescript = '''
        tell application "Safari"
            activate
            set URL of front document to "file:///Users/shahimquraishy/My Drive/GithubClone/ShahimQuraishy.github.io/index.html"
            delay 3
            tell application "System Events"
                keystroke "p" using command down
                delay 2
                keystroke "PDF" using command down
                delay 1
                keystroke return
                delay 2
                click menu button "Drucken" of window "Drucken"
                delay 1
                click menu button "PDF" of sheet 1 of window "Drucken"
                delay 1
                click menu item "Als PDF sichern" of menu "PDF" of menu button "PDF" of sheet 1 of window "Drucken"
                delay 2
                keystroke "lebenslauf.pdf"
                delay 1
                click button "Sichern" of sheet 1 of window "Drucken"
            end tell
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("PDF-Erstellung mit Safari gestartet (manuell bestätigen)")
            return True
        else:
            print(f"Safari Fehler: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Fehler bei Safari-Methode: {e}")
        return False

def create_simple_html_pdf():
    """Einfache HTML-Version ohne komplexe CSS für PDF erstellen"""
    html_content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Shahim Quraishy - Lebenslauf</title>
    <style>
        @page { margin: 1.5cm; }
        body { font-family: Arial, sans-serif; font-size: 10pt; line-height: 1.4; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #2563eb; padding-bottom: 10px; }
        .name { font-size: 18pt; font-weight: bold; margin-bottom: 5px; }
        .contact { font-size: 9pt; margin-bottom: 10px; }
        .section { margin-bottom: 15px; }
        .section-title { font-size: 12pt; font-weight: bold; color: #2563eb; margin-bottom: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 3px; }
        .item { margin-bottom: 10px; }
        .item-title { font-weight: bold; font-size: 10pt; }
        .item-subtitle { font-style: italic; font-size: 9pt; color: #666; }
        .item-content { font-size: 9pt; margin-top: 3px; }
        .skills { display: flex; flex-wrap: wrap; gap: 3px; }
        .skill { background: #f0f4f8; padding: 2px 6px; border-radius: 3px; font-size: 8pt; }
        .two-column { display: flex; gap: 20px; }
        .column { flex: 1; }
    </style>
</head>
<body>
    <div class="header">
        <div class="name">Shahim Quraishy</div>
        <div class="contact">📍 Hillscheiderstr. 9, 56179 Vallendar | 📱 +49 1525 8414 768 | ✉️ quraishyshahim@icloud.com</div>
        <div class="contact">🔗 LinkedIn: shahim-quraishy | 💻 GitHub: github.com/ShahimQuraishy</div>
        <div><strong>Cloud & DevSecOps Enthusiast</strong> · Fokus: Inhouse Cloud & KI · Uni Koblenz</div>
    </div>

    <div class="two-column">
        <div class="column">
            <div class="section">
                <div class="section-title">🎯 Profil</div>
                <div class="item-content">
                    Als Informatikstudent an der Uni Koblenz begeistere ich mich für Cloud-Infrastrukturen, DevSecOps und Künstliche Intelligenz. In eigenen Projekten (wie meinem EXIST-Gründungsvorhaben) und Nebenjobs habe ich praxisnah gelernt, wie man sichere, containerisierte Backend-Systeme aufbaut und automatisiert deployt (Docker, CI/CD, AWS).
                </div>
            </div>

            <div class="section">
                <div class="section-title">🚀 DevSecOps & KI-Projekte</div>
                <div class="item">
                    <div class="item-title">Plattform-Infrastruktur "hilfefuersenioren"</div>
                    <div class="item-subtitle">EXIST-Gründungsvorhaben · DevSecOps Fokus · Seit 09/2025</div>
                    <div class="item-content">
                        • Voice-First-Architektur vernetzt Senioren per Telefon mit Dienstleistern<br>
                        • DSGVO-konforme, containerisierte Architektur (Docker) für Node.js/PostgreSQL-Backend<br>
                        • Automatisierte CI/CD-Pipeline inkl. Security-Scans für sicheres Deployment
                    </div>
                    <div class="skills">
                        <span class="skill">Docker</span><span class="skill">CI/CD</span><span class="skill">Node.js</span><span class="skill">PostgreSQL</span><span class="skill">DSGVO</span>
                    </div>
                </div>
                <div class="item">
                    <div class="item-title">Lokales RAG-Wissenssystem für Pflege</div>
                    <div class="item-subtitle">Eigenentwicklung · Python · LangChain · ChromaDB</div>
                    <div class="item-content">
                        • RAG-Pipeline mit Text-Chunking und lokalen Vektor-Embeddings<br>
                        • Kontextnahe Antworten ohne Datenabfluss (DSGVO-konform)<br>
                        • Funktionsfähiger Prototyp auf GitHub
                    </div>
                    <div class="skills">
                        <span class="skill">Python</span><span class="skill">LangChain</span><span class="skill">ChromaDB</span><span class="skill">Local-LLM</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">💼 Berufserfahrung</div>
                <div class="item">
                    <div class="item-title">Studentische Hilfskraft – Green Office</div>
                    <div class="item-subtitle">Nachhaltigkeit & Digitalisierung · Universität Koblenz · Seit 02/2026</div>
                    <div class="item-content">
                        • Unterstützung der digitalen Kommunikation und Pflege von Inhalten<br>
                        • Mitarbeit bei Planung und Dokumentation von Events
                    </div>
                </div>
                <div class="item">
                    <div class="item-title">Werkstudent – Development Business Systems</div>
                    <div class="item-subtitle">1&1 Telecommunication SE · Montabaur · 11/2024 – 04/2025</div>
                    <div class="item-content">
                        • Automatisierungsskripte (Python/SQL) zur Datenbankbereinigung<br>
                        • Bugfixing, Unit-Tests und Code-Optimierungen<br>
                        • Erstellung komplexer SQL-Abfragen und technischer Dokumentationen
                    </div>
                    <div class="skills">
                        <span class="skill">SQL</span><span class="skill">Python</span><span class="skill">Automatisierung</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="column">
            <div class="section">
                <div class="section-title">🔧 Core Skills</div>
                <div class="item-content">
                    <strong>Cloud & DevOps:</strong> Docker, CI/CD-Pipelines, AWS (EC2, S3, Lambda), Azure, Git, Terraform (Basis)<br><br>
                    <strong>KI & Machine Learning:</strong> RAG-Systeme, LLMs/GPT-4, Prompt Engineering, Deep Learning, Embeddings<br><br>
                    <strong>Programmierung:</strong> Python, Java/OOP, JavaScript/Node.js, SQL, HTML/CSS<br><br>
                    <strong>Datenbanken & Web:</strong> PostgreSQL, ChromaDB, REST/GraphQL
                </div>
            </div>

            <div class="section">
                <div class="section-title">🎓 Ausbildung & Zertifizierung</div>
                <div class="item">
                    <div class="item-title">Zertifizierter Agiler Junior Softwareentwickler – KI-Fokus</div>
                    <div class="item-subtitle">BPU GmbH · Koblenz · 09/2024 – 08/2025</div>
                    <div class="item-content">
                        AWS CLF-C02 & Azure AZ-900 • Cloud Security & DSGVO • Systemarchitektur & Microservices • KI & Machine Learning
                    </div>
                </div>
                <div class="item">
                    <div class="item-title">B.Sc. Informatik (Nebenfach: Wirtschaftsinformatik)</div>
                    <div class="item-subtitle">Universität Koblenz · Seit 10/2021 • Abschluss voraussichtlich 04/2027</div>
                    <div class="item-content">
                        Algorithmen & Datenstrukturen • Softwaretechnik • Datenbanken • Betriebssysteme • Webentwicklung • Projektmanagement
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">🌐 Sprachen</div>
                <div class="item-content">
                    <strong>Deutsch:</strong> C1–C2 · Fließend<br>
                    <strong>Englisch:</strong> B2 · Gut<br>
                    <strong>Französisch:</strong> A2–B1 · Grundkenntnisse
                </div>
            </div>

            <div class="section">
                <div class="section-title">🏆 Zertifizierungen</div>
                <div class="item-content">
                    • AWS CLF-C02 Cloud Practitioner<br>
                    • Azure AZ-900 Fundamentals<br>
                    • KI & Agile Development (BPU GmbH)
                </div>
            </div>

            <div class="section">
                <div class="section-title">⚙️ Methodik</div>
                <div class="skills">
                    <span class="skill">Scrum</span><span class="skill">Kanban</span><span class="skill">DSGVO-Compliance</span><span class="skill">Unit-Testing</span><span class="skill">Microservices</span>
                </div>
            </div>
        </div>
    </div>

    <div class="section" style="margin-top: 20px; text-align: center; font-size: 8pt; color: #666;">
        Verfügbar: ab sofort als Werkstudent (Cloud/DevOps/AI) · Vollzeit ab 2027 · Remote & Rhein-Main/RLP möglich<br>
        Führerschein Klasse B vorhanden
    </div>
</body>
</html>'''

    with open('lebenslauf_fuer_pdf.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Versuche mit Chrome
    if create_pdf_with_chrome():
        return True
    
    print("Erstelle einfache HTML-Datei für manuelle PDF-Erstellung: lebenslauf_fuer_pdf.html")
    print("Bitte öffnen Sie diese Datei im Browser und speichern Sie als PDF (Cmd+P → Als PDF speichern)")
    return False

if __name__ == "__main__":
    print("Erstelle Lebenslauf als PDF...")
    
    if create_simple_html_pdf():
        print("PDF erfolgreich erstellt: lebenslauf.pdf")
    else:
        print("Bitte erstellen Sie das PDF manuell aus der generierten HTML-Datei.")

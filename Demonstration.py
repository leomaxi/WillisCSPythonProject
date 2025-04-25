# Python script to simulate an advanced, gamified, and comprehensive portfolio website for Leonard M. I. Mensah

import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class PortfolioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        questions = [
            {"question": "Which port is used by HTTPS?", "answers": ["443", "22"], "correct": 0},
            {"question": "What does SIEM stand for?", "answers": ["Security Information and Event Management", "Secure Internet Email Management"], "correct": 0},
            {"question": "What protocol does SSH use?", "answers": ["TCP", "UDP"], "correct": 0},
            {"question": "Which tool is best for vulnerability scanning?", "answers": ["Nessus", "Notepad"], "correct": 0},
            {"question": "What layer of the OSI model is IP?", "answers": ["Network", "Transport"], "correct": 0},
            {"question": "Which is a hashing algorithm?", "answers": ["SHA-256", "AES"], "correct": 0},
            {"question": "What does GDPR protect?", "answers": ["Personal Data", "Server Logs"], "correct": 0},
            {"question": "What is the main function of a firewall?", "answers": ["Block unauthorized access", "Provide storage"], "correct": 0},
            {"question": "Which of these is an example of 2FA?", "answers": ["Password + SMS code", "Username only"], "correct": 0},
            {"question": "Which tool is commonly used for penetration testing?", "answers": ["Metasploit", "Excel"], "correct": 0}
        ]

        random.shuffle(questions)

        quiz_html = ''.join(f'''
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h3>{q['question']}</h3>
                    </div>
                    <div class="flip-card-back">
                        {''.join([f'<button onclick="alert(\'{"✔ Correct!" if i==q["correct"] else "✘ Incorrect!"}\')">{ans}</button>' for i, ans in enumerate(q['answers'])])}
                    </div>
                </div>
            </div>
        ''' for q in questions[:10])

        html_content = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Leonard M. I. Mensah | Cybersecurity Portfolio</title>
            <style>
                body {{
                    background: radial-gradient(circle, #111 0%, #000 100%);
                    color: #0ff;
                    font-family: 'Courier New', Courier, monospace;
                    margin: 0;
                    padding: 40px;
                    animation: fadeIn 2s ease-in-out;
                }}
                h1, h2 {{ text-align: center; }}
                .section {{ padding: 20px; margin-bottom: 30px; background: #111; border-radius: 10px; border: 1px solid #0ff; }}
                button {{
                    background: #0ff;
                    border: none;
                    padding: 10px 20px;
                    margin: 5px;
                    color: #000;
                    font-weight: bold;
                    cursor: pointer;
                    border-radius: 5px;
                }}
                button:hover {{ background: #0aa; }}
                .flip-card {{
                    background-color: transparent;
                    width: 300px;
                    height: 200px;
                    perspective: 1000px;
                    display: inline-block;
                    margin: 10px;
                }}
                .flip-card-inner {{
                    position: relative;
                    width: 100%;
                    height: 100%;
                    transition: transform 0.6s;
                    transform-style: preserve-3d;
                }}
                .flip-card:hover .flip-card-inner {{
                    transform: rotateY(180deg);
                }}
                .flip-card-front, .flip-card-back {{
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    backface-visibility: hidden;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 10px;
                    box-sizing: border-box;
                    border: 2px solid #00ffcc;
                    border-radius: 10px;
                }}
                .flip-card-front {{
                    background-color: #111;
                    color: white;
                }}
                .flip-card-back {{
                    background-color: #222;
                    color: white;
                    transform: rotateY(180deg);
                    flex-direction: column;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
            </style>
        </head>
        <body>
            <h1>Leonard M. I. Mensah</h1>
            <h2>Cybersecurity & IT Operations Professional</h2>
            <div class="section">
                <h3>About Me</h3>
                <p>Versatile and dynamic cybersecurity professional with a background spanning IT infrastructure, threat mitigation, instructional design, application development, and global tech leadership roles. Passionate about securing systems and empowering communities through tech education.</p>
            </div>
            <div class="section">
                <h3>Professional Experience</h3>
                <p><strong>AVASO Technology Solutions (11/2024 - Present):</strong> Level 1/2 support, imaging, IMACD, field service, software installations, patching, documentation.</p>
                <p><strong>Atunwa Digital (08/2023 - 05/2024):</strong> Threat monitoring, SIEM, vulnerability scanning, security training, authentication controls, security automation.</p>
                <p><strong>Pellucid Technology (02/2014 - 09/2023):</strong> CTO, secure IT operations, client support, cybersecurity training, 42+ applications delivered, policy development.</p>
                <p><strong>Open Learning Exchange Int. (10/2017 – 02/2021):</strong> Tech-Lead Africa, Raspberry Pi deployment, Android LMS, intern supervision, secure platform development.</p>
                <p><strong>Jhpiego (01/2015 – 09/2017):</strong> Digital Health Officer, LMS implementation, IT training, automated SMS systems, data collection & recovery systems.</p>
            </div>
            <div class="section">
                <h3>Interactive Quiz</h3>
                {quiz_html}
            </div>
        </body>
        </html>
        '''

        self.wfile.write(html_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=PortfolioHandler):
    try:
        server_address = ('127.0.0.1', 8082)
        httpd = server_class(server_address, handler_class)
        print("Launching Leonard's gamified portfolio at http://127.0.0.1:8082")
        webbrowser.open('http://127.0.0.1:8082')
        httpd.serve_forever()
    except Exception as e:
        print(f"Failed to launch server: {e}")

if __name__ == '__main__':
    run()

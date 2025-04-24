# XSS Vulnerability Demonstration  

A project showcasing Cross-Site Scripting (XSS) attacks, payload injection, and mitigation using Content Security Policy (CSP).  

## **📌 Features**  
- **Stored XSS Demo**: Malicious script injection via a search form.  
- **Cookie Theft**: Captures browser cookies using a Flask server.  
- **Phishing Simulation**: Fake login page to steal credentials.  
- **CSP Protection**: Implementation to block inline scripts.  

## **⚙️ Setup**  
1. **Run the Capture Server**:  
   ```bash
   python capture_server.py
Test Payloads:
Open payload.html or test.html to trigger XSS.
Use index.html to simulate credential theft.

🛡️ Prevention
CSP Header: Added in Flask to restrict script sources:
response.headers["Content-Security-Policy"] = "script-src 'self'"

📂 Files
File	             Purpose
payload.html	     XSS payload to steal cookies.
capture_server.py	 Flask server to log stolen data.
index.html	       Fake login page (phishing).
test.html	         Search form with XSS payload.

⚠️ Disclaimer
For educational purposes only. Use responsibly and only on systems you own.

📜 License
MIT

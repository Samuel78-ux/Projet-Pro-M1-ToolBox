from flask import Flask, render_template, request
import nmap

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scan_ports', methods=['GET', 'POST'])
def scan_ports():
    if request.method == 'POST':
        target_host = request.form['target_host']

        # Utilisez la plage de ports 1-65535 pour scanner tous les ports
        target_ports = "1-500"

        nm = nmap.PortScanner()
        result = nm.scan(target_host, target_ports)
        print(result)
        # Vous pouvez maintenant traiter les résultats du scan ici
        return render_template('scan_result.html', result=result)
    return render_template('scan_ports.html')


if __name__ == '__main__':
    app.run(debug=True)

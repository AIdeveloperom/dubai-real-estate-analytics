from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def root():
    # Serve index.html from repo root
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # Serve any other static asset from the repo
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return send_from_directory(directory or '.', filename)
    return ("Not found", 404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)

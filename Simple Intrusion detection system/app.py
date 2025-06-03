from flask import Flask, render_template, send_file, redirect, url_for
from flask_socketio import SocketIO
import ids  # Import your IDS code

app = Flask(__name__)
socketio = SocketIO(app)

# Start the IDS when app starts
ids.start_ids(socketio)

@app.route('/')
def index():
    logs = []
    try:
        with open('detector.log', 'r') as f:
            logs = f.readlines()
    except FileNotFoundError:
        pass
    return render_template('index.html', logs=logs)

@app.route('/download')
def download_logs():
    return send_file('detector.log', as_attachment=True)

@app.route('/clear')
def clear_logs():
    open('detector.log', 'w').close()  # Clear the file
    return redirect(url_for('index'))

if __name__ == '__main__':
    socketio.run(app, debug=True)

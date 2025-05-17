from datetime import datetime
from flask import Flask, render_template, request, redirect

SUGGESTION_FILE = 'suggestions.txt'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/problems/eggDrop')
def egg_drop():
    return render_template('problems/eggDrop.html')

@app.route('/misc/suggest', methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        reason = request.form.get('reason', '').strip()
        timestamp = datetime.now().isoformat()

        # Ensure suggestion is not empty
        if name:
            with open(SUGGESTION_FILE, 'a', encoding='utf-8') as f:
                f.write(f"{timestamp} | {name} | {reason}\n")

        return render_template('misc/suggest.html', success=True)

    return render_template('misc/suggest.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import os

app = Flask(__name__)

# Path to your content folder
CONTENT_DIR = os.path.join(os.path.dirname(__file__), 'content')

@app.route('/')
def index():
    # List all files in the content directory
    files = os.listdir(CONTENT_DIR)
    file_data = []
    for file in files:
        file_path = os.path.join(CONTENT_DIR, file)
        if file.endswith('.txt'):
            with open(file_path, 'r') as f:
                content = f.read()
        else:
            content = None  # For non-text files, we'll just link them
        file_data.append({'name': file, 'content': content})
    return render_template('index.html', files=file_data)

if __name__ == '__main__':
    app.run(debug=True)
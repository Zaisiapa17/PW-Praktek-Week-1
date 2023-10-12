from flask import Flask, render_template

# main app
app = Flask(__name__)

@app.route('/')
def index():
    teks = """
    Nama : mushyafa ali
    npm : 5220411358
    """
    return teks

if __name__ == '__main__':
    app.run(debug=True)
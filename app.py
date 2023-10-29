from flask import Flask, render_template


# Initialize the Flask app
app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

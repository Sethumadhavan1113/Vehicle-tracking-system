from flask import Flask, render_template, request


# Initialize the Flask app
app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/track',methods=["POST"])
def home():
    track = request.form['Vehicleno']
    print(track)
    if track == 'yes':
        
        return render_template('index.html', data = "Data recieved")
    else:
        return render_template('index.html', data = "Data not recieved")
 
if __name__ == '__main__':
    app.run(debug=True)

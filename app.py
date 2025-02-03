from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
   return 'Web App with Python Flask!'

@app.route('/formulaire')
def pageHtml():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return str(query)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True)
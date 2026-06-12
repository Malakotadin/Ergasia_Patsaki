from flask import Flask,redirect, url_for, jsonify,request
app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():
    content = request.json
    #return render_template("homepage.html")
    return content ['name']
if __name__=="__main__":
    app.run()

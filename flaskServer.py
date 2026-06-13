from flask import Flask,redirect, url_for, jsonify, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

#def home():
#    content = request.json
    #return render_template("homepage.html")
#    return content ['name']

def handle_request():
    # The GET endpoint
    if request.method == "GET":
        return "This is the GET Endpoint of flask API."
        #return "Im a sad lonely faggot"
    
    # The POST endpoint
    if request.method == "POST":
    
        response=request.get_json()
        fin_output = response.get('encoded_image', '')
        #fin_output= response.encoded_image
        #response=request.json
        #print(response)

        with open("output.bmp","wb") as file:
            file.write(bytes.fromhex(fin_output))

        #cap_text= response.upper()
        #response = {'cap-text': cap_text}

        # return the response as JSON
        return jsonify(response)
    
    
if __name__=="__main__":
    app.run(host="192.168.2.8", port="5000")

'''
@app.route("/", methods=["GET"])
def handle_get():
    # The GET endpoint
  
    return "This is the GET Endpoint of flask API."
    
   
    
@app.route("/", methods=["POST"])
def handle_post():
    response=request.get_json()
    return jsonify(response)

'''
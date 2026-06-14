from flask import Flask,redirect, url_for, jsonify, request
import subprocess
import CallTest

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

def handle_request():
    # The GET endpoint
    if request.method == "GET":
        return "This is the GET Endpoint of flask API."
    
    # The POST endpoint
    if request.method == "POST":
    
        response=request.get_json()
        fin_output = response.get('encoded_image', '')
        
        with open("servertag", "wb") as file:
            file.write(fin_output)
        arg1="servertag"
        subprocess.call(['python', 'sumpiesh\map_wdecode.py', arg1])

        #with open("output.bmp","wb") as file:
            #file.write(bytes.fromhex(fin_output))

        subprocess.call(['python', 'CallTest.py'])
   

        # return the response as JSON
        return jsonify(response)
    
    
if __name__=="__main__":
    app.run(host="192.168.2.8", port="5000")


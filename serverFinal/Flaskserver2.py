from flask import Flask,redirect, url_for, jsonify, request, json
import subprocess
#import CallTest

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

def handle_request():
    # The GET endpoint
    if request.method == "GET":
        return "This is the GET Endpoint of flask API."
    
    # The POST endpoint
    if request.method == "POST":
    
        response=request.get_json()
        print(response)
        fin_output = response.get('encoded_text', '')
        '''
        #Η συνάρτηση ελέγχου του encoded κειμένου που μου βγαζει error στον τυπο δεδομενων στο data ενω δεν θα επρεπε

        def utf8_check(data):
            #"Returns a Unicode object on success, or None on failure"
            
            try:
                data= data.encode()
                print("Valid UTF-8 Data")
                return data.decode('utf-8')
            except UnicodeDecodeError:
                print("Unicode Decode Error")
                return None

            
        data = response.get('encoded_file', '')
        udata = utf8_check(data)
        if udata is None:
            print("no data to check validity for")
        '''

        def arxeioGrapsimo(filedata,filename):
                with open(filename, "wb") as file:
                        file.write(filedata)
        
        file1= response.get('parameters', 'param_list[0]')
        file2= response.get('parameters', 'param_list[1]')
        file3= response.get('parameters', 'param_list[2]')
        file4=response.get('parameters', 'param_list[3]')
        file5=response.get('parameters', 'param_list[4]')
        
                
        arxeioGrapsimo(file1,"arithmos3")
        arxeioGrapsimo(file2,"noumero3")
        arxeioGrapsimo(file3,"diafora3")
        arxeioGrapsimo(file4,"pososta3")
        arxeioGrapsimo(file5,"xarakthres3")
            
        arg1="servertag"
        arg2="arithmos3"
        arg3="noumero3"
        arg4="diafora3"
        arg5="pososta3"
        arg6="xarakthres3"
        
        subprocess.call(['python', 'sumpiesh\\map_wdecode.py', arg1 , arg2, arg3, arg4, arg5, arg6])
        
        
        fin_output=str(response)

        with open("output.txt", "w") as file:
            file.write(fin_output)

        Param= response.get('parameters','')
        strParam=str(Param[0])
        #hexParam=(Param[0]).hex()
        #strParam=strParam.lstrip("[").rstrip("]") #gia na vgazei to prwto kai to teleutaio [] ap to string alla to sha akoma einai lathos se sxesh me to arxiko arxeio
        #bytesParam= hexParam.encode()
        #bytesParam=strParam.encode()
        bytesParam=bytes(strParam,"utf-8")
        print(bytesParam)
        #print(strParam)
        
        #Νομιζω δεν γραφεται το αρχειο σε bytes οπως θα επρεπε και εχω δοκιμασει πολλα πραγματα χωρις να μπορω να βρω το γιατι ακριβως ή να το φτιαξω

        with open("bytefile", "wb") as file:
                    file.write(bytesParam)
        
        '''
        responseObj=json.loads(response)


        for parameters in responseObj:
            parameters.get(parameters[1])

        byteParam= response.get('parameters','')

        res=[]                 # Convert list to string using a loop
        for x in byteParam:
            res[x] = x 

        with open("bytefile.txt", "wb") as file:
            file.write(res[1])
        '''
        
        # return the response as JSON
        return jsonify(response)


 

    
if __name__=="__main__":
    #app.run(host="192.168.2.8", port="5000")
    app.run(host="127.0.0.1", port="5000")


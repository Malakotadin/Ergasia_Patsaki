import json
import os
import io
import hmac
import hashlib
import requests
import math 
import subprocess
import string
import sys
import sumpiesh


headers = {'Content-type': 'application/json'}

param_list=[]
info={  
"encoded_file": "",
"compression_algorithm": "arithmetic",
"encoding": "linear",
"parameters":[param_list],
"errors": "",
"SHA256": "",
"entropy":""
}


#Εδώ βάζουμε το όνομα του αρχείου που θέλουμε να χρησιμοποιήσουμε
print("Enter the text file name:")
txtfile="kamikaze girls.srt.txt" #"test2.txt"#DYamiBaraLyrics.txt"#input()


#---Κείμενο---

with open(txtfile, 'r') as file:
    file_content = file.read()



subprocess.call(['python', 'sumpiesh\\encode4.py'])

f = open('sumpiesh\\tag_ls2','rb')
bin = f.read()
f.close()
hex_bin=bin.hex()

info["encoded_file"]= hex_bin
print("Encoded file imported")



#---Αλγόριθμος συμπίεσης---
print(f"Compression Algorithm:{info['compression_algorithm']}")

#---Encoding---
print(f"Encoding:{info['encoding']}")

#---Λίστα παραμέτρων---

'''
with open("tag_ls2", "rb") as file:
     bytetext= file.read()
hexbytes=bytetext.hex()
#bytestring=str(bytetext)

#param_list.append(bytestring)
param_list.append(hexbytes)
'''

print("Parameters:")

def arxeia(file):
    f = open(file,'rb')
    bin = f.read()
    f.close()
    #strbin=bin.decode()
    hex_bin=bin.hex()
    param_list.append(hex_bin)

arxeia("sumpiesh\\arithmos_bit2")
arxeia("sumpiesh\\tag_ls")
arxeia("sumpiesh\\tag_ls2")
arxeia("sumpiesh\\ls_pososta_ls2")
arxeia("sumpiesh\\ls_xarakthres_ls2")

print("parameters imported")

'''
def arxeia(file):
    f = open(file,'rb')
    bin = f.read()
    f.close()
    hex_bin=bin.hex()
    param_list.append(hex_bin)

arxeia("sumpiesh\\arithmos_bit2")
arxeia("sumpiesh\\noumero2")
arxeia("sumpiesh\\diafora2")
arxeia("sumpiesh\\ls_pososta_ls2")
arxeia("sumpiesh\\ls_xarakthres_ls2")
#arxeia("sumpiesh\\arithmos_bit2")
        
#print(f"Parameter List:{param_list}")
print("parameters imported")
'''

#---Errors---


print("Errors (0-100):")
info["errors"]= input()
print(info["errors"])


#---SHA256---


hash_func = hashlib.new('sha256')

with open(txtfile, 'rb') as file:
    for line in file:
        hash_func.update(line)

hex_digest=hash_func.hexdigest()


info["SHA256"]=hex_digest
print(f"SHA256:{hex_digest}")


#---Εντροπία---

def entropy(string):

    # Πιθανότητα εμφάνησης κάθε χαρακτήρα στο string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # Υπολογισμός εντροπίας
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy


Text_entropy= entropy(file_content)     
info["entropy"]=Text_entropy
print(f"entropy:{Text_entropy}")


#βάζω τα στοιχεία του dictionary σε ενα καινούριο json
("info.json", {})

with open("info.json", "w") as f:
        json.dump(info, f, indent=4)

#print(info["compression_algorithm"])


#response = requests.post(url="http://192.168.2.8:5000/", json=info , headers=headers)
response = requests.post(url="http://127.0.0.1:5000/", json=info , headers=headers)

print(response.text)


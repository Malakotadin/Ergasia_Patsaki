import subprocess
from mpmath import mp,mpf
import time,sys
from multiprocessing import process
import pickle
from encode_to_files3 import encoder
from decode_from_file_and_append_to_func import decoder
import threading
image_path='ff7.webp'
#bytes.hex
f= open(image_path,'rb')
bint = f.read()
f.close()
mp.dps=1024#γαμω γαμω γαμω γαμω εχασα 20 χρονια απο το προσδοκιμω ζωης μου και απέκτησα άλλο ένα φαλακρό σημείο στο κεφάλι μου για αυτή την γραμμή κώδικα
demo_string=bint.hex()
splicing_counter=0
arg=demo_string[:256]
noumero=0
strnoumero=str(noumero)
print(arg)
#exit()
infinite_mhden=mp.mpf(0.0)
tag_ls=len(demo_string)*[infinite_mhden]
ls_pososta_ls=[0]*len(demo_string)
ls_xarakthres_ls=[0]*len(demo_string)
breakpoint()
start=time.time()
split_ls=[]
split_counter=0

while(True):
    if split_counter+256>len(demo_string):
        split_ls.append(demo_string[split_counter:len(demo_string)])
        break

    split_ls.append(demo_string[split_counter:split_counter+256])

small_pool=multiprocessing.Pool(processes=2,maxtaskperchild=1000)
i=0
with small_pool as pool:
    print(i)
    pool.map(encoder,split_ls)
   
#dictionary_apothikeusis={split_ls[i]:[infinite_mhden,infinite_mhden,infinite_mhden] for i in range(0,tag_ls)}
endno=noumero
noumero=0
strnoumero=str(noumero)
#breakpoint()
output_ls=len(demo_string)*[""]
while(True):
    print(noumero)
   # print(noumero>endno)
    #subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    
    if endno==noumero:
        decode=threading.Thread(None,decoder(tag_ls[noumero],ls_pososta_ls[noumero],ls_xarakthres_ls[noumero],diafora,output_ls,noumero))
       # decoder(tag_ls[noumero],ls_pososta_ls[noumero],ls_xarakthres_ls[noumero],diafora)
        print("teleiosa")
        break
    decode=threading.Thread(None,decoder(tag_ls[noumero],ls_pososta_ls[noumero],ls_xarakthres_ls[noumero],256,output_ls,noumero))
   # decoder(tag_ls[noumero],ls_pososta_ls[noumero],ls_xarakthres_ls[noumero],256)
    noumero+=1
    strnoumero=str(noumero)

fin_output="".join(output_ls)
with open("final_try.webp","ab") as file:
        file.write(bytes.fromhex(fin_output))
end=time.time()
print("διηρκησα",end-start," δευτερολεπτα")
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])



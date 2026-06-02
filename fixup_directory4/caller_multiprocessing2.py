import subprocess
from mpmath import mp,mpf
import time,sys
import pickle
from parallel_encode import encoder
from parallel_decode import decoder
import threading
import multiprocessing
#from multiprocessing import Process
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
jobs=[]
start=time.time()
while(True):
    if splicing_counter+256>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        diafora=len(temp)
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
       # encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
        arg_ls=[arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero]
        tag_ls[noumero]=multiprocessing.Process(target=encoder,args=arg_ls)
      #  timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=threading.Thread(target=encoder,args=arg)
        
        
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+256]
      #  saving_list=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
        #timoula=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
       # breakpoint()
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=encoder(arg)
        #saving_list
       # print(saving_list)
      #  print(lista_arhikon_pososton)
     #  timoula=timoula.decode()
       # print(timoula)
       # print(timoula)
     #   encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
        arg_ls=[arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero]
        
        output=multiprocessing.Process(target=encoder,args=arg_ls)
        print(output)
        jobs.append(output)
        output.start()
       # breakpoint()
        tag_ls[noumero]=output

       # ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
       ## ls_pososta_ls[noumero]=lista_arhikon_pososton
        #tag_ls[noumero]=timoula
    noumero+=1
    strnoumero=str(noumero)
    splicing_counter+=256
    print(splicing_counter)
breakpoint()
for proc in jobs:
    proc.join()
print(jobs)
exit()
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



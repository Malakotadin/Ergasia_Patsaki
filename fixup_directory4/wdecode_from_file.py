import subprocess
from mpmath import mp,mpf
import time,sys
import pickle
from parallel_encode import encoder
from parallel_decode import decoder
import threading
mp.dps=1024
file_to_send=open("tag_ls",'rb')
tag_ls=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("arithmos_bit",'rb')
arithmos_bit=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("ls_pososta_ls",'rb')
ls_pososta_ls=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("ls_xarakthres_ls",'rb')
ls_xarakthres_ls=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("noumero",'rb')
noumero=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("diafora",'rb')
diafora=pickle.load(file_to_send)
file_to_send.close()
#arithmos_bit=apothikeutiki_lista2[0]
#tag_ls=apothikeutiki_lista2[1]
#ls_pososta_ls=apothikeutiki_lista2[2]
#ls_xarakthres_ls=apothikeutiki_lista2[3]
#3noumero=apothikeutiki_lista2[4]
#diafora=apothikeutiki_lista2[5]
#print(apothikeutiki_lista==apothikeutiki_lista2)
#for i in range(0,len(apothikeutiki_lista)):
 #   print(apothikeutiki_lista[i]==apothikeutiki_lista2[i])
#exit()
endno=noumero
noumero=0
strnoumero=str(noumero)
#breakpoint()
output_ls=len(tag_ls)*[""]
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
with open("final_try.bmp","ab") as file:
        file.write(bytes.fromhex(fin_output))
#end=time.time()
#print("διηρκησα",end-start," δευτερολεπτα")
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])






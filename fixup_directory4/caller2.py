import subprocess
from mpmath import mp,mpf
import time,sys
import pickle
from encode_to_files3 import encoder
from decode_from_file_and_append_to_func import decoder
image_path='gimp.bmp'
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
while(True):
    if splicing_counter+256>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
        timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=encoder(arg)
        ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
        ls_pososta_ls[noumero]=lista_arhikon_pososton
        tag_ls[noumero]=timoula
        
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+256]
      #  saving_list=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
        #timoula=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
       # breakpoint()
        timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=encoder(arg)
        #saving_list
       # print(saving_list)
      #  print(lista_arhikon_pososton)
     #  timoula=timoula.decode()
       # print(timoula)
       # print(timoula)
        ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
        ls_pososta_ls[noumero]=lista_arhikon_pososton
        tag_ls[noumero]=timoula
    noumero+=1
    strnoumero=str(noumero)
    splicing_counter+=256
    print(splicing_counter)
    
#exit()
endno=noumero
noumero=0
strnoumero=str(noumero)
#breakpoint()
while(True):
    print(noumero)
   # print(noumero>endno)
    #subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    decoder(tag_ls[noumero],ls_pososta_ls[noumero],ls_xarakthres_ls[noumero])
    if endno==noumero:
        print("teleiosa")
        break
    noumero+=1
    strnoumero=str(noumero)
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])



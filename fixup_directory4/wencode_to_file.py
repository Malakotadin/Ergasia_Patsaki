import subprocess
from mpmath import mp,mpf
import time,sys
import pickle
from parallel_encode import encoder
from parallel_decode import decoder
import threading
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
arithmos_bit=256
start=time.time()
while(True):
    if splicing_counter+256>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        diafora=len(temp)
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
        encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
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
        encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
       # ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
       ## ls_pososta_ls[noumero]=lista_arhikon_pososton
        #tag_ls[noumero]=timoula
    noumero+=1
    strnoumero=str(noumero)
    splicing_counter+=256
    print(splicing_counter)
    
#apothikeutiki_lista=[arithmos_bit,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero,diafora]

def cleaner(lista):
  for i in range(0,len(lista)):
    try:
      if lista[i]==infinite_mhden:
        lista.pop(i)
        print("i did something")
    except:
      pass

  return lista

#tag_ls=cleaner(tag_ls)
#ls_pososta_ls=cleaner(ls_pososta_ls)
#ls_xarakthres_ls=cleaner(ls_xarakthres_ls)
clean=threading.Thread(None,cleaner(tag_ls))#η  μαλακια ειναι οτι τα σωζο σε πολυ μεγαλο precisoin και αυτο μου τρώει τοσο χώρο, what do i do  ? 
clean=threading.Thread(None,cleaner(ls_pososta_ls))
clean=threading.Thread(None,cleaner(ls_xarakthres_ls))
file_to_send=open("tag_ls",'wb')
pickle.dump(tag_ls,file_to_send)
file_to_send.close()
file_to_send=open("arithmos_bit",'wb')
pickle.dump(arithmos_bit,file_to_send)
file_to_send.close()
file_to_send=open("ls_pososta_ls",'wb')
pickle.dump(ls_pososta_ls,file_to_send)
file_to_send.close()
file_to_send=open("ls_xarakthres_ls",'wb')
pickle.dump(ls_xarakthres_ls,file_to_send)
file_to_send.close()
file_to_send=open("noumero",'wb')
pickle.dump(noumero,file_to_send)
file_to_send.close()
file_to_send=open("diafora",'wb')
pickle.dump(diafora,file_to_send)
file_to_send.close()
file_to_send=open("tag_ls",'rb')
tag_ls2=pickle.load(file_to_send)
file_to_send.close()
#breakpoint()
file_to_send=open("arithmos_bit",'rb')
arithmos_bit=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("ls_pososta_ls",'rb')
ls_pososta_ls2=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("ls_xarakthres_ls",'rb')
ls_xarakthres_ls2=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("noumero",'rb')
noumero2=pickle.load(file_to_send)
file_to_send.close()
file_to_send=open("diafora",'rb')
diafora2=pickle.load(file_to_send)
file_to_send.close()
#breakpoint()
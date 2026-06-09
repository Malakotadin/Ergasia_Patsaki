import subprocess
from mpmath import mp,mpf,workdps,workprec,autoprec
import time,sys
import pickle
from mapped_encode import encoder
#from parallel_decode import decoder
import threading
import math
from p_tqdm import p_map
from scipy.stats import entropy
image_path='gimp.bmp'
#bytes.hex
f= open(image_path,'rb')
bint = f.read()
f.close()
arithmos_bit=4096
arithmos_bit=arithmos_bit*2#1 it psc ο υπολογιστης μου δεν μπορει αλλο 
arithmos_bit=arithmos_bit*2# αντιο γλυκε κοσμε , αντιο ψημενη σιλικονη μου , ευχομαι τουλαχιστον να παρουμε 10
arithmos_bit=arithmos_bit*2#ζηλευω αυτους τους intel core με τους 20 πυρηνες , σαν τον ικαρο πεταω ολο και πιο κοντα στον ηλιο
#νιωθω πως ο υπολογιστης μου θα ανατιναχτει σε αυτο το σημειο
mp.dps=math.ceil(arithmos_bit*1.085)#γαμω γαμω γαμω γαμω εχασα 20 χρονια απο το προσδοκιμω ζωης μου και απέκτησα άλλο ένα φαλακρό σημείο στο κεφάλι μου για αυτή την γραμμή κώδικα
demo_string=bint.hex()
splicing_counter=0
#arg=demo_string[:256]
noumero=0
strnoumero=str(noumero)
#print(arg)
lista_kopsimatos=[]

#exit()
infinite_mhden=mp.mpf(0.0)
tag_ls=len(demo_string)*[0]
ls_pososta_ls=[0]*len(demo_string)
ls_xarakthres_ls=[0]*len(demo_string)
#breakpoint()
#arithmos_bit=256
start=time.time()
while(True):
    if splicing_counter+arithmos_bit>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        lista_kopsimatos.append(arg)
        diafora=len(demo_string)-splicing_counter
        print(diafora)
      #p  breakpoint()
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
      #  encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
      #  timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=threading.Thread(target=encoder,args=arg)
        
        
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+arithmos_bit]
        lista_kopsimatos.append(arg)
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
       # encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
       # ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
       ## ls_pososta_ls[noumero]=lista_arhikon_pososton
        #tag_ls[noumero]=timoula
    #noumero+=1
    #strnoumero=str(noumero)
    splicing_counter+=arithmos_bit
    print(splicing_counter)


    #if i==len(lista_kopsimatos):
       # tagl_ls,ls_pososta_ls,ls_xarakthres_ls=list(map(encoder(diafora)))
def apothikeutis0(item):
    if item[0]!=infinite_mhden and item[0]!=0:
        return item[0]#εδω περα ισως μπορω να βγαζω να αφερει τα μηδενικα
    else:
      print("i happened0")
def apothikeutis1(item):
    if item[1]!=infinite_mhden and item[1]!=0:
        return item[1]#εδω περα ισως μπορω να βγαζω να αφερει τα μηδενικα
    else:
      print("i happened1")
def apothikeutis2(item):
    if item[2]!=infinite_mhden and item[2]!=0:
        return item[2]#εδω περα ισως μπορω να βγαζω να αφερει τα μηδενικα
    else:
      print("i happened2")
    

lista_apothikeusis=p_map(encoder,lista_kopsimatos)

#breakpoint()
tag_ls=p_map(apothikeutis0,lista_apothikeusis)
#breakpoint()
ls_pososta_ls=p_map(apothikeutis1,lista_apothikeusis)
ls_xarakthres_ls=p_map(apothikeutis2,lista_apothikeusis)
#breakpoint()
#exit()
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
noumero=len(tag_ls)
def selfer(value):
  #print(mp.dps)
  
  value=value[0]
  value=autoprec(value)
  return value
#tag_ls=cleaner(tag_ls)
#ls_pososta_ls=cleaner(ls_pososta_ls)
#ls_xarakthres_ls=cleaner(ls_xarakthres_ls)
#clean=threading.Thread(None,cleaner(tag_ls))#η  μαλακια ειναι οτι τα σωζο σε πολυ μεγαλο precisoin και αυτο μου τρώει τοσο χώρο, what do i do  ? 
#clean=threading.Thread(None,cleaner(ls_pososta_ls))
#clean=threading.Thread(None,cleaner(ls_xarakthres_ls))
#breakpoint()
#tag_ls=p_map(autoprec,lista_apothikeusis)
#breakpoint()
#ls_pososta_ls=p_map(autoprec,lista_apothikeusis)
#ls_xarakthres_ls=p_map(autoprec,lista_apothikeusis)
file_to_send=open("tag_ls",'wb')
pickle.dump(tag_ls,file_to_send)
file_to_send.close()
print("δεν μπηκαα")
with workdps(500):
  print("μπικααααα)")
  print(mp.dps)
 # tag_ls=p_map(selfer,lista_apothikeusis)
  #breakpoint()
  #ls_pososta_ls=p_map(selfer,lista_apothikeusis)
  #ls_xarakthres_ls=p_map(selfer,lista_apothikeusis)
  print(mp.dps)
  #breakpoint()

  file_to_send=open("tag_ls2",'wb')
  pickle.dump(tag_ls,file_to_send)
  file_to_send.close()
  #exit()
  file_to_send=open("arithmos_bit2",'wb')
  pickle.dump(arithmos_bit,file_to_send)
  file_to_send.close()
  file_to_send=open("ls_pososta_ls2",'wb')
  pickle.dump(ls_pososta_ls,file_to_send)
  file_to_send.close()
  file_to_send=open("ls_xarakthres_ls2",'wb')
  pickle.dump(ls_xarakthres_ls,file_to_send)
  file_to_send.close()
  file_to_send=open("noumero2",'wb')
  pickle.dump(noumero,file_to_send)
  file_to_send.close()
  file_to_send=open("diafora2",'wb')
  pickle.dump(diafora,file_to_send)
  file_to_send.close()

#  απο εδω και πέρα θα δημιουργήσω το μεγάλο binary για υπολογισμούς εντροπίας , γαμώ το σπίτι μου
with open("tag_ls2",'ab') as tag_file ,  open("arithmos_bit2",'rb') as arithmos_bit , open("ls_pososta_ls2",'rb') as ls_pososta_ls , open("ls_xarakthres_ls2",'rb') as ls_xarakthres_ls , open("noumero",'rb') as noumero,open("diafora",'rb')as diafora :
  tag_file.write(arithmos_bit.read())
  tag_file.write(ls_pososta_ls.read())
  tag_file.write(ls_xarakthres_ls.read())
  tag_file.write(noumero.read())
  tag_file.write(diafora.read())
 # arithmos_bit_len=len(arithmos_bit.read())
  

  #breakpoint()

ls_pososta_ls
f= open('tag_ls2','rb')
bint = f.read()
f.close()
final_file=bint.hex()
def string_yparhei(dictionary_xarakthron_kai_pososton,char):
    for key in dictionary_xarakthron_kai_pososton:
        if char==key:
            dictionary_xarakthron_kai_pososton[char]=dictionary_xarakthron_kai_pososton[char] +1
            return dictionary_xarakthron_kai_pososton
    dictionary_xarakthron_kai_pososton[char]=1
    return dictionary_xarakthron_kai_pososton

def diavasma_string(string):
    dictionary_xarakthron_kai_pososton={}
    
    
    for char in string:
        
        dictionary_xarakthron_kai_pososton=string_yparhei(dictionary_xarakthron_kai_pososton,char)
        
    return dictionary_xarakthron_kai_pososton 

dictionary_xarakthron_kai_pososton=diavasma_string(final_file)
lista_arhikon_pososton=[]
for key in dictionary_xarakthron_kai_pososton:
    lista_arhikon_pososton.append(dictionary_xarakthron_kai_pososton[key])

p=lista_arhikon_pososton
ent = entropy(p, base=2)
print("Entropy:", ent)
breakpoint()
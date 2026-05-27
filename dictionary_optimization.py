from mpmath import mp,mpf 
import sys ,os
import time ,threading,math
import pickle
from scipy.stats import entropy
image_path='/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg'
f= open(image_path,'rb')
bin = f.read()
f.close()
#print(bin)
def lista_pososton_finderv2(demo_stirng):
    lista_xarakthron=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    lista_foron=16*[0]
    for char in demo_stirng:
        lista_foron[lista_xarakthron.index(char)]+=1
    for i in range(0,len(lista_foron)):
        lista_foron[i]=lista_foron[i]/len(demo_stirng)
    print(lista_foron)
    return lista_foron
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
def lista_posostron_finder(demo_string):
    dictionary_xarakthron_kai_pososton=diavasma_string(demo_string)
    lista_monadikon_xarakthron=[]
    for key in dictionary_xarakthron_kai_pososton:
        lista_monadikon_xarakthron.append(key)
    temp=0
    print(lista_monadikon_xarakthron)
    #breakpoint()

    lista_arhikon_pososton=[]
    lista_olikon_poston=[]
    metritis_monadikon_xarakthron=0
    for key in dictionary_xarakthron_kai_pososton:
        lista_arhikon_pososton.append(dictionary_xarakthron_kai_pososton[key])
        metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
        dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]/arithmos_bit +temp
        lista_olikon_poston.append(dictionary_xarakthron_kai_pososton[key])
        temp= dictionary_xarakthron_kai_pososton[key]
    lista_arhikon_pososton=[timi/arithmos_bit for timi in lista_arhikon_pososton]    
    return lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string

flag=0
megethos_eikonas=os.path.getsize(image_path)
infinite_miden=mp.mpf(0)
#mp.dps=1
hex_bin=bin.hex()#μετατροπή σε hex

#print(type(hex_bin))
#arithmos_bit=len(hex_bin)
block_size=512
demo_string=bin.hex()
arithmos_bit=len(demo_string)
def entropy_finder(demo_string):
    lista_pososton_emfanisis=lista_pososton_finderv2(demo_string)
    print(lista_pososton_emfanisis)
    #breakpoint()
    ent=entropy(lista_pososton_emfanisis,base=16)
    print("Entropy",ent)
    exit()
entropy_finder(demo_string)
mp.dps=block_size
arhiko_megethos_string=len(demo_string)
demo_string=demo_string[:arhiko_megethos_string]
#for i  in range(0,(len(demo_string)/block_size)+1):
carry_value_ls=[infinite_miden,infinite_miden,infinite_miden,infinite_miden]
dictionary_apothikeuesis={x:carry_value_ls for x in range(0,math.ceil(len(demo_string)/block_size))} 
start=time.time()
print(len(demo_string))
print(demo_string)
#exit()
counter_foron=0
splicing_counter=0


#lista_apothikeusis_ton_kommatakion_to_be_decoded=[infinite_miden]*(arithmos_bit+1)
lista_apothikeusis_ton_kommatakion_to_be_decoded2=[infinite_miden]*(arhiko_megethos_string)
#print(lista_apothikeusis_ton_kommatakion_to_be_decoded)
lista_apothikeusis_liston_monadikon_xarakthron=[0]*(arhiko_megethos_string)
#exit()



def olika_pososta(kato_orio,ano_orio,lista_pithanotiton):
    oliko_pososto=[kato_orio]
    diafora=ano_orio-kato_orio
    kato_orio_xarakthra=kato_orio
    for pithanotita in lista_pithanotiton:
        ano_orio_xarakthra=kato_orio_xarakthra+(diafora*pithanotita)
        oliko_pososto.append(ano_orio_xarakthra)
        kato_orio_xarakthra=ano_orio_xarakthra
    return oliko_pososto

def apostasi_tou_kleidou(lista_olikon_poston,lista_monadikon_xarakthron):
    interval={}
    i=0
    j=0 
    while i <len(lista_olikon_poston)-1:
        #print(len(lista_olikon_poston)-i)
        key = lista_monadikon_xarakthron[i]
        kato_orio=lista_olikon_poston[i]#εδω περα οριζονται τα ορια 
        ano_orio=lista_olikon_poston[i+1]
        interval[key]=[kato_orio,ano_orio]
        i+=1
        j+=1
    return interval


def encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string):
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
    #print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    timoula=0
    timoula=mp.mpf(timoula)
    for character in demo_string:
        char_diastima=dictionary_diastimaton.get(character)
        kato_orio_xarakthra=char_diastima[0]
        ano_orio_xarakthra=char_diastima[1]
        timoula=(kato_orio_xarakthra+ano_orio_xarakthra)/2.0
        oliki_lista_pososton=olika_pososta(kato_orio_xarakthra,ano_orio_xarakthra,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
   # print("teliosa",counter_foron)
    print("Η τιμουλα είναι",timoula)
    return timoula

def decoderv2(timoula,arithmos_bit,lista_arhikon_pososton,lista_monadikon_xarakthron):
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
   # print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    i=0
    teliko_string=[]
    kato_orio=0
    ano_orio=1
    torino_kato_orio=mp.mpf(kato_orio)
    torino_ano_orio=mp.mpf(ano_orio)
    while i < arithmos_bit:
       # print(i)
        for key,value in dictionary_diastimaton.items():
            kato_orio=value[0]
            ano_orio=value[1]
           # print((timoula >= kato_orio) and (timoula <= ano_orio))
          #  print(float(kato_orio)==float(timoula))
          #  print(float(ano_orio)==float(timoula))
          #  print("".join(teliko_string))
          #  print(timoula,kato_orio)
           # breakpoint()
          #  print("xamilo orio",kato_orio)
           # print("timoula",timoula)
           # print("psilo",ano_orio)
            if (timoula >= kato_orio) and (timoula<=ano_orio):
                
                torino_kato_orio=kato_orio
                torino_ano_orio=ano_orio
                teliko_string.append(key)#εδω περα μπορω να κανω optimize ισως βαζοντας concantenation αντι για ολες αυτες τις λιστες
                break
           
        oliki_lista_pososton=olika_pososta(torino_kato_orio,torino_ano_orio,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
        i+=1
    
    return teliko_string
i=0
string_to_use=demo_string[:block_size]
def encoder_wrapper(string_to_use,i,dictionary_apothikeuesis):
    
    dictionary_apothikeuesis[i][0],dictionary_apothikeuesis[i][1],string_to_use=lista_posostron_finder(string_to_use)#0λιστα αρχικων ποσοστον , 1 λιστα μοναδικων χαρακτηρων
   # lista_apothikeuseis_arhikon_pososton[i]=lista_arhikon_pososton
   # lista_apothikeusis_liston_monadikon_xarakthron[i]=lista_monadikon_xaraktiron #θα μπουρουσα απλα να περάσω το dictionary και σαν ορισμα
    stringaki=encoderv2(dictionary_apothikeuesis[i][0],dictionary_apothikeuesis[i][1],string_to_use)
    dictionary_apothikeuesis[i][2]=stringaki
   # print(stringaki==lista_apothikeusis_ton_kommatakion_to_be_decoded2[i])

def decoder_wrapper(arithmos_bit,i,dictionary_apothikeuesis):

    stringaki="".join(decoderv2(dictionary_apothikeuesis[i][2],arithmos_bit,dictionary_apothikeuesis[i][0],dictionary_apothikeuesis[i][1]))
    dictionary_apothikeuesis[i][3]=stringaki#lista_apothikeysis decoded bits ==3


#print(lista_apothikeusis_ton_kommatakion_to_be_decoded[1])
print(demo_string)
print(len(demo_string))
#exit()
counter_foron=0
#lista_apothikeuseis_arhikon_pososton=[infinite_miden]*len(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
#dictionary_apothikeuesis={k:(v[0])*[infinite_miden]for k,v in dictionary_apothikeuesis.items()}#θα μπορουα να τα οριζω ολα αυτα και στην αρχή 
#ista_apothikeusis_ton_kommatakion_to_be_decoded2=[]
while(True):
    #breakpoint()
   # if counter_foron==100:

      #  break
    
    if splicing_counter+block_size>len(demo_string):   
      #  breakpoint()
        diafora=len(demo_string)-splicing_counter
        string_to_use=demo_string[splicing_counter:len(demo_string)]
        #a,b,c=lista_posostron_finder(string_to_use)
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,dictionary_apothikeuesis))
        print("τελειωσαααα")
        print(splicing_counter)
        
        # lista_apothikeusis_ton_kommatakion_to_be_decoded[i]=stringaki
        break
    else:
     #   print("itsover")
        
       # breakpoint()
     #   print("o xarakthras ston opoio vrisokmai einai",demo_string[splicing_counter:splicing_counter+block_size])
        string_to_use=demo_string[splicing_counter:splicing_counter+block_size]
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,dictionary_apothikeuesis))
      #  print(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
      #  #exit()
    counter_foron+=1
    splicing_counter=splicing_counter+block_size
   # print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
    print(splicing_counter)
#print(dictionary_apothikeuesis)
#breakpoint()
#lista_oxi_midenikon=[]
#for item in lista_apothikeusis_ton_kommatakion_to_be_decoded2:#αυτό επίσης θα μπορούσε να μην είναι απαραίτητο και να σώζει χρόνο
#    if(item!=0):
  #      lista_oxi_midenikon.append(item)
 #       print(item)δοκιμαζω να το σβήσω
       
#if lista_oxi_midenikon==lista_apothikeusis_ton_kommatakion_to_be_decoded2:
 #   print("οι λιστες ισουνται")
 #   exit()
print(counter_foron==arhiko_megethos_string)
print("arhiko_megethos",arhiko_megethos_string)       
print(splicing_counter)
print(block_size)
#rint(len(lista_oxi_midenikon))
end=time.time()
print(end-start)#108 δευτερολεπτα , not bad not bad
#breakpoint()#νιωθω i  think thats good υπαρχει ενα μικρο descrepency με το splicing counter και arhiko megethos string but i think its whatever,οχι οχι νομίζω είναι καλά actually
#exit()
#νιωθω αυτη η υλοποίηση είναι πολύ καλή 
#lista_apothikeuseis_decoded_bits=[infinite_miden]*len(lista_oxi_midenikon)
def get_size(obj, seen=None):#ναναι καλά ο Wissam jarjoui για την παρακάτω συναρτηση γιατι και εγώ κάτι βρώμικο μυρίστηκα
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size#ισως μπορώ να το κάνω optimize μόνο για dictionaries  με βάση το δικό μου use case
mikos=len(dictionary_apothikeuesis)
compressed_size_to_send=get_size(dictionary_apothikeuesis)# έστω οτι αυτός ο κωδικςα δουλευει 
compressed_sizecounter=0
for i in range(0,mikos):
    compressed_sizecounter+=dictionary_apothikeuesis[i][2]

def list_size_finder(lista):
    summer=0
    for item in lista:
        summer+=sys.getsizeof(item)
    return summer
def get_size_of_dictionary(dictionary):
    summer=0
    for item in dictionary.items():
        summer+=list_size_finder(item)
    return summer
compressed_size_to_send_diko_mou=get_size_of_dictionary(dictionary_apothikeuesis)
print(block_size)
print("diko mou megethos",compressed_size_to_send_diko_mou)
print("μεγεθος λιστας",compressed_size_to_send)
print("compression rate ",(compressed_size_to_send_diko_mou/megethos_eikonas)*100)
file_to_send=open("file_to_send",'wb')
pickle.dump(dictionary_apothikeuesis,file_to_send)
file_to_send.close()
file_to_send=open("file_to_send",'rb')
dictionary_apothikeuesis2=pickle.load(file_to_send)
file_to_send.close()
file_size = os.path.getsize('file_to_send')
print("File Size is :", file_size, "bytes")

print("compression rate ,arheio",(file_size/megethos_eikonas)*100)
print(dictionary_apothikeuesis2==dictionary_apothikeuesis)#woah holy shit 
exit()

#να σκεφτω πως ισως θα ηταν να μην περνάω ολοκληρο το dictionary σαν ορισμα και μόνο συγκεκριμένες τιμές

for i in range(0,mikos):
    if i!=mikos:
        threading.Thread(None,decoder_wrapper(block_size,i,dictionary_apothikeuesis))
    else:
        threading.Thread(None,decoder_wrapper(diafora,i,dictionary_apothikeuesis))
   # print(lista_apothikeuseis_decoded_bits[i])
   # print(demo_string[i])
    #breakpoint()


def string_concantinator(dictionary_apothikeuesis):
    string=""
    for i in range(0,mikos):
        for char in dictionary_apothikeuesis[i][3]:
            string+=char
        

    return string


#ολες αυτέςτις λίστες να τις κάνω ένα μεγάλο dictionary #optimization
#teliko_string="".join(lista_apothikeuseis_decoded_bits)
teliko_string=string_concantinator(dictionary_apothikeuesis)

#breakpoint()
#hexed_teliko_stirng=hex(teliko_string)
#breakpoint()
#if hexed_teliko_stirng==hex_bin:

f= open('/home/meow/pytohn_codes/ergasia_patsaki/final_photo.jpg','br+')
f.write(bytes.fromhex(hex_bin))
f.close()
#else:
    #breakpoint()
end2=time.time()
print(end2-end)
print(end2-start)
print("μεγεθος λιστας",compressed_size_to_send)
print("compression rate ",(compressed_size_to_send/megethos_eikonas)*100)
#print("μεγεθος των αντικειμενων μονο ",compressed_sizecounter)
#megethos_eikonas=os.path.getsize('/home/meow/pytohn_codes/ergasia_patsaki/ff6.png')
print(megethos_eikonas)
print(megethos_eikonas>compressed_size_to_send,megethos_eikonas>compressed_sizecounter)
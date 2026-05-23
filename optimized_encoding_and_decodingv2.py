from mpmath import mp,mpf
import time ,threading
f= open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
#print(bin)
flag=0


#mp.dps=1
hex_bin=bin.hex()#μετατροπή σε hex
#print(type(hex_bin))
#arithmos_bit=len(hex_bin)
block_size=256
demo_string=bin.hex()
mp.dps=block_size
arhiko_megethos_string=len(demo_string)
demo_string=demo_string[:arhiko_megethos_string]

start=time.time()
print(len(demo_string))
print(demo_string)
#exit()
counter_foron=0
splicing_counter=0
arithmos_bit=len(demo_string)
infinite_miden=mp.mpf(0)
#lista_apothikeusis_ton_kommatakion_to_be_decoded=[infinite_miden]*(arithmos_bit+1)
lista_apothikeusis_ton_kommatakion_to_be_decoded2=[infinite_miden]*(arhiko_megethos_string+1)
#print(lista_apothikeusis_ton_kommatakion_to_be_decoded)
lista_apothikeusis_liston_monadikon_xarakthron=[0]*(arhiko_megethos_string+1)
#exit()
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
def encoder_wrapper(string_to_use,i,lista_apothikeusis_ton_kommatakion_to_be_decoded2,lista_apothikeuseis_arhikon_pososton,lista_apothikeusis_liston_monadikon_xarakthron):
    
    lista_arhikon_pososton,lista_monadikon_xaraktiron,string_to_use=lista_posostron_finder(string_to_use)
    lista_apothikeuseis_arhikon_pososton[i]=lista_arhikon_pososton
    lista_apothikeusis_liston_monadikon_xarakthron[i]=lista_monadikon_xaraktiron
    stringaki=encoderv2(lista_arhikon_pososton,lista_monadikon_xaraktiron,string_to_use)
    lista_apothikeusis_ton_kommatakion_to_be_decoded2[i]=stringaki
    print(stringaki==lista_apothikeusis_ton_kommatakion_to_be_decoded2[i])

def decoder_wrapper(timoula,arithmos_bit,lista_arhikon_pososton,i,lista_apothikeuseis_decoded_bits,lista_monadikon_xarakthron):

    stringaki="".join(decoderv2(timoula,arithmos_bit,lista_arhikon_pososton,lista_monadikon_xarakthron))
    lista_apothikeuseis_decoded_bits[i]=stringaki


#print(lista_apothikeusis_ton_kommatakion_to_be_decoded[1])
print(demo_string)
print(len(demo_string))
#exit()
counter_foron=0
lista_apothikeuseis_arhikon_pososton=[infinite_miden]*len(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
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
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,lista_apothikeusis_ton_kommatakion_to_be_decoded2,lista_apothikeuseis_arhikon_pososton,lista_apothikeusis_liston_monadikon_xarakthron))
        print("τελειωσαααα")
        print(splicing_counter)
        
        # lista_apothikeusis_ton_kommatakion_to_be_decoded[i]=stringaki
        break
    else:
     #   print("itsover")
        
       # breakpoint()
     #   print("o xarakthras ston opoio vrisokmai einai",demo_string[splicing_counter:splicing_counter+block_size])
        string_to_use=demo_string[splicing_counter:splicing_counter+block_size]
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,lista_apothikeusis_ton_kommatakion_to_be_decoded2,lista_apothikeuseis_arhikon_pososton,lista_apothikeusis_liston_monadikon_xarakthron))
      #  print(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
      #  #exit()
    counter_foron+=1
    splicing_counter=splicing_counter+block_size
   # print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
    print(splicing_counter)
    

lista_oxi_midenikon=[]
for item in lista_apothikeusis_ton_kommatakion_to_be_decoded2:#αυτό επίσης θα μπορούσε να μην είναι απαραίτητο και να σώζει χρόνο
    if(item!=0):
        lista_oxi_midenikon.append(item)
        print(item)
       
print(counter_foron==arhiko_megethos_string)
print("arhiko_megethos",arhiko_megethos_string)       
print(splicing_counter)
print(block_size)
print(len(lista_oxi_midenikon))
end=time.time()
print(end-start)#108 δευτερολεπτα , not bad not bad
#breakpoint()#νιωθω i  think thats good υπαρχει ενα μικρο descrepency με το splicing counter και arhiko megethos string but i think its whatever,οχι οχι νομίζω είναι καλά actually
#exit()
#νιωθω αυτη η υλοποίηση είναι πολύ καλή 
lista_apothikeuseis_decoded_bits=[infinite_miden]*len(lista_oxi_midenikon)

for i in range(0,len(lista_oxi_midenikon)):
    if i!=len(lista_oxi_midenikon):
        threading.Thread(None,decoder_wrapper(lista_oxi_midenikon[i],block_size,lista_apothikeuseis_arhikon_pososton[i],i,lista_apothikeuseis_decoded_bits,lista_apothikeusis_liston_monadikon_xarakthron[i]))
    else:
        threading.Thread(None,decoder_wrapper(lista_oxi_midenikon[i],diafora,lista_apothikeuseis_arhikon_pososton[i],i,lista_apothikeuseis_decoded_bits,lista_apothikeusis_liston_monadikon_xarakthron[i]))
   # print(lista_apothikeuseis_decoded_bits[i])
   # print(demo_string[i])
    #breakpoint()


def string_concantinator(lista_apothikeuseis_decoded_bits):
    string=""
    for lista in lista_apothikeuseis_decoded_bits:
        for char in lista:
            string+=char
    return string


#ολες αυτέςτις λίστες να τις κάνω ένα μεγάλο dictionary #optimization
#teliko_string="".join(lista_apothikeuseis_decoded_bits)
teliko_string=string_concantinator(lista_apothikeuseis_decoded_bits)

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
import time, threading

f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
flag = False

block_size = 256

demo_string = bin.hex()

demo_string
block_demo_string: list[str] = [demo_string[start:start + block_size] for start in range(0, len(demo_string), block_size)]

print(len(demo_string))
print(demo_string)

counter_foron = 0
splicing_counter = 0

demo_len = len(demo_string)

lista_apothikeusis_ton_kommatakion_to_be_decoded=[0]*(demo_len+1)
lista_apothikeusis_ton_kommatakion_to_be_decoded2=[0]*(demo_len+1)

# Calculate the frequencies of each block of the demo_string
def create_block_char_frequency_dict(block):
    block_char_frequency_dict={}
    
    for char in block:
        if char in char_frequency_dict:
            block_char_frequency_dict[char] = char_frequency_dict[char] + 1
        else:
            block_char_frequency_dict[char] = 1
        
    return block_char_frequency_dict 

def lista_posostron_finder(block_demo_string):

    for block in block_demo_string:
        block_char_frequency_dict = create_block_char_frequency_dict(block)
    
        block_freq_percent_list = [freq/block_size for freq in block_char_frequency_dict.values()]
        lista_olikon_poston = []
        metritis_monadikon_xarakthron = 0
    
        for key in char_frequency_dict:
            block_freq_percent_list.append(char_frequency_dict[key])
            metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
            char_frequency_dict[key]=char_frequency_dict[key]/demo_len +temp
            lista_olikon_poston.append(char_frequency_dict[key])
            temp= char_frequency_dict[key]
    
        block_freq_percent_list=[timi/block_size for timi in block_freq_percent_list]    
    
    return block_freq_percent_list, lista_monadikon_xarakthron

def olika_pososta(kato_orio,ano_orio,lista_pithanotiton):
    oliko_pososto = [kato_orio]
    diafora = ano_orio-kato_orio
    kato_orio_xarakthra = kato_orio
 
    for pithanotita in lista_pithanotiton:
        ano_orio_xarakthra = kato_orio_xarakthra + (diafora*pithanotita)
        oliko_pososto.append(ano_orio_xarakthra)
        kato_orio_xarakthra = ano_orio_xarakthra
 
    return oliko_pososto

def apostasi_tou_kleidou(lista_olikon_poston,lista_monadikon_xarakthron):
    interval = {}
 
    i = 0
    j = 0 
    while i < len(lista_olikon_poston)-1:
        #print(len(lista_olikon_poston)-i)
        key = lista_monadikon_xarakthron[i]
        kato_orio = lista_olikon_poston[i]#εδω περα οριζονται τα ορια 
        ano_orio = lista_olikon_poston[i + 1]
        interval[key] = [kato_orio,ano_orio]
        i += 1
        j += 1
 
    return interval


def encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string):
    start = 0
    start = mp.mpf(start)
    end = 1
    end = mp.mpf(end)
 
    oliki_lista_pososton = olika_pososta(start, end, lista_arhikon_pososton)
    dictionary_diastimaton = apostasi_tou_kleidou(oliki_lista_pososton, lista_monadikon_xarakthron)
 
    #print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
 
    timoula = 0
    timoula = mp.mpf(timoula)
    for character in demo_string:
        char_diastima = dictionary_diastimaton.get(character)
        kato_orio_xarakthra = char_diastima[0]
        ano_orio_xarakthra = char_diastima[1]
        timoula = (kato_orio_xarakthra+ano_orio_xarakthra)/2.0
        oliki_lista_pososton = olika_pososta(kato_orio_xarakthra, ano_orio_xarakthra, lista_arhikon_pososton)
        dictionary_diastimaton = apostasi_tou_kleidou(oliki_lista_pososton, lista_monadikon_xarakthron)
 
   # print("teliosa",counter_foron)
 
    print("Η τιμουλα είναι",timoula)
 
    return timoula

def decoderv2(timoula,demo_len,lista_arhikon_pososton):
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
    while i < demo_len:
        print(i)
        for key,value in dictionary_diastimaton.items():
            kato_orio=value[0]
            ano_orio=value[1]
           # print((timoula >= kato_orio) and (timoula <= ano_orio))
            print(float(kato_orio)==float(timoula))
            print(float(ano_orio)==float(timoula))
            print("".join(teliko_string))
            print(timoula,kato_orio)
           # breakpoint()
            print("xamilo orio",kato_orio)
            print("timoula",timoula)
            print("psilo",ano_orio)
            if (timoula >= kato_orio) and (timoula<=ano_orio):
                
                torino_kato_orio=kato_orio
                torino_ano_orio=ano_orio
                teliko_string.append(key)
                break
           
        oliki_lista_pososton=olika_pososta(torino_kato_orio,torino_ano_orio,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
        i+=1
    
    return teliko_string
i=0
string_to_use=demo_string[:block_size]
def encoder_wrapper(string_to_use,i,lista_apothikeusis_ton_kommatakion_to_be_decoded2):
    
    lista_arhikon_pososton,lista_monadikon_xaraktiron,string_to_use=lista_posostron_finder(string_to_use)
    stringaki=encoderv2(lista_arhikon_pososton,lista_monadikon_xaraktiron,string_to_use)
    lista_apothikeusis_ton_kommatakion_to_be_decoded2[i]=stringaki
    print(stringaki==lista_apothikeusis_ton_kommatakion_to_be_decoded2[i])


print(demo_string)
print(len(demo_string))

counter_foron=0

while(True):
    #breakpoint()
   # if counter_foron==100:

      #  break
    
    if splicing_counter+block_size>len(demo_string):   
        breakpoint()
        string_to_use=demo_string[splicing_counter:len(demo_string)]
        #a,b,c=lista_posostron_finder(string_to_use)
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,lista_apothikeusis_ton_kommatakion_to_be_decoded2))
        # lista_apothikeusis_ton_kommatakion_to_be_decoded[i]=stringaki
        break
    else:
        print("itsover")
        
       # breakpoint()
        print("o xarakthras ston opoio vrisokmai einai",demo_string[splicing_counter:splicing_counter+block_size])
        string_to_use=demo_string[splicing_counter:splicing_counter+block_size]
        stringaki=threading.Thread(None,encoder_wrapper(string_to_use,counter_foron,lista_apothikeusis_ton_kommatakion_to_be_decoded2))
        print(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
        #exit()
    counter_foron+=1
    splicing_counter=splicing_counter+block_size
   # print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
    print(splicing_counter)
    


print(lista_apothikeusis_ton_kommatakion_to_be_decoded2)
       

exit()
#νιωθω αυτη η υλοποίηση είναι πολύ καλή 

char_frequency_dict=create_char_frequency_dict(demo_string)
lista_monadikon_xarakthron=[]
for key in char_frequency_dict:
    lista_monadikon_xarakthron.append(key)
temp=0
print(lista_monadikon_xarakthron)
#breakpoint()
lista_arhikon_pososton=[]
lista_olikon_poston=[]
metritis_monadikon_xarakthron=0
for key in char_frequency_dict:
    lista_arhikon_pososton.append(char_frequency_dict[key])
    metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
    char_frequency_dict[key]=char_frequency_dict[key]/demo_len +temp
    lista_olikon_poston.append(char_frequency_dict[key])
    temp= char_frequency_dict[key]
lista_arhikon_pososton=[timi/demo_len for timi in lista_arhikon_pososton]    
print(lista_arhikon_pososton)
#breakpoint()
print(char_frequency_dict)
#breakpoint()
start_range=0
end_range=1
start_range=mp.mpf(start_range)
end_range=mp.mpf(end_range)
print(lista_arhikon_pososton)


lista_arhikon_pososton=[timi/demo_len for timi in lista_arhikon_pososton]
print(lista_olikon_poston)
#breakpoint()



timoula=encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string)#ωραια αυτο επιστρεφει επιτυχως τιμη



def iterator(timoula,demo_len,arhiki_lista_sinolon,start,end,decoded_string):
    if demo_len==0:
        return decoded_string
    for i in range(0,len(arhiki_lista_sinolon)):
       # breakpoint()
        if timoula<arhiki_lista_sinolon[0]: #and start==0:# εδω περα ισως να το θελει αυτο , θα το δουμε i guess
            end=arhiki_lista_sinolon[0]
            decoded_string=decoded_string+lista_monadikon_xarakthron[0]
            return iterator(timoula,demo_len-1,[item*lista_arhikon_pososton[0] for item in arhiki_lista_sinolon],start,end,decoded_string)
        elif timoula<arhiki_lista_sinolon[i]:
            print("mpika_elif")
            start=arhiki_lista_sinolon[i-1]
            end=arhiki_lista_sinolon[i]

            decoded_string=decoded_string+lista_monadikon_xarakthron[i]
            print(decoded_string)
            return(timoula,demo_len-1,[item*lista_arhikon_pososton[i] for item in arhiki_lista_sinolon],start,end,decoded_string)
            

        

def decoder(timoula,demo_len,arhiki_lista_sinolon):
    start=0
    end=1
    decoded_string=""
    decoded_string=iterator(timoula,demo_len,arhiki_lista_sinolon,start,end,decoded_string)
    print("bgika_decoder")
    return decoded_string

print(timoula)
#breakpoint()
#exit()
final_output="".join(decoderv2(timoula,demo_len,lista_arhikon_pososton))
print(demo_len)
print(demo_string)
print(demo_string==final_output)
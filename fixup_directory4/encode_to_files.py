from mpmath import mp,mpf
import time,sys
import pickle

splicing_counter_begin=sys.argv[1]
f= open('ff7.webp','rb')
bin = f.read()
f.close()
#print(bin)
flag=0


#mp.dps=1
#hex_bin=bin.hex()#μετατροπή σε hex
#print(type(hex_bin))
#arithmos_bit=len(hex_bin)

demo_string=bin.hex()
mp.dps=512
demo_string=demo_string[splicing_counter_begin:splicing_counter_begin+256]
arithmos_bit=len(demo_string)
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
       


#νιωθω αυτη η υλοποίηση είναι πολύ καλή 

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
    
print(lista_arhikon_pososton)
#breakpoint()
print(dictionary_xarakthron_kai_pososton)
#breakpoint()
start_range=0
end_range=1
start_range=mp.mpf(start_range)
end_range=mp.mpf(end_range)
print(lista_arhikon_pososton)


lista_arhikon_pososton=[timi/arithmos_bit for timi in lista_arhikon_pososton]
print(lista_olikon_poston)
#breakpoint()

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
    print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    timoula=0
    timoula=mp.mpf(timoula)
    for character in demo_string:
        char_diastima=dictionary_diastimaton.get(character)
        kato_orio_xarakthra=char_diastima[0]
        ano_orio_xarakthra=char_diastima[1]
        timoula=(kato_orio_xarakthra+ano_orio_xarakthra)/2.0
        oliki_lista_pososton=olika_pososta(kato_orio_xarakthra,ano_orio_xarakthra,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)

    return timoula

timoula=encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string)#ωραια αυτο επιστρεφει επιτυχως τιμη

def decoderv2(timoula,arithmos_bit,lista_arhikon_pososton):
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
    print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    i=0
    teliko_string=[]
    kato_orio=0
    ano_orio=1
    torino_kato_orio=mp.mpf(kato_orio)
    torino_ano_orio=mp.mpf(ano_orio)
    while i < arithmos_bit:
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


        

print(timoula)
#breakpoint()
#exit()
with open(f"timoula{splicing_counter_begin}.txt","w") as file:
    file.write(timoula)
filename=f"arhiki_lista_sinolon{splicing_counter_begin}"
with open(filename,'wb') as file:
    pickle.dump(arhiki_lista_sinolon,file)
#final_output="".join(decoderv2(timoula,arithmos_bit,lista_arhikon_pososton))
print(arithmos_bit)
print(demo_string)
print(final_output)
print(demo_string==final_output)
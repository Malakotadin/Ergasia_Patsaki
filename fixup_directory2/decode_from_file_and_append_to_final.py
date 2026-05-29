from mpmath import mp,mpf
import time,sys
import pickle
arithmos_bit=256
#id=0
mp.dps=512
#breakpoint()
id=int(sys.argv[1])
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

def decoderv2(timoula,arithmos_bit,lista_arhikon_pososton,lista_monadikon_xarakthron):
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
 #   print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
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
         #   print(float(kato_orio)==float(timoula))
          #  print(float(ano_orio)==float(timoula))
           # print("".join(teliko_string))
            #print(timoula,kato_orio)
           # breakpoint()
            #print("xamilo orio",kato_orio)
            #print("timoula",timoula)
            #print("psilo",ano_orio)
            if (timoula >= kato_orio) and (timoula<=ano_orio):
                
                torino_kato_orio=kato_orio
                torino_ano_orio=ano_orio
                teliko_string.append(key)
                break
           
        oliki_lista_pososton=olika_pososta(torino_kato_orio,torino_ano_orio,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
        i+=1
    
    return teliko_string

with open(f"timoula{id}","rb") as file:
    timoula=pickle.load(file)

filename=f"arhiki_lista_sinolon{id}"
with open(filename,'rb') as file:
    lista_arhikon_pososton=pickle.load(file)
    filename=f"xarakthres{id}"
with open(filename,'rb') as file:
    lista_monadikon_xarakthron=pickle.load(file)

#breakpoint()
final_output="".join(decoderv2(timoula,arithmos_bit,lista_arhikon_pososton,lista_monadikon_xarakthron))
#print(final_output)

with open("final_try.bmp","ab") as file:
    file.write(bytes.fromhex(final_output))

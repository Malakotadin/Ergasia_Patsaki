import mpmath as mp
f= open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
#print(bin)
flag=0

#mp.dps=1
#hex_bin=bin.hex()#μετατροπή σε hex
#print(type(hex_bin))
#arithmos_bit=len(hex_bin)
demo_string=bin.hex()
demo_string=demo_string[:15]
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
lista_arhikon_pososton=[]
lista_olikon_poston=[]
metritis_monadikon_xarakthron=0
for key in dictionary_xarakthron_kai_pososton:
    lista_arhikon_pososton.append(dictionary_xarakthron_kai_pososton[key])
    metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
    dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]/arithmos_bit +temp
    lista_olikon_poston.append(dictionary_xarakthron_kai_pososton[key])
    temp= dictionary_xarakthron_kai_pososton[key]
print(dictionary_xarakthron_kai_pososton)
start_range=0
end_range=1
start_range=mp.mpf(start_range)
end_range=mp.mpf(end_range)
print(lista_arhikon_pososton)
lista_arhikon_pososton=[timi/arithmos_bit for timi in lista_arhikon_pososton]
def range_splitter(dictionary_xarakthron_kai_pososton,gramma):
    #apostash=end_range-start_range
    #lista_temp_posoton=[]
   # for i in range(0,metritis_monadikon_xarakthron):
   # lista_temp_posoton.append()
   # breakpoint()
    thessi_grammatos=lista_monadikon_xarakthron.index(gramma)
    temp=lista_arhikon_pososton[thessi_grammatos]
    #temp=dictionary_xarakthron_kai_pososton[gramma]
    for key in dictionary_xarakthron_kai_pososton:
       # breakpoint()
        dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]*temp
    return dictionary_xarakthron_kai_pososton




def character_encoder(char,dictionary_xarakthron_kai_pososton,start_range,end_range):
    #breakpoint()
    end_range=dictionary_xarakthron_kai_pososton[char]
    if char== lista_monadikon_xarakthron[0]and start_range==0:#ελεγχος για να μην μου βαζει το τελικο στοιχειο σαν end range
        print("mpika_peristash")    
    else:
        start_range=dictionary_xarakthron_kai_pososton[lista_monadikon_xarakthron[lista_monadikon_xarakthron.index(char)-1]]
    dictionary_xarakthron_kai_pososton=range_splitter(dictionary_xarakthron_kai_pososton,char)
    print(char)#νιωθω πως μειώνω μόνο την πρώτη τιμή του συνολού
    print("αρχικη τιμη ",start_range)
    print("τελικη τιμη",end_range)
    print(dictionary_xarakthron_kai_pososton)
    return dictionary_xarakthron_kai_pososton,start_range,end_range

for key in dictionary_xarakthron_kai_pososton:
    dictionary_xarakthron_kai_pososton[key]=mp.mpf(dictionary_xarakthron_kai_pososton[key])
for char in demo_string:
    
    dictionary_xarakthron_kai_pososton,start_range,end_range=character_encoder(char,dictionary_xarakthron_kai_pososton,start_range,end_range)
# εδω δουλευει καλα θελω να πιστευω 

timoula=(start_range+end_range)/2
print(timoula)

def iterator(timoula,arithmos_bit,arhiki_lista_sinolon,start,end,decoded_string):
    if arithmos_bit==0:
        return decoded_string
    for i in range(0,len(arhiki_lista_sinolon)):
       # breakpoint()
        if timoula<arhiki_lista_sinolon[0]: #and start==0:# εδω περα ισως να το θελει αυτο , θα το δουμε i guess
            end=arhiki_lista_sinolon[0]
            decoded_string=decoded_string+lista_monadikon_xarakthron[0]
            return iterator(timoula,arithmos_bit-1,[item*lista_arhikon_pososton[0] for item in arhiki_lista_sinolon],start,end,decoded_string)
        elif timoula<arhiki_lista_sinolon[i]:
            print("mpika_elif")
            start=arhiki_lista_sinolon[i-1]
            end=arhiki_lista_sinolon[i]

            decoded_string=decoded_string+lista_monadikon_xarakthron[i]
            print(decoded_string)
            return(timoula,arithmos_bit-1,[item*lista_arhikon_pososton[i] for item in arhiki_lista_sinolon],start,end,decoded_string)
            

        

def decoder(timoula,arithmos_bit,arhiki_lista_sinolon):
    start=0
    end=1
    decoded_string=""
    decoded_string=iterator(timoula,arithmos_bit,arhiki_lista_sinolon,start,end,decoded_string)
    print("bgika_decoder")
    return decoded_string

print(decoder(timoula,arithmos_bit,lista_olikon_poston))
print(demo_string)

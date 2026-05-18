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
demo_string="ffffdddaccdddddcff12335abcdad" 
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

def range_splitter(dictionary_xarakthron_kai_pososton,gramma):
    #apostash=end_range-start_range
    #lista_temp_posoton=[]
   # for i in range(0,metritis_monadikon_xarakthron):
   #     lista_temp_posoton.append()
   temp=dictionary_xarakthron_kai_pososton[gramma]
   for key in dictionary_xarakthron_kai_pososton:
    dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]*temp
    return dictionary_xarakthron_kai_pososton




def character_encoder(char,dictionary_xarakthron_kai_pososton,start_range,end_range):
    #breakpoint()
    end_range=dictionary_xarakthron_kai_pososton[char]
    if char!= lista_monadikon_xarakthron[0]:#ελεγχος για να μην μου βαζει το τελικο στοιχειο σαν end range
        start_range=dictionary_xarakthron_kai_pososton[lista_monadikon_xarakthron[lista_monadikon_xarakthron.index(char)-1]]
    dictionary_xarakthron_kai_pososton=range_splitter(dictionary_xarakthron_kai_pososton,char)
    print("αρχικη τιμη ",start_range)
    print("τελικη τιμη",end_range)
    print(dictionary_xarakthron_kai_pososton)
    return dictionary_xarakthron_kai_pososton,start_range,end_range

for key in dictionary_xarakthron_kai_pososton:
    dictionary_xarakthron_kai_pososton[key]=mp.mpf(dictionary_xarakthron_kai_pososton[key])
for char in demo_string:
    
    dictionary_xarakthron_kai_pososton,start_range,end_range=character_encoder(char,dictionary_xarakthron_kai_pososton,start_range,end_range)



import time
from mpmath import mp
import sys
sys.setrecursionlimit(10**9)
#τι κιαν δεν ταξινομουσα το dictionary , πολυ μικρο κερδος ,αλλα θελω να ειμαι αριστος
f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
#print(bin)
flag=0
mp.dps=1
hex_bin=bin.hex()#μετατροπή σε hex
print(type(hex_bin))
arithmos_bit=len(hex_bin)
print(arithmos_bit)
dictionary_foron={}
hex_bin="0a1b2c3d4e5f6789"
xarakthres=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]


#d = {a:b for a,b in enumerate(list)}

dictionary_foron={"0": 0,"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0,"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0}
for char in hex_bin:
    flag=0
    for key in dictionary_foron:
        if key==char:
            flag=1
          #  print(key,char)
          #  print(dictionary_foron[char])
            dictionary_foron[char]+=1
            break
    if flag==0:
        dictionary_foron.update({char:1})

print(dictionary_foron)
lista_pososton=[]
lista_xarakthra=[]
#descending_ordered_dictionary=dict(sorted(dictionary_foron.items(),key=lamda item: item[1],reverse=True))#καλα επειδη βαριέμαι φριχτά να ακολουθήσω το geeks for geeks απλα θα χάσω 10 λεπτά απο την ζωη μου να κάνω το sort monos mou

def studpid_sort_des(dictionary_foron):
    descending_ordered_dictionary={}
    for i in range(0,len(dictionary_foron)):
        max=0
        key_name=""
        for key in dictionary_foron:
            if dictionary_foron[key]>max:
                
                max=dictionary_foron[key]
                key_name=key
        descending_ordered_dictionary.update({key_name:max})
        #print(key_name)
        dictionary_foron.pop(key_name)
    

    return descending_ordered_dictionary
lista_sinolon=[]
descending_ordered_dictionary=dictionary_foron
for key in descending_ordered_dictionary:
    lista_pososton.append(descending_ordered_dictionary[key]*100/arithmos_bit)

    lista_sinolon.append(mp.mpf(descending_ordered_dictionary[key]/arithmos_bit))
    lista_xarakthra.append(key)
print(lista_sinolon)
print(lista_pososton)#ποσο τις 100 φορές εμφανίζεται αυτός ο χαρακτήρα ς
print(lista_xarakthra)#ταξινομημενη btw
#μαγευτίκα αυτός ο κώδικας δουλεύει αρκετλα καλά , το sorting δεν είναι γρήγορο αλλά δεν με νοιάζει να το κάνει πιο γρήγορο sort κάποιος άλλος
#έστω οτι έχω τους πίνακες ποσοστών και χαρακτήρων και θέλω να κάνω encode την λέξη fab

for i in range(0,len(lista_sinolon)):
    if i==0:
        continue
    lista_sinolon[i]=lista_sinolon[i]+lista_sinolon[i-1]
#εδω πέρα αλλά και γενικότερα η υλοποίηση σηκώνει πολύ optimization
arhiki_lista_sinolon=lista_sinolon                                    
print(lista_sinolon)  
#exit()                   
def letter_to_be_encoded(lista_sinolon,gramma):
    thessi_grammatos=0
    for i in range(0,len(lista_xarakthra)):
       # print(gramma)
        #print(lista_xarakthra[i])
        #print(gramma==lista_xarakthra[i])
        if gramma==lista_xarakthra[i]:
         #   print(i)
          #  print(gramma==lista_xarakthra[i])
           # print("MPIKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            #print(gramma)
            thessi_grammatos=i
           # print(lista_xarakthra[thessi_grammatos])
            
            break

    if thessi_grammatos==0:
        temp_epistrofhs1=0
    else:
        temp_epistrofhs1=lista_sinolon[thessi_grammatos-1]
    kainourgia_lista_sinolon=[sinolo*lista_sinolon[thessi_grammatos]for sinolo in lista_sinolon]
    print(kainourgia_lista_sinolon)
    print("ο χαρακτήρας ",gramma,"βρισκεται μεταξτων τιμών ",mp.mpf(temp_epistrofhs1),"kai",mp.mpf(lista_sinolon[thessi_grammatos]))
    
    return kainourgia_lista_sinolon,temp_epistrofhs1,lista_sinolon[thessi_grammatos]

#letter_to_be_encoded(lista_sinolon,"f")
#παμε να χτίσουμε την συναρτησούλα μας και ίσως να αρχίσουμε να δουλεύουμε μερικές βελτισοτποιήσεις γιατι ο υπολογιστης μου είναι αργος
#εστω string acc
demo_string=hex_bin
counter_foron=0
for char in demo_string:
    counter_foron=counter_foron+1
    print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
    #if counter_foron >300000:
     #   breakpoint()
    lista_sinolon,sinolo_arhi,sinolo_telos=letter_to_be_encoded(lista_sinolon,char)#για παραδειγμά οι δύο βοηθηθτικες μεταβλητές στα σύνολα , δεν χρείαζεται να καταχωρούνται κάθε φορά (ίσα ίσα καλύτερα να βάλω να μην καταχωρουνται τόσες φορές)
    

print("το string  κωδικοποιείται μεταξύ (",sinolo_arhi,",",sinolo_telos,")")#εβαλα κάτι τιμές , και βγαζει ωραία αποτελεσματα μένει να δούμε άμα μπορω να τα αποκωδικοποιήσω
#Έστω οτι τώρα κάνω την decoded  συνάρτηση 
#βασικά δεν έχω τελείωσει με το encoding ακόμα 
#exit()
def binary_searcher(start_range,end_range,starting_value,final_value):
    
    print("start_range",start_range)
    print("end_range",end_range)
    #print("το",(start_range+end_range)/2,"ειναι μεγαλύτερο από το ",final_value)
    if end_range==9.5367431640625e-07:
        pass
     #breakpoint()
   # print(final_value<(start_range+end_range)/2)
    if (start_range+end_range)/2>starting_value and (start_range+end_range)/2<final_value:#start_range>starting_value and end_range<final_value νιωθω οτι αυτό έχει merit αλλα δεν βάζω το χέρι μου στην φωτία 
        print("TELEIOSAAAAAAAAA")
        return -1
    elif final_value<(start_range+end_range)/2:
        print("το",(start_range+end_range)/2,"ειναι μεγαλύτερο από το ",final_value)
        return 0
    elif starting_value>(start_range+end_range)/2:
        print("το",(start_range+end_range)/2,"ειναι μικροτερο  από το ",final_value)
        return 1
    print("kati_ashimo_sinebi")
def binary_encoder(starting_value,final_value):
    #starting_value=starting_value.mpf()
    #final_value=final_value.mpf()
    lista_pou_kouvalaei_to_binary=[]
    start_range=0
    end_range=1 
    start_range=mp.mpf(start_range)
    end_range=mp.mpf(end_range)

    flag=2
    
    while(flag!=-1):
       # print(flag)
        #breakpoint()
        print(flag)
        flag=binary_searcher(start_range,end_range,starting_value,final_value)
        lista_pou_kouvalaei_to_binary.append(flag)
        middle=(start_range+end_range)/2
        if flag==None:
            
            print("teleiosa")
            print("start_range",start_range)
            print("end_range",end_range)
            exit()
            
      #  breakpoint()
        if flag==1:
            
            start_range=middle
            #breakpoint()
           # flag=binary_searcher(start_range,end_range,starting_value,final_value)
        elif flag==0:
           # breakpoint()
            end_range=middle
            
            
           #flag=binary_searcher(start_range,end_range,starting_value,final_value)
    
    return lista_pou_kouvalaei_to_binary       

sinolo_arhi=mp.mpf(sinolo_arhi)
sinolo_telos=mp.mpf(sinolo_telos)
lista_binary=binary_encoder(sinolo_arhi,sinolo_telos)# εστω στο υποθετικό σενάριο οτι αυτό το encoding είναι καλό 
lista_binary.pop()
print(lista_binary)
print(len(lista_binary))
#πρεπει να γινει str ομως
lista_binary=list(map(str,lista_binary))
string_binary="".join(lista_binary)
def reverse_binary_search(binary,start,end):
    print(binary)
    middle=(start+end)/2
    if binary=="":
        return middle
    
    
    char=binary[0]
    if char==str(0):
        start=middle
    else:
        end=middle
    print(middle)
   # print(binary)
    return(reverse_binary_search(binary[1:],start,end))
def binary_decoder(string_binary,arhiki_lista_sinolon):
    start=0
    end=1
    return mp.mpf((reverse_binary_search(string_binary,start,end)))


def decoder_timoulas(timoula,sinola,cap,simboloseira,xarakthres):
    if cap==0:
        return simboloseira
    cap=cap-1
    for i in range(len(sinola)):
        print(i)
        if timoula<sinola[i]:
           

            simboloseira=simboloseira+xarakthres[i]
            
            print(simboloseira)
            return (decoder_timoulas(timoula,[rangie*sinola[i]for rangie in sinola],cap,simboloseira,xarakthres))#κανουμε και τον μαγκα δηθεν , ακομα δεν μου αρεσει το list comprehension αναρωτιεμαι αμα θα το συμπαθησω ποτε
    return simboloseira


timoula=binary_decoder(string_binary,arhiki_lista_sinolon)
print(timoula)
print(arhiki_lista_sinolon)
print(decoder_timoulas(timoula,arhiki_lista_sinolon,len(demo_string),"",xarakthres))

 

    
    

    



#counter=0
#for i in lista_pososton:
 #   counter=counter+i

#print(counter)
# print(lista_sinolon)
import time
from mpmath import mp
import numpy as np
import threading
f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
#print(bin)
flag=0

#mp.dps=1
hex_bin=bin.hex()#μετατροπή σε hex
print(type(hex_bin))
arithmos_bit=len(hex_bin)
print(arithmos_bit)
dictionary_foron={}
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
def kommataki_kodikopoioishs(protoi_128_harakthres,arhiki_lista_sinolon,lista_apotelesmaton,deiktis):
    lista_sinolon=arhiki_lista_sinolon
    for char in protoi_128_harakthres:
      ##  print("έχω ελλεγξει ",a,"χαρακτηρες")
      #  a=a+1
        lista_sinolon,lista_apotelesmaton[deiktis],lista_apotelesmaton[deiktis+1]=letter_to_be_encoded(lista_sinolon,char)#εδω περα θα μπορουσε να πειστρεφει και την ανανεωμενη λιστα συνολων αλλα δεν νομιζω πως χρειαζεται να επιστρεφεται καθε φορα
   # breakpoint()
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
descending_ordered_dictionary=studpid_sort_des(dictionary_foron)
for key in descending_ordered_dictionary:
    lista_pososton.append(descending_ordered_dictionary[key]*100/arithmos_bit)

    lista_sinolon.append(mp.mpf(descending_ordered_dictionary[key]/arithmos_bit))
    lista_xarakthra.append(key)
print(lista_sinolon)
#breakpoint()
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
#breakpoint()        
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
    
    print(type(lista_sinolon))
    kainourgia_lista_sinolon=[sinolo*lista_sinolon[thessi_grammatos]for sinolo in lista_sinolon]
    #kainourgia_lista_sinolon=lista_sinolon*np.array(lista_sinolon[thessi_grammatos])#η εδω πέρα προσπάθεια στην βελτιστοποιηση μου κάνει τον κωδικα να τρέχει 10 φορες πιο αργα
    print(kainourgia_lista_sinolon)
    print("ο χαρακτήρας ",gramma,"βρισκεται μεταξτων τιμών ",mp.mpf(temp_epistrofhs1),"kai",mp.mpf(lista_sinolon[thessi_grammatos]))
    
    return kainourgia_lista_sinolon,temp_epistrofhs1,lista_sinolon[thessi_grammatos]

#letter_to_be_encoded(lista_sinolon,"f")
#παμε να χτίσουμε την συναρτησούλα μας και ίσως να αρχίσουμε να δουλεύουμε μερικές βελτισοτποιήσεις γιατι ο υπολογιστης μου είναι αργος
#εστω string acc
start=time.time()
#demo_string="ca123423abc2312973982173192837023a123423abc2312973982173192837023982130982109382130982192830219384387983babcbdbdbcbbdbababcdbcbdbcdbbabcdbcdbbdbacbadbcbd1a123423abc2312973982173192837023982130982183749817283dff"
demo_string=hex_bin[:100000]
print(len(demo_string))
counter_foron=0
splicing_counter=0
lista_apothikeusis_ton_kommatakion_to_be_encoded=[0]*len(demo_string)
while(splicing_counter!=-1):
    #breakpoint()
    if splicing_counter+128>len(demo_string):   
      #  breakpoint()
        threading.Thread(None,kommataki_kodikopoioishs(demo_string[splicing_counter:len(demo_string)],arhiki_lista_sinolon,lista_apothikeusis_ton_kommatakion_to_be_encoded,counter_foron))
        splicing_counter=-1
    else:
       # breakpoint()
        threading.Thread(None,kommataki_kodikopoioishs(demo_string[splicing_counter:splicing_counter+128],arhiki_lista_sinolon,lista_apothikeusis_ton_kommatakion_to_be_encoded,counter_foron))
        splicing_counter=splicing_counter+128
    
    counter_foron=counter_foron+2
    print("έχω ελλεγξει ",counter_foron/2,"χαρακτηρες")
    print(splicing_counter)
    

end=time.time()
print("διηρκησα τοσα δευτερολεπτα",end-start)
exit()

for char in demo_string:
    counter_foron=counter_foron+1
    print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
    #if counter_foron >300000:
     #   breakpoint()
    lista_sinolon,sinolo_arhi,sinolo_telos=letter_to_be_encoded(lista_sinolon,char)#για παραδειγμά οι δύο βοηθηθτικες μεταβλητές στα σύνολα , δεν χρείαζεται να καταχωρούνται κάθε φορά (ίσα ίσα καλύτερα να βάλω να μην καταχωρουνται τόσες φορές)
    
print(len(demo_string))#θα χωρισω σε καθε 128 bytes
print("το string  κωδικοποιείται μεταξύ (",sinolo_arhi,",",sinolo_telos,")")#εβαλα κάτι τιμές , και βγαζει ωραία αποτελεσματα μένει να δούμε άμα μπορω να τα αποκωδικοποιήσω
#Έστω οτι τώρα κάνω την decoded  συνάρτηση 
#βασικά δεν έχω τελείωσει με το encoding ακόμα 
#exit()
end=time.time()
print("διηρκησα τοσα δευτερολεπτα",end-start)

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
   # starting_value=mp.mpf(starting_value)
  #  final_value=final_value.mpf()
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
def binary_decoder(lista_binary,arhiki_lista_sinolon):
    pass
    

    



#counter=0
#for i in lista_pososton:
 #   counter=counter+i

#print(counter)
# print(lista_sinolon)
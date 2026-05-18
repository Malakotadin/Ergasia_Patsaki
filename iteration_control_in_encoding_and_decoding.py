import mpmath as mp
#ωρα να σκεφτω τον binary decoder  .  έστω οτι μου έρχεται το 0,0,0,0,1,1 και έστω οτι τα σύνολα μου είναι Α40% , Β30 C20% ,D10% 
#κανοντας απλα διαδική αναζητηση θα βρω έναν αριθμο πολυ ευκολα , ο οποίος θα είναι 

start=0
end=1


binary="010101001"
demo_string="dbcdabcddb"
 
arithmos_bit=len(demo_string)
#xarakthres=["a,b,c,d"]
dictionary_foron={"a": 0,"b": 0,"c": 0,"d": 0}
for char in demo_string:
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
lista_sinolon=[]
descending_ordered_dictionary=dictionary_foron
for key in descending_ordered_dictionary:
    lista_pososton.append(descending_ordered_dictionary[key]*100/arithmos_bit)

    lista_sinolon.append(mp.mpf(descending_ordered_dictionary[key]/arithmos_bit))
    lista_xarakthra.append(key) 
authetntiki_lista_sinolon=lista_sinolon#πχ 20,20,20,20,20
for i in range(0,len(lista_sinolon)):
    if i==0:
        continue
    lista_sinolon[i]=lista_sinolon[i]+lista_sinolon[i-1]

arhiki_lista_sinolon=lista_sinolon       #πχ 0,20,40,60,80,100                             
print(lista_sinolon) 
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
    #breakpoint()#τωρα εδω ισως έχει γίνει παπαρια αλλα εγω λεω το κραταμε σαν σκεψη
    kainourgia_lista_sinolon=[sinolo*authetntiki_lista_sinolon[thessi_grammatos]for sinolo in lista_sinolon]#!!!ΣΗΜΑΝΤΙΚΟ εδω πέρα κάνω μαλακια και τα πολλαπλασιαζω με το αυξημενο ολικο ποσοστο όχι με το αυθεντικο ποσοστό τους ( πχ αμα ο τελευταιος χαρακτήρα ειναι 10% εγω πολλαπλασιαζω με 100 και οχι με 10)
    print(kainourgia_lista_sinolon)
    print("ο χαρακτήρας ",gramma,"βρισκεται μεταξτων τιμών ",mp.mpf(temp_epistrofhs1),"kai",mp.mpf(lista_sinolon[thessi_grammatos]))
    
    return kainourgia_lista_sinolon,temp_epistrofhs1,lista_sinolon[thessi_grammatos]

#letter_to_be_encoded(lista_sinolon,"f")
#παμε να χτίσουμε την συναρτησούλα μας και ίσως να αρχίσουμε να δουλεύουμε μερικές βελτισοτποιήσεις γιατι ο υπολογιστης μου είναι αργος
#εστω string acc

counter_foron=0
for char in demo_string:
    
    #if counter_foron >300000:
    
    lista_sinolon,sinolo_arhi,sinolo_telos=letter_to_be_encoded(lista_sinolon,char)#για παραδειγμά οι δύο βοηθηθτικες μεταβλητές στα σύνολα , δεν χρείαζεται να καταχωρούνται κάθε φορά (ίσα ίσα καλύτερα να βάλω να μην καταχωρουνται τόσες φορές)
    counter_foron=counter_foron+1
    print("έχω ελλεγξει ",counter_foron,"χαρακτηρες")
   # breakpoint()

print("το string  κωδικοποιείται μεταξύ (",sinolo_arhi,",",sinolo_telos,")")#εβαλα κάτι τιμές , και βγαζει ωραία αποτελεσματα μένει να δούμε άμα μπορω να τα αποκωδικοποιήσω
#Έστω οτι τώρα κάνω την decoded  συνάρτηση 
mesos=(sinolo_arhi+sinolo_telos)/2
#βασικά δεν έχω τελείωσει με το encoding ακόμα 
exit()
def binary_searcher(start_range,end_range,starting_value,final_value):
   
    print("start_range",start_range)
    print("end_range",end_range)
    middle=(start_range+end_range)/2
    print("middle",middle)
   # breakpoint()
   
   # #print("το",(start_range+end_range)/2,"ειναι μεγαλύτερο από το ",final_value)
   # if end_range==9.5367431640625e-07:
    #pass
     #breakpoint()
   # print(final_value<(start_range+end_range)/2)
    if middle/2>starting_value and middle/2<final_value:#start_range>starting_value and end_range<final_value νιωθω οτι αυτό έχει merit αλλα δεν βάζω το χέρι μου στην φωτία 
        print("to ",middle,"ειναι αναμεσα στο αρχικο",starting_value,"και στο τελικο",final_value)

        return -1
    elif starting_value>middle:
        print("το",middle/2,"ειναι μικροτερο  από το ",final_value)
        return 1
    elif final_value<middle: 
        print("το",middle/2,"ειναι μεγαλύτερο από το ",final_value)
        return 0
   
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
#exit()
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
           
           # breakpoint()
            simboloseira=simboloseira+xarakthres[i]
            
            print(simboloseira)
            return (decoder_timoulas(timoula,[rangie*sinola[i]for rangie in sinola],cap,simboloseira,xarakthres))#κανουμε και τον μαγκα δηθεν , ακομα δεν μου αρεσει το list comprehension αναρωτιεμαι αμα θα το συμπαθησω ποτε
    return simboloseira

#def decoder_timoulas(timoula,sinola,cap,simboloseira,xarakthres):
#    if cap==0:
#       return simboloseira
 #   cap=cap-1
 #   for i in range(len(sinola)):
 #       print(i)
 #       if timoula<sinola[i]:
#           
#            breakpoint()
#            simboloseira=simboloseira+xarakthres[i]
#           
#            print(simboloseira)
#            return (decoder_timoulas(timoula,[rangie*sinola[i]for rangie in sinola],cap,simboloseira,xarakthres))#κανουμε και τον μαγκα δηθεν , ακομα δεν μου αρεσει το list comprehension αναρωτιεμαι αμα θα το συμπαθησω ποτε
#    return simboloseira

xarakthres=["a","b","c","d"] 
timoula=binary_decoder(string_binary,arhiki_lista_sinolon)
print(timoula)
print(arhiki_lista_sinolon)
print(decoder_timoulas(timoula,arhiki_lista_sinolon,len(demo_string),"",xarakthres))

     
#exit()
#counter=0
#for i in lista_pososton:
 #   counter=counter+i

#print(counter)
# print(lista_sinolon)
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
    

timoula=reverse_binary_search(binary,start,end)
        
#ωραια εστω οτι αυτό δουλεύει , ήρθε η ώρα να παμω στον αποκωδικοποιητη μικρης τιμουλας σε χαρακτήρες 
sinola=[0.1,0.4,0.6,1] 
xarakthres=["a","b","c","d"]   #νιωθω πως το 1 δεν θα επρεπε να υπαρχει , αυτο είναι ειτε ασημαντο είτε λαθος
cap=len(binary)
print(len(xarakthres))
simboloseira=""

print(decoder_timoulas(timoula,sinola,cap,simboloseira,xarakthres))


f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
#print(bin)
flag=0

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
    lista_sinolon.append(descending_ordered_dictionary[key]/arithmos_bit)
    lista_xarakthra.append(key)
print(lista_sinolon)
print(lista_pososton)#ποσο τις 100 φορές εμφανίζεται αυτός ο χαρακτήρα ς
print(lista_xarakthra)#ταξινομημενη btw
#μαγευτίκα αυτός ο κώδικας δουλεύει αρκετλα καλά , το sorting δεν είναι γρήγορο αλλά δεν με νοιάζει να το κάνει πιο γρήγορο sort κάποιος άλλος
#έστω οτι έχω τους πίνακες ποσοστών και χαρακτήρων και θέλω να κάνω encode την λέξη faggacab

for i in range(0,len(lista_sinolon)):
    if i==0:
        continue
    lista_sinolon[i]=lista_sinolon[i]+lista_sinolon[i-1]
#εδω πέρα αλλά και γενικότερα η υλοποίηση σηκώνει πολύ optimization
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
    kainourgia_lista_sinolon=[sinolo*lista_sinolon[thessi_grammatos]for sinolo in lista_sinolon]
    print(kainourgia_lista_sinolon)
    print("ο χαρακτήρας ",gramma,"βρισκεται μεταξτων τιμών ",temp_epistrofhs1,"kai",lista_sinolon[thessi_grammatos])
    return kainourgia_lista_sinolon,temp_epistrofhs1,lista_sinolon[thessi_grammatos]

letter_to_be_encoded(lista_sinolon,"f")
            


#counter=0
#for i in lista_pososton:
 #   counter=counter+i

#print(counter)
# print(lista_sinolon)
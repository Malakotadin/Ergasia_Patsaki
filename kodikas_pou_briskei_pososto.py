import operator
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

descending_ordered_dictionary=studpid_sort_des(dictionary_foron)
for key in descending_ordered_dictionary:
    lista_pososton.append(descending_ordered_dictionary[key]*100/arithmos_bit)
    lista_xarakthra.append(key)

print(lista_pososton)#ποσο τις 100 φορές εμφανίζεται αυτός ο χαρακτήρα ς
print(lista_xarakthra)
#μαγευτίκα αυτός ο κώδικας δουλεύει αρκετλα καλά , το sorting δεν είναι γρήγορο αλλά δεν με νοιάζει να το κάνει πιο γρήγορο sort κάποιος άλλος
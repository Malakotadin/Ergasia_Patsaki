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
demo_string="aksdjfkjdshfksjadhfksdfasdfsadfasdfadsf"
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
        print(len(lista_olikon_poston)-i)
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

print(encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string))#ωραια αυτο επιστρεφει επιτυχως τιμη
#exit()
def range_splitter(dictionary_xarakthron_kai_pososton,gramma):
    #apostash=end_range-start_range
    #lista_temp_posoton=[]
   # for i in ran#ge(0,metritis_monadikon_xarakthron):
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

print(timoula)
#breakpoint()
#exit()
print(decoder(timoula,arithmos_bit,lista_olikon_poston))
print(demo_string)

'''
def concatenate_char(ls):  # O(n)
    string = ''
    for e in ls:  # O(n)
        string += e
    return string


def get_cumulative_sum(lower_bound, upper_bound, probability_ls):  # O(n) (where append to a list takes O(1) amortized)
    cumulative_sum = [lower_bound]
    diff_btw_two_bounds = upper_bound - lower_bound
    char_lower_bound = lower_bound
    for probability in probability_ls:  # O(n)
        char_upper_bound = char_lower_bound + (diff_btw_two_bounds * probability)
        cumulative_sum.append(char_upper_bound)  # O(1) amortized
        char_lower_bound = char_upper_bound
    return cumulative_sum

def associate_key_with_interval(cumulative_sum, unique_char):  # O(n) (where adding to a dictionary O(1) average case)
    # use a dictionary where
    #   the key is the unique character
    #   the value is a list of length 2 where
    #       - the first element is the lower bound
    #       - the second element is the upper bound
    interval = {}
    i = 0
    j = 0
    while i < len(cumulative_sum) - 1:  # O(n)
        key = unique_char[j]
        lower_bound = cumulative_sum[i]
        upper_bound = cumulative_sum[i + 1]
        interval[key] = [lower_bound, upper_bound]  # Average case O(1) or Amortized worst case O(n)
        i += 1
        j += 1
    return interval
def arithmetic_decoding(probability, message_length, tag):  # O(n^2)
    # put all values from probability dictionary into a probability list
    # put all keys from probability dictionary into a unique_char list
    probability_ls = lista_arhikon_pososton
    unique_char = lista_monadikon_xarakthron
   # for key, value in probability.items():  # O(n)
    #    probability_ls.append(value)  # O(1) amortized
     #   unique_char.append(key)  # O(1) amortized
    # then use the probability list to calculate cumulative sum of probability_ls
    # initially, the lower bound is 0.0 and the upper bound is 1.0
    cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls)  # O(n) (where append to a list takes O(1) amortized)
    # associate each key with its interval
    interval_dict = associate_key_with_interval(cumulative_sum,
                                                unique_char)  # O(n) (where adding to a dictionary O(1) average case)

    i = 0
    message_char_ls = []
    current_lower_bound = 0.0
    current_upper_bound = 1.0
    while i < message_length:  # O(n)
        for key, value in interval_dict.items():  # O(n)
            # get the interval of the current character (key)
            lower_bound = value[0]
            upper_bound = value[1]
            # check if tag is within the interval of the current character (key)
            if (tag > lower_bound) and (tag < upper_bound):
                # narrow down the interval
                current_lower_bound = lower_bound
                current_upper_bound = upper_bound
                # add the character to message_char_ls if tag is within the interval of the current character (key)
                message_char_ls.append(key)  # O(1) amortized
                break
        # every time the interval is narrowed down:
        #   - get the new cumulative sum for the new interval
        #   - each key will have a new lower and upper bound in the new interval
        cumulative_sum = get_cumulative_sum(current_lower_bound, current_upper_bound,
                                            probability_ls)  # O(n) (where append to a list takes O(1) amortized)
        interval_dict = associate_key_with_interval(cumulative_sum,
                                                    unique_char)  # O(n) (where adding to a dictionary O(1) average case)
        i += 1

    return concatenate_char(message_char_ls)

print(arithmetic_decoding(lista_arhikon_pososton,arithmos_bit,timoula))'''#γαμω το σπιτι μου γαμω το κερατο μου
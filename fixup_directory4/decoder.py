#ωρα να σκεφτω τον binary decoder  .  έστω οτι μου έρχεται το 0,0,0,0,1,1 και έστω οτι τα σύνολα μου είναι Α40% , Β30 C20% ,D10% 
#κανοντας απλα διαδική αναζητηση θα βρω έναν αριθμο πολυ ευκολα , ο οποίος θα είναι 
import mpmath as mp
start=0
end=1
start=mp.mpf(start)
end=mp.mpf(end)
midenika=444*[0]
midenika=list(map(str,midenika))
binary="".join(midenika)

 
def reverse_binary_search(binary,start,end):
    print(binary)
    middle=mp.mpf((start+end)/2)
    if binary=="":
        return middle
    
    
    char=binary[0]
    if char==str(0):
        start=middle
        #breakpoint()
    else:
        end=middle
    print(middle)
  #  breakpoint()
   # print(binary)
    return(reverse_binary_search(binary[1:],start,end))
    

timoula=reverse_binary_search(binary,start,end)
        
#ωραια εστω οτι αυτό δουλεύει , ήρθε η ώρα να παμω στον αποκωδικοποιητη μικρης τιμουλας σε χαρακτήρες 
sinola=[0.4,0.7,0.9,1] 
xarakthres=["a","b","c","d"]   #νιωθω πως το 1 δεν θα επρεπε να υπαρχει , αυτο είναι ειτε ασημαντο είτε λαθος
cap=len(binary)
simboloseira=""
def decoder_timoulas(timoula,sinola,cap,simboloseira,xarakthres):
    if cap==0:
        return simboloseira
    cap=cap-1
    for i in range(len(sinola)):
        print(i)
        if timoula<sinola[i]:
           

            simboloseira=simboloseira+xarakthres[i]
            print(sinola)
            print(simboloseira)
            return (decoder_timoulas(timoula,[rangie*sinola[i]for rangie in sinola],cap,simboloseira,xarakthres))#κανουμε και τον μαγκα δηθεν , ακομα δεν μου αρεσει το list comprehension αναρωτιεμαι αμα θα το συμπαθησω ποτε
    return simboloseira

print(decoder_timoulas(timoula,sinola,cap,simboloseira,xarakthres))


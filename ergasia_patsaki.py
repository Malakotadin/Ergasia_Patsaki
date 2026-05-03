
f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
print(type(bin))
with open("face_bytes_real.png","wb") as f:#εδω απλα τυπωνω ολα τα bytes της φωτογραφίας και βγαινει η φωτογραφια
    f.write(bin) 
#Αυτός ο κώδικας είναι ολίγον τι χρονοβόρος , άμα μπορουσα να βρω τρόπο να τον κάνω πιο γρήγορο θα ημουν πολύ χαρούμενος 
str_bin=bin.__str__()
decoded_bytes=bin.decode('utf-8','ignore')#είτε ignore βαλω  είτε replace τα ίδια σκατα είναι 
hex_bin=bin.hex()
#hex_bin=str_bin.hex()
#hex_bin=hex(int(bin))#ηρθε η ωρα για λιγη μαγεια#ακα μετατρέπω τα binaries σε δεκαεξαδικο 
with open("hexed_bytes.png","br+") as f: 
    f.write(bytes.fromhex(hex_bin))#αυτό είναι πάρα πολύ καλό γιατί επίσης έχουμε την φωτογραφία γιουπιιιι :)))))
kommena_bytes=[str_bin[i:i+2]for i in range(0,len(str_bin),2)]# Αυτη η γραμμη κοβει ολα τα bytes ανα bytes ( 8 bit ) και τα πετάει σε μια λίστα μπας και μπορουμε να κάνουμε κάτι με αυτά 
#print(str_bin)
#print(kommena_bytes)
print(decoded_bytes)
encoded_bytes=decoded_bytes.encode()
#print(encoded_bytes)

with open("face_bytes.png","wb") as f:#εδω απλα τυπωνω ολα τα bytes της φωτογραφίας και δεν βγαινει η φωτογραφία ... γιατι ???
  f.write(encoded_bytes)     #αυτό και το αποκάτω βγάζουν το ίδιο αποτέλεσμα που βγάζει νόημα γιατι τυπώνουν πάνω κάτω το ίδιο πράγμα#με αυτή την μετατρόπη ΣΧΕΔΟΝ βγάζει την φωτογραφία απλώς τρώει τα πρώτα 8 bytes καταταλλα ειναι καλο 
   # f.write(bytes(bin,"utf-8"))# η απάντηση είναι ξέρω γιατι , γιατί τιπώνονται και τα μέρη του string που δενθαπρεπε όπως τα b' και τα\x καταταλλα τα bytes ειναι απαράλλαχτα 

with open("kathara_face_bytes.png","wb") as f: #εδω θα ηθελα να εχουν βγει τα σατανικα \\χ απο αυτά γιατι μου κανουν την ζωη λιγο δυσκολη πιστεύω , θα δούμε
    f.write(bytes(str_bin,"'iso-8859-1'"))#ειναι και αυτό αρκέτα κοντά νομίζω
    #αυτό το θέμα με τους υπόλοιπους τρόπους εγγραφής μπορουν να το λύσουν και τα άλλα παιδία 
#μπορείτε να δείτε πόσο κοντά είναι κάθε μέθοδος μέσω τοu ghex(ή κάποιου άλλου hex editor )
 
 


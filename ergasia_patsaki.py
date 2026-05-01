f = open('/home/meow/pytohn_codes/ergasia_patsaki/ff6.jpg','rb')
bin = f.read()
f.close()
with open("face_bytes_real.png","wb") as f:#εδω απλα τυπωνω ολα τα bytes της φωτογραφίας και βγαινει η φωτοραδια
    f.write(bin)
#Αυτός ο κώδικας είναι ολίγον τι χρονοβόρος , άμα μπορουσα να βρω τρόπο να τον κάνω πιο γρήγορο θα ημουν πολύ χαρούμενος 
str_bin=bin.__str__()
#hex_bin=str_bin.hex()
hex_bin=hex(int(bin))#ηρθε η ωρα για λιγη μαγεια#ακα μετατρέπω τα binaries σε δεκαεξαδικο 
with open("hexed_bytes","w+") as f: 
    f.write(hex_bin)
kommena_bytes=[str_bin[i:i+2]for i in range(0,len(str_bin),2)]# Αυτη η γραμμη κοβει ολα τα bytes ανα bytes ( 8 bit ) και τα πετάει σε μια λίστα μπας και μπορουμε να κάνουμε κάτι με αυτά 
print(str_bin)
print(kommena_bytes)
encoded_bytes=str_bin.encode("'iso-8859-1'")
print(encoded_bytes)
with open("face_bytes.png","wb") as f:#εδω απλα τυπωνω ολα τα bytes της φωτογραφίας και δεν βγαινει η φωτογραφία ... γιατι ???
  f.write(encoded_bytes)
   # f.write(bytes(bin,"utf-8"))# η απάντηση είναι ξέρω γιατι , γιατί τιπώνονται και τα μέρη του string που δενθαπρεπε όπως τα b' και τα\x καταταλλα τα bytes ειναι απαράλλαχτα 

with open("kathara_face_bytes","w+") as f: #εδω θα ηθελα να εχουν βγει τα σατανικα \\χ απο αυτά γιατι μου κανουν την ζωη λιγο δυσκολη πιστεύω , θα δούμε
    f.write("".join(str_bin))
import subprocess
image_path='gimp.bmp'
f= open(image_path,'rb')
bint = f.read()
f.close()
demo_string=bint.hex()
splicing_counter=0
arg=demo_string[:256]
noumero=0
strnoumero=str(noumero)
print(arg)
#exit()
breakpoint()
while(True):
    if splicing_counter+256>len(demo_string):
        diafora=len(demo_string)-splicing_counter
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        
        subprocess.run(['python','encode_to_files2.py',arg,strnoumero])
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+256]
        subprocess.run(['python','encode_to_files2.py',arg,strnoumero])
    noumero+=1
    strnoumero=str(noumero)
    splicing_counter+=256
    print(splicing_counter)
    

endno=int(strnoumero)
noumero=0
strnoumero=str(noumero)
breakpoint()
while(True):
    #breakpoint()
    #print(noumero)
   # print(noumero>endno)
    subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    if endno==noumero:
        print("teleiosa")
        break
    noumero+=1
    strnoumero=str(noumero)
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])


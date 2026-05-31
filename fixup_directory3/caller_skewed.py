import subprocess
image_path='gimp.bmp'
f= open(image_path,'rb')
bin = f.read()
f.close()
demo_string=bin.hex()
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
while(True):
    
    subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    if endno!=noumero:
        subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    else:
        subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero,diafora])
        print("teleiosa")

    noumero+=1
    strnoumero=str(noumero)
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])


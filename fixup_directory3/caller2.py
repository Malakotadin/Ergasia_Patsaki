import subprocess
from mpmath import mp,mpf
import time,sys
import pickle

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
infinite_mhden=mp.mpf(0.0)
tag_ls=len(demo_string)*infinite_mhden
breakpoint()
while(True):
    if splicing_counter+256>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        tag_ls[noumero]=subprocess.check_output(['python','encode_to_files2.py',arg,strnoumero])
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+256]
        tag_ls[noumero]=subprocess.check_output(['python','encode_to_files2.py',arg,strnoumero])
    noumero+=1
    strnoumero=str(noumero)
    splicing_counter+=256
    print(splicing_counter)
    
exit()
endno=int(strnoumero)
noumero=0
strnoumero=str(noumero)
while(True):
    
    subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])
    if endno==noumero:
        print("teleiosa")
        break
    noumero+=1
    strnoumero=str(noumero)
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])



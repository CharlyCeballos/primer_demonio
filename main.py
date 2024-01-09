import threading, time, msvcrt

def tiempo():
    contador = 10
    mensaje = 'El demonio ha muerto!!!!!!'
    print()
    while contador > 0:
        time.sleep(1)
        contador -= 1
        print(contador, 'Segundos restantes')
    print()
    print(mensaje.upper())

x = threading.Thread(target=tiempo, daemon=True)
'''Si esta comentado: Se detiene al presionar una tecla
Si se setea False: No importan las entradas'''
x.setDaemon(False)
x.start()

print('Desea salir? [Y/n]')
entrada = msvcrt.getch()
if entrada and not x.isDaemon():
    print('PUES NO PUEDES 😈')
print()

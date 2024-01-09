import threading, time

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
x.setDaemon(False)
x.start()

print(x.isDaemon())

entrada = input(f'Desea salir? [Y/n] \n')
if entrada:
    print('PUES NO PUEDES 😈')
print()

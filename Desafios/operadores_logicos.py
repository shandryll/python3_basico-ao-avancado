trabalho_terca = True
trabalho_quinta = False

if trabalho_terca and trabalho_quinta:
    print("Comprar TV 50' + Sorvete")

elif trabalho_terca and not trabalho_quinta or not trabalho_terca and trabalho_quinta:
    print("Comprar TV 32' + Sorvete")

elif not trabalho_terca and not trabalho_quinta:
    print("Ficar em casa")
from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Maria', 44)
    vendedor = Vendedor('Pedro', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra (cliente, datetime.now(2018, 6, 4), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adult() else '')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_compras} compras')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()

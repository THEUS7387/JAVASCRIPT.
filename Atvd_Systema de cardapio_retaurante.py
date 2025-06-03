import os
from dataclasses import dataclass
os.system("cls || clear")

class Prato:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.codigo} - {self.nome} - R$ {self.preco:.2f}"


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, prato):
        self.itens.append(prato)

    def calcular_subtotal(self):
        return sum(prato.preco for prato in self.itens)

    def listar_itens(self):
        for prato in self.itens:
            print(f"{prato.codigo} - {prato.nome} - R$ {prato.preco:.2f}")


class Restaurante:
    def __init__(self):
        self.cardapio = self._criar_cardapio()
        self.pedido = Pedido()

    def _criar_cardapio(self):
        return {
            1: Prato(1, "Feijoada", 25.0),
            2: Prato(2, "Lasanha", 22.5),
            3: Prato(3, "Strogonoff", 24.0),
            4: Prato(4, "Frango Grelhado", 20.0),
            5: Prato(5, "Sushi", 30.0),
            6: Prato(6, "Hambúrguer Artesanal", 18.5),
            7: Prato(7, "Salada Vegana", 17.0),
        }

    def exibir_menu(self):
        print("\n--- CARDÁPIO ---")
        for prato in self.cardapio.values():
            print(prato)
        print("0 - Finalizar pedido")

    def fazer_pedido(self):
        while True:
            try:
                codigo = int(input("\nDigite o código do prato (ou 0 para finalizar): "))
                if codigo == 0:
                    break
                elif codigo in self.cardapio:
                    self.pedido.adicionar_item(self.cardapio[codigo])
                    print(f" {self.cardapio[codigo].nome} adicionado ao pedido.")
                else:
                    print("Código inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def escolher_pagamento(self):
        while True:
            print("\nForma de pagamento:")
            print("1 - À vista (10% de desconto)")
            print("2 - Cartão de crédito (10% de acréscimo)")
            opcao = input("Escolha a forma de pagamento (1 ou 2): ")
            if opcao in ['1', '2']:
                return opcao
            print("Opção inválida. Tente novamente.")

    def mostrar_resumo(self, forma_pagamento):
        print("\n--- RESUMO DO PEDIDO ---")
        self.pedido.listar_itens()
        subtotal = self.pedido.calcular_subtotal()
        print(f"\nSubtotal: R$ {subtotal:.2f}")

        if forma_pagamento == '1':
            desconto = subtotal * 0.10
            total = subtotal - desconto
            print("Forma de pagamento: À vista")
            print(f"Desconto aplicado: R$ {desconto:.2f}")
        else:
            acrescimo = subtotal * 0.10
            total = subtotal + acrescimo
            print("Forma de pagamento: Cartão de crédito")
            print(f"Acréscimo aplicado: R$ {acrescimo:.2f}")

        print(f"Total a pagar: R$ {total:.2f}")

    def iniciar(self):
        self.exibir_menu()
        self.fazer_pedido()

        if not self.pedido.itens:
            print("\nNenhum pedido realizado.")
            return

        forma_pagamento = self.escolher_pagamento()
        self.mostrar_resumo(forma_pagamento)


if __name__ == "__main__":
    restaurante = Restaurante()
    restaurante.iniciar()
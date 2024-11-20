import json
import time
import os
# compras = {}

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]
    

def visualizar_compras(compras):
    for item , quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print()
    print("Precione Enter Para continuar")
    input()
        


def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)


def carregar_compras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return json.load(arquivo)
    


def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Adicionar item")
        print("2 Remover item")
        print("3 Vizualizar Lista")
        print("4 Salvar e Sair")
        print("5 Sair sem salvar")
        escolha2 = input("Escolhe uma opção: ")
        
        if escolha2 == "1":
            nome_item = input("Digite nome do Item: ")
            quantidade_item = float(input("Digite quantidade do Item: "))
            adicionar_item(compras, nome_item, quantidade_item)
   
        elif escolha2 == "2":
            itemdeletar = input("Digite item que deseja excluir: ")
            remover_item(compras, itemdeletar)
            time.sleep(2)
            
        elif escolha2 == "3":
            visualizar_compras(compras)
            
        elif escolha2 == "4":
            if nome_arquivo is None:
                nome_arquivo = input("Digite nome do arquivo: ")
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)
            break
            
            
        elif escolha2 == "5":
            break
        else:
            print("Ops! Escolha Inválida")
            time.sleep(2)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Criar uma nova lista de compra")
        print("2 Caregar uma lista existente")
        print("3 Sair")
        escolha = input("Escolhe uma opção: ")
        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)
         
        elif escolha == "2":
          
          print("Listas disponiveis:")
          arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]
          #print(arquivos)
          if not arquivos:
            print("Nenhum arquivo encontrada.")
            time.sleep(3)
            continue
            
          for i, arquivo in enumerate(arquivos, 1):
            print(f"{i} {arquivo}")
          escolha = int(input("Escolhe um arquivo para carregar (0 se nenhum) "))
          if escolha == 0:
            continue
          if escolha < 0 or escolha > len(arquivos):
            print("Ops! Escolha Inválida")
            time.sleep(2)
            continue
          compras = carregar_compras(arquivos[escolha - 1])
          nome_arquivo = arquivos[escolha - 1]
          gerenciar_compras(compras, nome_arquivo)
          
            
        elif escolha == "3":
            break
        else:
            print("Ops! Opção invalida")
            time.sleep(2)
if __name__ == "__main__":
    main()
    
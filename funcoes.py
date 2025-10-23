import os
import datetime

nome = " "
quantidade = 0
preco = 0.0

estoque_da_loja = []    
id = 1  # Variável global para controlar o próximo ID

def limpar_terminal():
     os.system("cls")
     
# Caminhos dos arquivos 

ARQUIVOS_DADOS = "dados/estoque.csv"
ARQUIVO_LOG = "dados/log.txt"




  
                

def cadastrar_produto():
        print ("/n=== Cadastrar produto ===")
        nome =input("Digite o nome do produto: ").split()
        quantidade =int(input("Digite a quantidade de produtos: "))
        preço = float(input("digite o preço do produto: "))
        
    


# (Requisito 7) Usando um dicionário para organizar o produto
novo_produto = {
        "id": id,
        "nome": nome,
        "preco": preco
    }
    
    # Adiciona o produto à nossa lista
estoque_da_loja.append(novo_produto)
    
    # Incrementa o ID para o próximo cadastro
id += 1


        
        
 
def listar_produtos(): # Percorre a lista 'estoque' e imprime cada item.  
    print("\n--- Lista de Produtos ---")
    
    if not estoque_da_loja: # Verifica se a lista está vazia
        print("Nenhum produto cadastrado ainda.")
        return
    
    for produto in estoque_da_loja:
        
        print(f"ID: {id} | Nome: {nome} | Preço: R$ {preco:.2f}")
        
        # print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}") # Imprime os dados de cada produto





'''def editar_produtos(): #edita um produto existente no estoque.
        print("/n=== Editar produto ===")
        if not estoque_da_loja:
            print("Esse item não está cadastrado em nosso estoque.")
            return
        listar_produtos() #mostra os produtos antes de editar.
        # id_editar = int(input("\Digite o ID do produto que deseja editar: "))
        
        produto = next((item for item in estoque_da_loja if item ["id"] == id_editar ), None)

        if produto is None: 
            print("Produto não encontrado!")
            return

        print(f"\nProduto selecionado: {produto['nome']}")
        print("Deixe o campo vazio para manter o valor atual. \n")'''

'''def excluir_item(): #remove o produto desejado do estoque
    print("\n === Excluir produtos === ")

    if not estoque_da_loja: '''
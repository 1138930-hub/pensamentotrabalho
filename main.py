from funcoes import limpar_terminal
from funcoes import cadastrar_produto 
from funcoes import listar_produtos

#id do produto
id = 1

# Lista de vai guardar os produtos na memória 
estoque_da_loja = []  

print("\n=== CONTROLE DE ESTOQUE ===")
print("1. Cadastrar produto")
print("2. Listar produtos")
print("3. Editar  produto")
print("4. Excluir produto")
print("5. Sair")

escolha_do_usuario = 0

#fiz uma alteração

# limpar_terminal()

while True:
    escolha_do_usuario =int(input("digite uma opcão: "))
    if escolha_do_usuario == 1:
                print("Cadastrar produto: ")
                cadastrar_produto()
                continue
    elif escolha_do_usuario == 2:
                print("Listar produtoss")
                listar_produtos()
                continue
    elif escolha_do_usuario == 3:
                print("Editar produto")
    elif escolha_do_usuario == 4:
                print("Excluir produto")
    elif escolha_do_usuario == 5:
                print("Sair")
                break
    else:  
                print("Opção invalida, tente novamente!")
                escolha_do_usuario =int(input("digite uma opcão: "))



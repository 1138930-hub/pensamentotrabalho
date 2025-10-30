import os
import csv
import datetime

ARQUIVO_DADOS = "dados/estoque.csv"
ARQUIVO_LOG = "dados/log.txt"



def limpar_terminal(): #Limpa o terminal para ficar mais organizado
    os.system("cls")


def salvar_estoque_csv(estoque_da_loja): #Salva os produtos no arquivo estoque.CSV
    os.makedirs("dados", exist_ok=True)

    with open(ARQUIVO_DADOS, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "quantidade", "preco"])
        for produto in estoque_da_loja:
            escritor.writerow([
                produto["id"],
                produto["nome"],
                produto["quantidade"],
                produto["preco"]
            ])


def registrar_log(acao, nome_produto): #Registra as ações feitas no menu interativo, e registra no arquivo log.txt
    
    momento = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_LOG, mode="a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{momento}] {acao}: {nome_produto}\n")
        
def carregar_estoque_csv():

    estoque_da_loja = []

    if not os.path.exists(ARQUIVO_DADOS):
        return estoque_da_loja, 1

    with open(ARQUIVO_DADOS, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        max_id = 0
        for linha in leitor:
            try:
                produto = {
                    "id": int(linha["id"]),
                    "nome": linha["nome"],
                    "quantidade": int(linha["quantidade"]),
                    "preco": float(linha["preco"])
                }
                estoque_da_loja.append(produto)
                if produto["id"] > max_id:
                    max_id = produto["id"]
            except (KeyError, ValueError):
                continue

    return estoque_da_loja, (max_id + 1 if max_id >= 1 else 1)
        
def main():
    estoque_da_loja, id_produto = carregar_estoque_csv() #Carrega o arquivo estoque.CSV e o último ID cadastrado. 

    while True:
        print('''
            ==== CONTROLE DE ESTOQUE ==== 
            ==== MENU PRINCIPAL ====
            1. Cadastrar produtos
            2. Listar produtos
            3. Editar produto 
            4. Excluir produto
            5. Limpar toda a lista de produtos
            6. Sair
            =============================
            ''')

        try:
            escolha_do_usuario = int(input("escolha uma opcão: "))
        except ValueError:
                print("Digite apenas número que contém no menu!")
                continue
        
        limpar_terminal()

        if escolha_do_usuario == 1:
                    print("Cadastrar produto: ")
                    cadastrar_produto(estoque_da_loja)

        elif escolha_do_usuario == 2:
                    print("Listar produtos")
                    listar_produtos(estoque_da_loja)

        elif escolha_do_usuario == 3:
                    print("Editar produto")
                    editar_produto(estoque_da_loja)

        elif escolha_do_usuario == 4:
                    print("Excluir produto")
                    excluir_produto(estoque_da_loja)
        elif escolha_do_usuario == 5:
                    print("Limpar toda a lista de produtos")
                    limpar_lista(lista_produtos=estoque_da_loja)

        elif escolha_do_usuario == 6:
                    print("Saindo, obrigado por utilizar nosso sistema!")
                    break
        else:  
                    print("Opção invalida, tente novamente!")
                    escolha_do_usuario =int(input("digite uma opcão: "))
                    

def gerar_novo_id(lista_produtos):
    """Verifica a lista e retorna o próximo ID válido."""
    if not lista_produtos:
        # Se a lista está vazia, o primeiro ID é 1
        return 1
    
    # Pega o maior ID que existe na lista e soma 1
    maior_id = max(produto['id'] for produto in lista_produtos)
    return maior_id + 1





def cadastrar_produto(estoque_da_loja): 

    id_atual = gerar_novo_id(estoque_da_loja)   
    
    print("=== Cadastrar produto ===")

    nome = input("Digite o nome do produto: ").strip().upper()
    
    while not nome:
        print("Nome não pode estar vazio!")
        nome = input("Digite o nome do produto: ").strip().upper()
    
    # --- VERIFICAÇÃO DE DUPLICIDADE ---
    produto_ja_existe = False
    for produto in estoque_da_loja:
        # Compara os nomes ignorando maiúsculas/minúsculas
        if produto['nome'].lower() == nome.lower(): 
            produto_ja_existe = True
            print(f"\nErro: O produto '{nome}' já está cadastrado (ID: {produto['id']}).")
            print("Use a Opção 3 (Editar) se quiser adicionar estoue ou alterar o preço.")
            break
    
    if produto_ja_existe:
        return
    # --- FIM DA VERIFICAÇÃO ---

    # Se o 'if' acima não foi ativado, o produto é novo e o código continua:

    while True:
        try:
            quantidade = int(input("Digite a quantidade de produtos: "))
            break
        except ValueError:
            print("Quantidade inválida! Deve ser um número inteiro.")

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço inválido! Use ponto para decimais (ex: 10.50).")

    novo_produto = {
        "id": id_atual,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    estoque_da_loja.append(novo_produto)
    salvar_estoque_csv(estoque_da_loja)
    registrar_log("Cadastro de novo produto", nome)

    print(f"Produto '{nome}' cadastrado com sucesso!")
                                                   
    
    


def listar_produtos(estoque_da_loja):
    print("--- Lista de Produtos ---")

    if not estoque_da_loja:
        print("Nenhum produto cadastrado ainda.")
        return

    for produto in estoque_da_loja:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | "
              f"Qtd: {produto['quantidade']} | Preço: R$ {produto['preco']:.2f}")


def editar_produto(estoque_da_loja):
    print("=== Editar produto ===")

    if not estoque_da_loja:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos(estoque_da_loja)

    try:
        id_editar = int(input("Digite o ID do produto que deseja editar: "))
    except ValueError:
        print("ID inválido!")
        return

    produto = next((item for item in estoque_da_loja if item["id"] == id_editar), None)

    if produto is None:
        print("Produto não encontrado!")
        return

    print(f"Produto selecionado: {produto['nome']}")
    print("Deixe o campo vazio para manter o valor atual.")

    novo_nome = input("Novo nome do produto: ").strip()
    if novo_nome:
        produto["nome"] = novo_nome

    nova_quantidade = input("Nova quantidade do produto: ").strip()
    if nova_quantidade:
        try:
            produto["quantidade"] = int(nova_quantidade)
        except ValueError:
            print("Quantidade inválida! Valor não alterado.")

    novo_preco = input("Novo preço do produto: ").strip()
    if novo_preco:
        try:
            produto["preco"] = float(novo_preco)
        except ValueError:
            print("Preço inválido! Valor não alterado.")

    salvar_estoque_csv(estoque_da_loja)
    registrar_log("Edição do produto", produto["nome"])
    print("Produto atualizado com sucesso!")


def excluir_produto(estoque_da_loja):
    print("=== Excluir produto ===")

    if not estoque_da_loja:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos(estoque_da_loja)

    try:
        id_excluir = int(input("Digite o ID do produto que deseja excluir: "))
    except ValueError:
        print("ID inválido! Deve ser um número inteiro.")
        return

    produto = next((item for item in estoque_da_loja if item["id"] == id_excluir), None)
    if produto is None:
        print("Produto não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir '{produto['nome']}'? (S/N): ").strip().lower()
    if confirmacao != "s":
        print("Exclusão cancelada.")
        return

    estoque_da_loja.remove(produto)
    salvar_estoque_csv(estoque_da_loja)
    registrar_log("Exclusão do produto", produto["nome"])
    print(f"Produto '{produto['nome']}' excluído com sucesso!")
    
    
def limpar_lista(lista_produtos):
    """
    Exclui TODOS os produtos da lista e do arquivo, após confirmação.
    """
    global salvar_estoque_csv, registrar_log, nome_produto
    print("--- Excluir Todos os Produtos ---")
    
    if not lista_produtos:
        print("A lista de produtos já está vazia.")
        return lista_produtos

    # Confirmação de segurança
    print(f"ATENÇÃO: Esta ação é IRREVERSÍVEL.")
    print(f"Você está prestes a apagar todos os {len(lista_produtos)} produtos do sistema.")
    
    confirmacao = input(f"Digite 's' para confirmar: ").upper().strip()

    # Verificação rigorosa para evitar acidentes
    if confirmacao == 'S':
        lista_produtos.clear()      # Limpa a lista em memória
        salvar_estoque_csv(lista_produtos)  # Salva a lista vazia no arquivo JSON
        
        print(f"Todos os produtos foram excluídos com sucesso.")
    else:
        print("Ação cancelada. Nenhum produto foi excluído.")

    return lista_produtos
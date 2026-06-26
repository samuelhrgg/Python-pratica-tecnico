# ==============================
# Sistema de Cadastro de Livros
# ==============================

livros = []

while True:

    print("\n" + "=" * 40)
    print("     SISTEMA DE CADASTRO")
    print("=" * 40)
    print("[1] Cadastrar livro")
    print("[2] Listar livros")
    print("[3] Alterar livro")
    print("[4] Excluir livro")
    print("[5] Sair")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    # CADASTRAR
    if opcao == "1":

        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()

        if titulo == "" or autor == "":
            print("\nDados inválidos!")
        else:
            livros.append([titulo, autor])
            print("\nLivro cadastrado com sucesso!")

    # LISTAR
    elif opcao == "2":

        if len(livros) == 0:
            print("\nNenhum livro cadastrado.")

        else:
            print("\nLISTA DE LIVROS")
            print("-" * 40)

            for i in range(len(livros)):
                print(f"{i+1}. {livros[i][0]} - {livros[i][1]}")

    # ALTERAR
    elif opcao == "3":

        if len(livros) == 0:
            print("\nNenhum livro cadastrado.")

        else:

            print("\nLivros cadastrados:")

            for i in range(len(livros)):
                print(f"{i+1}. {livros[i][0]}")

            try:
                indice = int(input("\nQual livro deseja alterar? ")) - 1

                if indice >= 0 and indice < len(livros):

                    novo_titulo = input("Novo título: ").strip()
                    novo_autor = input("Novo autor: ").strip()

                    livros[indice][0] = novo_titulo
                    livros[indice][1] = novo_autor

                    print("\nLivro alterado com sucesso!")

                else:
                    print("\nLivro inexistente!")

            except:
                print("\nDigite apenas números!")

    # EXCLUIR
    elif opcao == "4":

        if len(livros) == 0:
            print("\nNenhum livro cadastrado.")

        else:

            print("\nLivros cadastrados:")

            for i in range(len(livros)):
                print(f"{i+1}. {livros[i][0]}")

            try:
                indice = int(input("\nQual livro deseja excluir? ")) - 1

                if indice >= 0 and indice < len(livros):

                    del livros[indice]
                    #livros.pop(indice)

                    print("\nLivro excluído com sucesso!")

                else:
                    print("\nLivro inexistente!")

            except:
                print("\nDigite apenas números!")

    # SAIR
    elif opcao == "5":

        print("\nPrograma encerrado!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("\nOpção inválida!")


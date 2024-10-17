from Ouvidoria import (
    listar, listarPorTipo, adicionar, quantidadeManifestacoes,
    buscarPorCodigo, excluirPorCodigo
)

def menu():
    print("\nOuvidoria")
    print("1 - Listagem de Manifestações")
    print("2 - Listagem de Manifestações por tipo")
    print("3 - Criar uma Manifestação")
    print("4 - Exibir quantidade de Manifestações")
    print("5 - Pesquisar uma Manifestação por código")
    print("6 - Excluir uma Manifestação pelo Código")
    print("7 - Sair do Sistema")


def obterTipoManifestacao():
    tipoManifestacao = input("\nDigite o tipo da manifestação:\n"
                             "1 - reclamacoes \n"
                             "2 - elogios\n"
                             "3 - sugestoes\n")

    while tipoManifestacao not in ["1", "2", "3"]:
        print("\nDigite uma opção válida!\n")
        tipoManifestacao = input("Digite o tipo da manifestação:\n"
                                 "1 - reclamacoes \n"
                                 "2 - elogios\n"
                                 "3 - sugestoes\n")

    return tipoManifestacao


def obterCodigo(mensagem):
    codigo = input(mensagem)
    while codigo == "":
        print("O código não pode estar vazio!")
        codigo = input(mensagem)
    return codigo


def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                print(listar())
            case "2":
                tipoManifestacao = obterTipoManifestacao()
                print(listarPorTipo(tipoManifestacao))
            case "3":
                tipoManifestacao = obterTipoManifestacao()

                mensagem = input("Digite a mensagem: ")

                while mensagem == "":
                    print("\nDigite uma mensagem nos campos a baixo!\n")

                    mensagem = input("Digite a mensagem: ")

                adicionar(tipoManifestacao, mensagem)
                print("\nManifestação adicionada com sucesso!")
            case "4":
                print(quantidadeManifestacoes())
            case "5":
                buscarCodigo = obterCodigo("Digite o codigo da manifestação que voce deseja buscar: ")

                print(buscarPorCodigo(buscarCodigo))
            case "6":
                excluirCodigo = obterCodigo("Digite o codigo da manifestação que voce deseja excluir: ")

                print(excluirPorCodigo(excluirCodigo))
            case "7":
                print("Programa fechado")
                break
            case _: print("Selecione uma opção valida")


if __name__ == "__main__":
    main()
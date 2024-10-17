from operacoesbd import *

conexao = criarConexao('localhost', 'root', 'root', 'ouvidoria_python')

def listar():
    sql = "SELECT * FROM manifestacoes"
    manifestacoes = listarBancoDados(conexao, sql)

    if len(manifestacoes) == 0:
        return "\nNão existem manifestações"
    else:
        manifestacoesStr = []
        for manifestacao in manifestacoes:
            manifestacaoFormatada = (
                f"\nId = {manifestacao['id']}; "
                f"Tipo = {manifestacao['tipo']}; "
                f"Mensagem = {manifestacao['mensagem']}"
            )
            manifestacoesStr.append(manifestacaoFormatada)

        return "\n".join(manifestacoesStr)


def listarPorTipo(tipoManifestacaoNum):
    tipoManifestacao = modificarTipos(tipoManifestacaoNum)

    sql = "SELECT * FROM manifestacoes WHERE tipo = %s"
    manifestacoes = listarBancoDados(conexao, sql, tipoManifestacao)

    if len(manifestacoes) == 0:
        return "\nNão existem manifestações"
    else:
        manifestacoesStr = []
        for manifestacao in manifestacoes:
            manifestacaoFormatada = (
                f"\nId = {manifestacao['id']}; "
                f"Tipo = {manifestacao['tipo']}; "
                f"Mensagem = {manifestacao['mensagem']}"
            )
            manifestacoesStr.append(manifestacaoFormatada)

        return "\n".join(manifestacoesStr)


def modificarTipos(tipoManifestacao):
    if tipoManifestacao == '1':
        return "reclamação"

    elif tipoManifestacao == '2':
        return "elogio"

    else:
        return "sugestão"


def adicionar(tipoManifestacao, manifestacao):
    sql = "INSERT INTO manifestacoes (tipo, mensagem) VALUES (%s, %s)"
    dados = (tipoManifestacao, manifestacao)
    insertNoBancoDados(conexao,sql,dados)


def quantidadeManifestacoes():
    sql = "SELECT COUNT(*) FROM manifestacoes"
    resultado = listarBancoDados(conexao,sql)

    if resultado and len(resultado) > 0:
        return f"\nO numero total de manifestações é de: {resultado[0]['COUNT(*)']}"
    else:
        return "\nNenhuma manifestação encontrada"


def buscarPorCodigo(codigo):
    sql = "SELECT * FROM manifestacoes WHERE id = %s"
    manifestacaoBusca = listarBancoDados(conexao,sql,codigo)

    if len(manifestacaoBusca) == 0:
        return f"\nManifestação de id '{codigo}' não encontrada"
    else:
        manifestacaoStr = []
        for manifestacao in manifestacaoBusca:
            manifestacaoFormatada = (
                f"\nId = {manifestacao['id']}; "
                f"Tipo = {manifestacao['tipo']}; "
                f"Mensagem = {manifestacao['mensagem']}"
            )
            manifestacaoStr.append(manifestacaoFormatada)

        return "\n".join(manifestacaoStr)


def excluirPorCodigo(codigo):
    sql = "DELETE FROM manifestacoes WHERE id = %s"
    linhasAfetadas = excluirBancoDados(conexao,sql,codigo)

    if linhasAfetadas == 0:
        return f"\nManifestação com ID '{codigo}' não encontrada"
    else:
        return f"\nManifestação com ID '{codigo}' removida com sucesso"
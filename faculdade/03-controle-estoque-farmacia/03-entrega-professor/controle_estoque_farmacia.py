# Sistema de Controle de Estoque de Farmacia


def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada invalida! Este campo nao pode ficar em branco.")


def ler_inteiro_minimo(mensagem, minimo):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor >= minimo:
                return valor
            print(f"Valor invalido! Digite um numero inteiro >= {minimo}.")
        except ValueError:
            print("Entrada invalida! Digite apenas um numero inteiro.")


def ler_preco_positivo(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            preco = float(entrada)
            if preco > 0.0:
                return preco
            print("Valor invalido! O preco deve ser maior que zero.")
        except ValueError:
            print("Entrada invalida! Digite um valor numerico (ex: 12.50 ou 12,50).")


def buscar_medicamento(estoque, codigo_busca):
    for item in estoque:
        if item["codigo"] == codigo_busca:
            return item
    return None


def cadastrar_medicamento(estoque):
    print("\n--- Cadastrar Novo Medicamento ---")
    codigo = ler_texto_obrigatorio("Codigo do medicamento: ").upper()
    if buscar_medicamento(estoque, codigo) is not None:
        print(f"Erro: Ja existe um medicamento cadastrado com o codigo '{codigo}'.")
        return

    nome = ler_texto_obrigatorio("Nome do medicamento: ")
    quantidade = ler_inteiro_minimo("Quantidade inicial em estoque [>= 0]: ", 0)
    estoque_minimo = ler_inteiro_minimo("Estoque minimo de seguranca [>= 1]: ", 1)
    preco_unitario = ler_preco_positivo("Preco unitario (R$) [> 0]: ")

    estoque.append(
        {
            "codigo": codigo,
            "nome": nome,
            "quantidade": quantidade,
            "estoque_minimo": estoque_minimo,
            "preco_unitario": preco_unitario,
        }
    )
    print(f"Medicamento '{nome}' ({codigo}) cadastrado com sucesso!")


def registrar_saida(estoque):
    print("\n--- Registrar Saida de Medicamento ---")
    if not estoque:
        print("Nenhum medicamento cadastrado no estoque.")
        return

    codigo = ler_texto_obrigatorio("Codigo do medicamento: ").upper()
    item = buscar_medicamento(estoque, codigo)
    if item is None:
        print(f"Erro: Medicamento com codigo '{codigo}' nao encontrado.")
        return

    qtd_saida = ler_inteiro_minimo("Quantidade a retirar [>= 1]: ", 1)
    if qtd_saida > item["quantidade"]:
        print(
            f"Operacao bloqueada! Estoque insuficiente "
            f"(Disponivel: {item['quantidade']} unidades)."
        )
        return

    item["quantidade"] -= qtd_saida
    print(
        f"Saida registrada! Novo saldo de '{item['nome']}': "
        f"{item['quantidade']} unidades."
    )


def exibir_relatorio(estoque):
    print("\n--- Relatorio Geral de Estoque ---")
    if not estoque:
        print("Estoque vazio.")
        return

    valor_total_estoque = 0.0
    total_em_alerta = 0

    for item in estoque:
        subtotal = item["quantidade"] * item["preco_unitario"]
        valor_total_estoque += subtotal
        alerta = ""
        if item["quantidade"] < item["estoque_minimo"]:
            alerta = " [ALERTA: REPOR ESTOQUE]"
            total_em_alerta += 1

        print(
            f"[{item['codigo']}] {item['nome']} | "
            f"Qtd: {item['quantidade']} (Min: {item['estoque_minimo']}) | "
            f"Unit: R$ {item['preco_unitario']:.2f} | "
            f"Subtotal: R$ {subtotal:.2f}{alerta}"
        )

    print("--------------------------------------------------")
    print(f"Total de Itens Cadastrados   : {len(estoque)}")
    print(f"Itens Abaixo do Estoque Min. : {total_em_alerta}")
    print(f"Valor Financeiro em Estoque  : R$ {valor_total_estoque:.2f}")


def main():
    estoque = []
    while True:
        print("\n=== CONTROLE DE ESTOQUE DE FARMACIA ===")
        print("1 - Cadastrar Medicamento")
        print("2 - Registrar Saida (Venda)")
        print("3 - Exibir Relatorio e Alertas")
        print("4 - Sair")

        opcao = input("Escolha uma opcao [1 a 4]: ").strip()
        if opcao == "1":
            cadastrar_medicamento(estoque)
        elif opcao == "2":
            registrar_saida(estoque)
        elif opcao == "3":
            exibir_relatorio(estoque)
        elif opcao == "4":
            print("Encerrando o sistema de estoque. Ate logo!")
            break
        else:
            print("Opcao invalida! Digite um numero de 1 a 4.")


if __name__ == "__main__":
    main()

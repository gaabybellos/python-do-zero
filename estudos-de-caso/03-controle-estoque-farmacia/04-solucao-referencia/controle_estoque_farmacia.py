# Estudo de Caso 03 (PYZ-CASE-003) - Sistema de Controle de Estoque de Farmacia
# Estudo de caso ficticio e autoral criado exclusivamente para aprendizado.


def ler_texto_obrigatorio(mensagem: str) -> str:
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada invalida! Este campo nao pode ficar em branco.")


def ler_inteiro_minimo(mensagem: str, minimo: int) -> int:
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor >= minimo:
                return valor
            print(f"Valor invalido! Digite um numero inteiro >= {minimo}.")
        except ValueError:
            print("Entrada invalida! Digite apenas um numero inteiro.")


def ler_preco_positivo(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            preco = float(entrada)
            if preco > 0.0:
                return preco
            print("Valor invalido! O preco deve ser maior que zero.")
        except ValueError:
            print("Entrada invalida! Digite um valor numerico (ex: 12.50 ou 12,50).")


def buscar_medicamento(estoque: list[dict], codigo_busca: str) -> dict | None:
    codigo_padronizado = codigo_busca.strip().upper()
    for item in estoque:
        if item["codigo"] == codigo_padronizado:
            return item
    return None


def adicionar_medicamento_estoque(
    estoque: list[dict],
    codigo: str,
    nome: str,
    quantidade: int,
    estoque_minimo: int,
    preco_unitario: float,
) -> bool:
    codigo_limpo = codigo.strip().upper()
    if buscar_medicamento(estoque, codigo_limpo) is not None:
        return False
    estoque.append(
        {
            "codigo": codigo_limpo,
            "nome": nome.strip(),
            "quantidade": quantidade,
            "estoque_minimo": estoque_minimo,
            "preco_unitario": round(preco_unitario, 2),
        }
    )
    return True


def baixar_estoque(
    estoque: list[dict], codigo: str, qtd_saida: int
) -> tuple[bool, str]:
    if qtd_saida <= 0:
        return False, "A quantidade de saida deve ser maior que zero."
    item = buscar_medicamento(estoque, codigo)
    if item is None:
        return False, f"Erro: Medicamento com codigo '{codigo}' nao encontrado."
    if qtd_saida > item["quantidade"]:
        return (
            False,
            f"Operacao bloqueada! Estoque insuficiente "
            f"(Disponivel: {item['quantidade']} unidades).",
        )
    item["quantidade"] -= qtd_saida
    return (
        True,
        f"Saida registrada! Novo saldo de '{item['nome']}': "
        f"{item['quantidade']} unidades.",
    )


def cadastrar_medicamento(estoque: list[dict]) -> None:
    print("\n--- Cadastrar Novo Medicamento ---")
    codigo = ler_texto_obrigatorio("Codigo do medicamento: ").upper()
    if buscar_medicamento(estoque, codigo) is not None:
        print(f"Erro: Ja existe um medicamento cadastrado com o codigo '{codigo}'.")
        return

    nome = ler_texto_obrigatorio("Nome do medicamento: ")
    quantidade = ler_inteiro_minimo("Quantidade inicial em estoque [>= 0]: ", 0)
    estoque_minimo = ler_inteiro_minimo("Estoque minimo de seguranca [>= 1]: ", 1)
    preco_unitario = ler_preco_positivo("Preco unitario (R$) [> 0]: ")

    adicionar_medicamento_estoque(
        estoque, codigo, nome, quantidade, estoque_minimo, preco_unitario
    )
    print(f"Medicamento '{nome}' ({codigo}) cadastrado com sucesso!")


def registrar_saida(estoque: list[dict]) -> None:
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
    _, mensagem = baixar_estoque(estoque, codigo, qtd_saida)
    print(mensagem)


def exibir_relatorio(estoque: list[dict]) -> None:
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


def main() -> None:
    estoque: list[dict] = []
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

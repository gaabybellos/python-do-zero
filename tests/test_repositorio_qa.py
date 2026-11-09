from pathlib import Path
from resetar_progresso import resetar_arquivos_progresso

RAIZ = Path(__file__).resolve().parent.parent
LIMITE_COLUNAS_PEP8 = 88


def test_todos_arquivos_python_compilam_e_respeitam_88_colunas():
    arquivos_py = [
        p
        for p in RAIZ.rglob("*.py")
        if ".venv" not in p.parts and "venv" not in p.parts
    ]
    assert len(arquivos_py) > 0

    violacoes = []
    for arquivo in arquivos_py:
        conteudo = arquivo.read_text(encoding="utf-8")
        compile(conteudo, str(arquivo), "exec")
        for num_linha, linha in enumerate(conteudo.splitlines(), start=1):
            if len(linha) > LIMITE_COLUNAS_PEP8:
                rel = arquivo.relative_to(RAIZ)
                violacoes.append(f"{rel}:{num_linha} ({len(linha)} cols)")

    assert not violacoes, "Linhas acima de 88 caracteres:\n" + "\n".join(violacoes)


def test_resetar_progresso_cria_arquivo_local(tmp_path):
    docs_dir = tmp_path / "Docs" / "templates"
    docs_dir.mkdir(parents=True)
    template = docs_dir / "progresso-inicial.md"
    template.write_text("# Progresso Teste\n", encoding="utf-8")

    arq_padrao, arq_local = resetar_arquivos_progresso(tmp_path)
    assert arq_padrao.exists()
    assert arq_local.exists()
    assert arq_local.read_text(encoding="utf-8") == "# Progresso Teste\n"

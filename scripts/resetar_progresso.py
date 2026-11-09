"""
Script utilitário para inicializar ou resetar o painel de progresso a partir do
template oficial (`Docs/templates/progresso-inicial.md`).

Gera/atualiza:
- `Docs/progresso-aluno.md` (template base rastreado)
- `Docs/progresso-local.md` (progresso individual ignorado pelo Git)
"""

from pathlib import Path


def resetar_arquivos_progresso(diretorio_raiz: Path | None = None) -> tuple[Path, Path]:
    raiz = diretorio_raiz or Path(__file__).resolve().parent.parent
    template = raiz / "Docs" / "templates" / "progresso-inicial.md"
    progresso_aluno = raiz / "Docs" / "progresso-aluno.md"
    progresso_local = raiz / "Docs" / "progresso-local.md"

    conteudo = template.read_text(encoding="utf-8")
    progresso_aluno.write_text(conteudo, encoding="utf-8")
    progresso_local.write_text(conteudo, encoding="utf-8")
    return progresso_aluno, progresso_local


def main() -> None:
    arq_padrao, arq_local = resetar_arquivos_progresso()
    print(f"Progresso padrao restaurado em: {arq_padrao}")
    print(f"Progresso pessoal local criado em: {arq_local}")


if __name__ == "__main__":
    main()

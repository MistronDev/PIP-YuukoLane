# cli.py
import argparse
import subprocess
from pathlib import Path
from .yuukolane_transpiler import converter
from .validador import validar_codigo

def main():
    parser = argparse.ArgumentParser(
        description="Transpila e executa código YuukoLane (.yl)"
    )
    parser.add_argument("arquivo", help="Caminho do arquivo .yl")
    parser.add_argument("--so-transpilar", action="store_true", help="Só transpilar, não executar")
    parser.add_argument("--debug", action="store_true", help="Mostrar código transpilado antes de executar")

    args = parser.parse_args()
    caminho = Path(args.arquivo)
    if not caminho.exists() or not caminho.suffix == ".yl":
        print(f"[ERRO] Arquivo inválido: {caminho}")
        return

    try:
        codigo_yl = caminho.read_text(encoding="utf-8")
        codigo_py = converter(codigo_yl)

        if args.debug:
            print("📜 Código transpilado:\n")
            print(codigo_py)
            print("\n🔚 Fim da transpilação\n")

        # Salva o .py correspondente
        saida = caminho.with_suffix(".py")
        saida.write_text(codigo_py, encoding="utf-8")
        print(f"[OK] Transpilação concluída: {saida}")

        # Executa o código, se permitido
        if not args.so_transpilar:
            print(f"\n🚀 Executando {saida}:\n")
            subprocess.run(["python", str(saida)])

    except Exception as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()

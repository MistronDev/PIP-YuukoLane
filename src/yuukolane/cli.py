import argparse
import subprocess
from yuukolane import validador, yuukolane_transpiler

def main():
    parser = argparse.ArgumentParser(
        description="Transpila e executa código YuukoLane (.yl)"
    )
    parser.add_argument("arquivo", help="Caminho do arquivo .yl")
    parser.add_argument("--so-transpilar", action="store_true", help="Só transpilar, não executar")
    parser.add_argument("--debug", action="store_true", help="Mostrar código transpilado antes de executar")

    args = parser.parse_args()
    caminho = args.arquivo
    saida = caminho.replace(".yl", ".py")

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            codigo = f.read()

        validador.validar(codigo)
        codigo_python = yuukolane_transpiler.transpilar(codigo)

        if args.debug:
            print("📜 Código transpilado:\n")
            print(codigo_python)
            print("\n🔚 Fim da transpilação\n")

        with open(saida, "w", encoding="utf-8") as f:
            f.write(codigo_python)

        print(f"✅ Arquivo transpilado salvo em: {saida}")

        if not args.so_transpilar:
            print(f"🚀 Executando {saida}...\n")
            subprocess.run(["python", saida])
    except Exception as e:
        print(f"❌ Erro: {e}")

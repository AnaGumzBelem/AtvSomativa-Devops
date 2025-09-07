import argparse
from .core import bmi, category


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora de IMC")
    parser.add_argument(
        "--peso",
        type=float,
        required=True,
        help="Peso em kg (ex: 70)",
    )
    parser.add_argument(
        "--altura",
        type=float,
        required=True,
        help="Altura em metros (ex: 1.75)",
    )
    args = parser.parse_args()

    valor = bmi(args.peso, args.altura)
    print(
        f"IMC: {valor:.2f} | Categoria: {category(valor)}"
    )


def run_cli() -> None:
    """Wrapper para ser chamado externamente (ex.: main.py)."""
    main()


if __name__ == "__main__":
    main()

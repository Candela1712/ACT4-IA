import argparse
import sys
import ollama


def main():
    parser = argparse.ArgumentParser(
        description="Genera text amb Gemma3:4b utilitzant Ollama."
    )

    parser.add_argument("prompt", type=str, help="El prompt.")
    parser.add_argument("--vegades", type=int, default=5)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=None)

    # Comprovar si no hi ha arguments
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    options = {
        "temperature": args.temperature
    }

    if args.seed is not None:
        options["seed"] = args.seed

    print(f"Prompt: {args.prompt}")
    print(f"vegades: {args.vegades}")
    print(f"temperature: {args.temperature}")
    if args.seed is not None:
        print(f"seed: {args.seed}")
    print()

    for i in range(1, args.vegades + 1):
        response = ollama.generate(
            model="gemma3:4b",
            prompt=args.prompt,
            options=options
        )

        text = response["response"].strip()
        print(f"{i}. {text}")


if __name__ == "__main__":
    main()
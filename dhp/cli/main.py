import argparse
from dhp.commerce.products import Products

def main():
    parser = argparse.ArgumentParser(prog="dhp")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("version")
    sub.add_parser("health")

    products = sub.add_parser("products")
    products.add_argument("action", choices=["list", "get"])
    products.add_argument("value", nargs="?")

    args = parser.parse_args()

    if args.command == "version":
        print("DHP AI Platform v0.1.0")

    elif args.command == "health":
        print("DHP STATUS: OK")

    elif args.command == "products":
        p = Products()

        if args.action == "list":
            p.list()

        elif args.action == "get":
            p.get(args.value)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

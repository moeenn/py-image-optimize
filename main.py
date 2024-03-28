from app.app import Application
import sys


def main() -> None:
    app = Application()
    app.run(sys.argv[1:])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("ctrl+c: shutting down...")
    except Exception as err:
        print("error: ", err)

import time


def main():
    try:
        while True:
            print("Test")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa Detenido")


if __name__ == "__main__":
    main()

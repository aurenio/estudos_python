def leiaint(m="vazio"):
    while True:
        try:
            numb = int(input(f"{m}\n"))
        except ValueError:
            print("\033[34mDigite um valor válido\033[m")
        except KeyboardInterrupt:
            print("O usuario decidiu cancelar, valor é 0")
            return 0
        except Exception as erro:
            print(f"{erro.__class__, erro.__cause__}")
        else:
            print(f"O valor que você digitou foi {numb}")
            return numb


def leiafloat(m="vazio"):
    while True:
        try:
            numb = float(input(f"{m}\n"))
        except ValueError:
            print("\033[34mDigite um valor válido\033[m")
        except KeyboardInterrupt:
            print("O usuario decidiu cancelar, valor é 0")
            return 0
        except Exception as erro:
            print(f"{erro.__class__, erro.__cause__}")
        else:
            print(f"O valor que você digitou foi {numb}")
            return numb


leiaint()
leiafloat()

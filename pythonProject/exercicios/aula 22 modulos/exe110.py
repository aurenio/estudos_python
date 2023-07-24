import exe109
def resumo(n=0, aume=1, dim=1, fo=False):
    print("=-"*20)
    print(f"{'RESUMO':^40}")
    print("--" * 20)
    print("numero", end="")
    print(f" {exe109.moeda(n, fo):>3}")
    print(f"metade {exe109.metade(n, fo):^15}")
    print(f"dobro {exe109.dobro(n, fo):^15}")
    print(f"dimin {exe109.diminuir(dim, n, fo):^15}")
    print(f"aument {exe109.aumentar(aume, n, fo):^15}")
    print("=-" * 20)
    print()

def oi():
    print("oinn")
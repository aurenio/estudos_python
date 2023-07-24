fut=("Palmeiras", "Internacional", "Fluminense", "Corinthians", 'Flamengo', "Athletico-PR", "Atlético-MG"
     , "América-MG", "Fortaleza", "Botafogo", "Santos", "Goiás", "São Paulo", "Bragantino", "Coritiba",
     "Ceará", "Cuiabá", "Avaí", "Atlético-GO", "Juventude")
print(f"Os primeiros 5 times são\n {fut[0:5]}")
print(f"Os últimos 6 colocados são\n {fut[-4:]}")
print(f"Os times em ordem afabetica fica:\n {sorted(fut)}")
print(f" O nome santos fica nessa posição:\n {fut.index('Santos') + 1}")

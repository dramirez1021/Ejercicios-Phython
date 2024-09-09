#proposito: tp
# autor: DRM
# Fecha: 22/12/2020
for a in range (1,501):
    for b in range (1,501):
        for c in range (1,501):
            if (a**2) + (b**2) == (c**2):
                print(f"{a},{b},{c}")

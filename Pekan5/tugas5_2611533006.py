print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3006 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
print("#", end="")

for i_3006 in range(4 * n_3006 + 5):
    print("=", end="")

print("#")

# Fase 1: Jam pasir atas
for baris_3006 in range(n_3006, 0, -1):
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3006 in range(2 * (n_3006 - baris_3006)):
        print(" ", end="")

    # Angka menurun
    for angka_3006 in range(baris_3006, 0, -1):
        print(angka_3006, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_3006 in range(1, baris_3006 + 1):
        print(" ", end="")
        print(angka_3006, end="")

    # Spasi penyeimbang kanan
    for spasi_3006 in range(2 * (n_3006 - baris_3006)):
        print(" ", end="")

    print(" |")

# Fase 2: Poros pusat
print("|", end="")

for spasi_3006 in range(2 * n_3006 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_3006 in range(2 * n_3006 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah
for baris_3006 in range(1, n_3006 + 1):
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3006 in range(2 * (n_3006 - baris_3006)):
        print(" ", end="")

    # Angka menurun
    for angka_3006 in range(baris_3006, 0, -1):
        print(angka_3006, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_3006 in range(1, baris_3006 + 1):
        print(" ", end="")
        print(angka_3006, end="")

    # Spasi penyeimbang kanan
    for spasi_3006 in range(2 * (n_3006 - baris_3006)):
        print(" ", end="")

    print(" |")

# Border bawah
print("#", end="")

for i_3006 in range(4 * n_3006 + 5):
    print("=", end="")

print("#")
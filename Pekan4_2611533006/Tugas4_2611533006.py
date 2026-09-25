print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_3006 = input("Masukkan Nama Pengunjung        : ")
umur_3006 = int(input("Input umur anda                 : "))

sim_input_3006 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_3006 = sim_input_3006[0] if sim_input_3006 else 't'

# 2. Pemilihan Wahana Menggunakan match-case
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

pilihan_3006 = int(input("Masukkan nomor paket (1-5)      : "))

# Variabel awal paket wahana
nama_paket_3006 = ""
harga_satuan_3006 = 0

match pilihan_3006:
    case 1:
        nama_paket_3006 = "Wahana Safari Rimba"
        harga_satuan_3006 = 50000
    case 2:
        nama_paket_3006 = "Wahana Arung Jeram"
        harga_satuan_3006 = 75000
    case 3:
        nama_paket_3006 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3006 = 120000
    case 4:
        nama_paket_3006 = "Wahana Roller Coaster Kilat"
        harga_satuan_3006 = 100000
    case 5:
        nama_paket_3006 = "Wahana All-Access VIP"
        harga_satuan_3006 = 220000
    case _:
        print("\nPaket wahana tidak valid!")
        exit()

jumlah_tiket_3006 = int(input("Masukkan jumlah tiket           : "))

# Penerapan IF tunggal untuk validasi kuota/jumlah tiket
if jumlah_tiket_3006 <= 0:
    print("Peringatan: Jumlah tiket tidak valid! Transaksi dibatalkan.")
    exit()

is_member_3006 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3006 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else dan Operator Logika
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if pilihan_3006 == 3:
    if umur_3006 >= 17 and sim_3006 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_3006 >= 17 and sim_3006 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_3006 < 17 and sim_3006 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_3006 >= 10:
        print(f"Status Akses: Pengunjung memenuhi syarat usia untuk {nama_paket_3006}.")
    else:
        print(f"Status Akses: Pengunjung di bawah umur minimum (10 tahun) untuk {nama_paket_3006}.")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_3006 = harga_satuan_3006 * jumlah_tiket_3006
total_diskon_persen_3006 = 0

if subtotal_3006 >= 200000:
    total_diskon_persen_3006 += 10  # Diskon Belanja Besar

if is_member_3006 in ['y', 'ya']:
    total_diskon_persen_3006 += 5   # Diskon Member

if kode_promo_valid_3006 in ['y', 'ya']:
    total_diskon_persen_3006 += 15  # Diskon Voucher Promo

if jumlah_tiket_3006 >= 5:
    total_diskon_persen_3006 += 5   # Diskon Tambahan Rombongan

# 5. Evaluasi Kelulusan Audit & Rincian Pembayaran
nominal_diskon_3006 = subtotal_3006 * (total_diskon_persen_3006 / 100)
total_bayar_3006 = subtotal_3006 - nominal_diskon_3006

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3006:,.0f}".replace(",", "."))
print(f"Total Diskon     : {total_diskon_persen_3006}% (Rp {nominal_diskon_3006:,.0f})".replace(",", "."))
print(f"Total Bayar      : Rp {total_bayar_3006:,.0f}".replace(",", "."))

print("Catatan Layanan  : ", end="")
if total_bayar_3006 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Terima kasih telah berkunjung.")

print("Program Selesai")
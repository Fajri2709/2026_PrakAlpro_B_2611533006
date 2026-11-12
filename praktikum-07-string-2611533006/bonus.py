# Name: Fajri Ramadhan
# NIM: 2611533006
# Bonus

kalimat = input("Masukkan kalimat: ")
bersih = kalimat.replace(" ", "").lower()
if bersih == bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
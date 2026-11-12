# Name: Fajri Ramadhan
# NIM: 2611533006
# Question 3

# Soal A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Soal B
text = "Fajri Ramadhan"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)

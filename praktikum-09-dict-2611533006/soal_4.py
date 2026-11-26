kelas = input().split()
pengumpul = input().split()

set_kelas = set(kelas)
set_pengumpul = set(pengumpul)

submitted = set_kelas & set_pengumpul
not_submitted = set_kelas - set_pengumpul

print(f"Submitted: {len(submitted)} students")
print(f"Submitted: {len(not_submitted)} students")

for pengumpul in kelas:
    if pengumpul in not_submitted:
        print(pengumpul)
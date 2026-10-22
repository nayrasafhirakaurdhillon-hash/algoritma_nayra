#input
tugas = int(input("nilai tugas : "))
uts = int(input("nilai UTS : "))
uas = int(input("nilai UAS : "))
kehadiran = int(input("kehadiran : "))

#proses
nilai_akhir = (20/100 * tugas) + (30/100 * uts) + (50/100 * uas)

lulus = nilai_akhir >= 75 and kehadiran >= 80

predikat = (
    nilai_akhir >= 85
    and kehadiran >= 90
    and nilai_akhir % 2 == 0
)

# output
print(f"nilai akhir : {nilai_akhir}")

if predikat:
    print("status     : LULUS DENGAN PREDIKAT")
elif lulus:
    print("status      : LULUS")   
else:
    print("status      : BELUM LULUS")
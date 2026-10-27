from sistem_informasi.service import mahasiswa_service as svc

print(svc.tambah("001", "Budi", 3.5))
print(svc.tambah("002", "Ani", 3.9))
print(svc.tambah("001", "Dobel", 3.0))   # harus gagal: NIM sama
print(svc.semua())
print(svc.ubah("001", ipk=3.7))
print(svc.baca("001"))
print(svc.hapus("002"))
print(svc.semua())

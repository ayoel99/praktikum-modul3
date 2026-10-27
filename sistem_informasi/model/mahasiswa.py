# Penyimpanan in-memory: key = NIM, value = data mahasiswa
penyimpanan = {}


def buat_mahasiswa(nim, nama, ipk):
    return {"nim": nim, "nama": nama, "ipk": ipk}

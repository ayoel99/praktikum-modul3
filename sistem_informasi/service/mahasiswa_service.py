from sistem_informasi.model.mahasiswa import penyimpanan, buat_mahasiswa
from sistem_informasi.utils.validator import validasi_mahasiswa


def tambah(nim, nama, ipk):                      # CREATE
    valid, pesan = validasi_mahasiswa(nim, nama, ipk)
    if not valid:
        return False, pesan
    if nim in penyimpanan:
        return False, "NIM sudah terdaftar"
    penyimpanan[nim] = buat_mahasiswa(nim, nama, ipk)
    return True, "Berhasil ditambahkan"


def baca(nim):                                   # READ (satu)
    return penyimpanan.get(nim)


def semua():                                     # READ (semua)
    return list(penyimpanan.values())


def ubah(nim, nama=None, ipk=None):              # UPDATE
    mhs = penyimpanan.get(nim)
    if mhs is None:
        return False, "NIM tidak ditemukan"
    if nama is not None:
        mhs["nama"] = nama
    if ipk is not None:
        mhs["ipk"] = ipk
    return True, "Berhasil diubah"


def hapus(nim):                                  # DELETE
    if nim in penyimpanan:
        del penyimpanan[nim]
        return True, "Berhasil dihapus"
    return False, "NIM tidak ditemukan"

def validasi_mahasiswa(nim, nama, ipk):
    """Return (valid, pesan)."""
    if not nim or not nama:
        return False, "NIM dan nama wajib diisi"
    if not 0.0 <= ipk <= 4.0:
        return False, "IPK harus 0.0 - 4.0"
    return True, ""

def konversi_nilai_huruf(angka):
    """Mengubah nilai angka menjadi (huruf, bobot)."""
    if angka < 0 or angka > 100:
        raise ValueError("Nilai harus 0-100")
    if angka >= 85:
        return "A", 4.0
    if angka >= 70:
        return "B", 3.0
    if angka >= 55:
        return "C", 2.0
    if angka >= 40:
        return "D", 1.0
    return "E", 0.0


def hitung_ipk(daftar_mk):
    """daftar_mk: list of dict {"mk": str, "sks": int, "nilai": angka}."""
    total_sks = sum(mk["sks"] for mk in daftar_mk)
    if total_sks == 0:
        return 0.0
    total_bobot = sum(konversi_nilai_huruf(mk["nilai"])[1] * mk["sks"] for mk in daftar_mk)
    return total_bobot / total_sks


def generate_transkrip(nama, nim, daftar_mk):
    """Mengembalikan transkrip dalam bentuk string."""
    baris = [f"TRANSKRIP: {nama} ({nim})", "-" * 40]
    for mk in daftar_mk:
        huruf, _ = konversi_nilai_huruf(mk["nilai"])
        baris.append(f"{mk['mk']:<20} {mk['sks']} SKS  {mk['nilai']:>3}  {huruf}")
    baris.append("-" * 40)
    baris.append(f"IPK: {hitung_ipk(daftar_mk):.2f}")
    return "\n".join(baris)


if __name__ == "__main__":
    contoh = [
        {"mk": "Pemrograman Python", "sks": 3, "nilai": 88},
        {"mk": "Basis Data", "sks": 3, "nilai": 76},
    ]
    print(konversi_nilai_huruf(82))
    print(generate_transkrip("Tes", "123", contoh))
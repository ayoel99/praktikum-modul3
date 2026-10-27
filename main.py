import utilitas_akademik as ua

daftar = [
    {"mk": "Pemrograman Python", "sks": 3, "nilai": 90},
    {"mk": "Basis Data", "sks": 3, "nilai": 72},
    {"mk": "Sistem Informasi", "sks": 2, "nilai": 60},
]


def main():
    print(ua.generate_transkrip("Nama Kamu", "20241320019", daftar))


if __name__ == "__main__":
    main()
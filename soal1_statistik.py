import statistics
import math


def hitung_statistik(data):
    """Mengembalikan dictionary: mean, median, modus, range, std_dev."""
    if not data:
        raise ValueError("Data tidak boleh kosong")

    mean = sum(data) / len(data)
    median = statistics.median(data)
    modus = statistics.multimode(data)       # list, karena bisa lebih dari satu modus
    rentang = max(data) - min(data)
    std_dev = math.sqrt(statistics.pvariance(data))

    return {
        "mean": mean,
        "median": median,
        "modus": modus,
        "range": rentang,
        "std_dev": std_dev,
    }


if __name__ == "__main__":
    hasil = hitung_statistik([85, 90, 78, 92, 88, 90])
    for kunci, nilai in hasil.items():
        print(f"{kunci}: {nilai}")
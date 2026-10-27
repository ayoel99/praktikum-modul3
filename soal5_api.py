import json
import requests

URL = "https://jsonplaceholder.typicode.com/todos"


def ambil_data(url):
    respon = requests.get(url, timeout=10)
    respon.raise_for_status()          # error jika status bukan 2xx
    return respon.json()


def main():
    todos = ambil_data(URL)

    # filter: hanya yang selesai
    selesai = list(filter(lambda t: t["completed"], todos))

    # map: ambil sebagian field + judul jadi huruf kapital di awal kata
    ringkas = list(map(
        lambda t: {"id": t["id"], "userId": t["userId"], "title": t["title"].title()},
        selesai,
    ))

    # hitung todo selesai per user
    per_user = {}
    for t in selesai:
        per_user[t["userId"]] = per_user.get(t["userId"], 0) + 1

    # sorted: urutkan user dari yang paling banyak menyelesaikan
    ranking = sorted(per_user.items(), key=lambda x: x[1], reverse=True)
    ranking = list(map(lambda x: {"userId": x[0], "jumlah_selesai": x[1]}, ranking))

    hasil = {
        "total_todo": len(todos),
        "total_selesai": len(selesai),
        "ranking_user": ranking,
        "contoh_todo_selesai": ringkas[:5],
    }

    with open("hasil_analisis.json", "w", encoding="utf-8") as f:
        json.dump(hasil, f, indent=2, ensure_ascii=False)

    print("Selesai. Total selesai:", len(selesai))
    print("Top user:", ranking[0])


if __name__ == "__main__":
    main()

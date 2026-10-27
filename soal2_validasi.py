def validasi_data(data, schema, *wajib_tambahan, **opsi):
    """
    data   : dict yang divalidasi
    schema : dict aturan, contoh {"umur": {"tipe": int, "min": 17, "max": 60}}
    *wajib_tambahan : nama field tambahan yang wajib ada
    **opsi : strict=True -> field di luar schema dianggap error
    Return : (is_valid, errors)
    """
    errors = []

    for field in wajib_tambahan:
        if field not in data:
            errors.append(f"Field '{field}' wajib diisi")

    for field, aturan in schema.items():
        if field not in data:
            if aturan.get("wajib", False):
                errors.append(f"Field '{field}' wajib diisi")
            continue

        nilai = data[field]
        tipe = aturan.get("tipe")
        if tipe and not isinstance(nilai, tipe):
            errors.append(f"Field '{field}' harus bertipe {tipe.__name__}")
            continue

        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"Field '{field}' minimal {aturan['min']}")
        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"Field '{field}' maksimal {aturan['max']}")

    if opsi.get("strict", False):
        for field in data:
            if field not in schema:
                errors.append(f"Field '{field}' tidak dikenal")

    return (len(errors) == 0, errors)


if __name__ == "__main__":
    schema = {
        "nama": {"tipe": str, "wajib": True},
        "umur": {"tipe": int, "min": 17, "max": 60},
        "ipk": {"tipe": float, "min": 0.0, "max": 4.0},
    }

    print(validasi_data({"nama": "Budi", "umur": 20, "ipk": 3.5}, schema))
    print(validasi_data({"nama": "Ani", "umur": 10, "ipk": 5.0}, schema))
    print(validasi_data({"umur": 20}, schema, "nim", strict=True))
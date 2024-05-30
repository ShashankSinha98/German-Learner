def remove_umlaut_and_etset(inp: str) -> str:
    replace_with = {"ü": "u", "ö": "o", "ä": "a", "ß": "s"}

    for key, value in replace_with.items():
        if key in inp:
            inp = inp.replace(key, value)
    return inp

print(remove_umlaut_and_etset("hößrenüßää"))
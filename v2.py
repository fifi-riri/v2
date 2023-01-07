def stroka(str: str) -> str:
    if not str.endswith("!"):
        str = str + "!"
    return str.capitalize()

print(stroka("privet"))
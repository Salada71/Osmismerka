from pathlib import Path
from utils import (
    load_file_as_ascii,
    pozice_nul,
    pocet_nul,
    porovnej_posuvy,
    vrat_texty_radek_sloupec,
    obraceni_textu,
    vrat_texty_uhlopricne,
)

czech_path: Path = Path(__file__).resolve().parent / "czech.txt"
matice_path: Path = Path(__file__).resolve().parent / "matice.txt"

czech: list[str] = load_file_as_ascii(czech_path)
matice: list[str] = load_file_as_ascii(matice_path)

positions_of_zeros = pozice_nul(matice)
print("Pozice znaků '0':", positions_of_zeros)

count_zeros = pocet_nul(matice)
if count_zeros == 0:
    print("Nenalezena žádná 0")
    exit()
if count_zeros == 1:
    print("Nalezena jedna 0")
    texty = vrat_texty_radek_sloupec(matice, positions_of_zeros)
    texty_obracene = obraceni_textu(texty)
    combined_texts = texty_obracene + texty
    texty = vrat_texty_uhlopricne(matice, positions_of_zeros)
    texty_obracene = obraceni_textu(texty)
    combined_texts = combined_texts + texty_obracene + texty



    print("Spojené texty:", combined_texts)

    # zkus najít pro každé slovo v czech jeho pozici v poli combined_texts pomocí porovnej_posuvy
    try:
        combined_texts
    except NameError:
        combined_texts = []

    results = []
    found_words = 0
    for word in czech:
        for idx, text in enumerate(combined_texts):
            pos = porovnej_posuvy(word, text)
            if isinstance(pos, int) and pos >= 0:
                results.append((word, idx, pos))
                found_words += 1
                break
    print(f"Počet nalezených slov: {found_words}")

    print("Nalezené pozice (slovo, index_textu, posuv):", results)


input("Stiskněte Enter pro ukončení...")



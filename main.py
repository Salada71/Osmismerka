from pathlib import Path
from utils import load_file_as_ascii, pozice_nul, pocet_nul

czech_path: Path = Path(__file__).resolve().parent / "czech.txt"
matice_path: Path = Path(__file__).resolve().parent / "matice.txt"

czech: list[str] = load_file_as_ascii(czech_path)
matice: list[str] = load_file_as_ascii(matice_path)

positions_of_zeros = pozice_nul(matice)
print("Pozice znaků '0':", positions_of_zeros)

count_zeros = pocet_nul(matice)
if count_zeros == 0:
    print("Text nenalezen")

input("Stiskněte Enter pro ukončení...")



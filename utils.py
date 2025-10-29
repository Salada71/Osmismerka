from pathlib import Path

def load_file_as_ascii(path: Path = None) -> list[str]:
    """
    Načte soubor, rozdělí na řádky a odstraní všechny ne-ASCII znaky z každého řádku.
    Vrací seznam (pole) očištěných řádků.
    """
    
    if path is None:
        raise ValueError("Nebyla zadána cesta k souboru.")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    cleaned_lines = [''.join(ch for ch in line if ch.isascii()) for line in lines]
    return cleaned_lines

def pocet_nul(pole: list[str]) -> int:
    """
    Vrátí počet znaků '0' v zadaném poli řetězců.
    """
    return sum(s.count('0') for s in pole)

def pozice_nul(pole: list[str]) -> list[int]:
    """
    Vrátí seznam pozic znaků '0' v zadaném poli řetězců.
    """
    positions = []
    for i, line in enumerate(pole):
        for j, char in enumerate(line):
            if char == '0':
                positions.append((i, j))
    return positions

def porovnej_posuvy(kratky: str, dlouhy: str) -> int:
    """
    Prohledá všechny posuny kratky vůči dlouhy. Vrací první nalezený posun,
    kde 0 znamená, že oba začínají na stejné pozici, 1 znamená, že
    bylo nutno kratky posunout o jednu pozici doprava atd.
    V dlouhy je znak '0' považován za wildcard (matchuje jakýkoli znak).
    Pokud není nalezena žádná shoda, vrací -1.
    """
    if len(kratky) > len(dlouhy):
        raise ValueError("První řetězec nesmí být delší než druhý.")
    
    n = len(kratky)
    for start in range(len(dlouhy) - n + 1):
        for i, ch in enumerate(kratky):
            c2 = dlouhy[start + i]
            if c2 != '0' and c2 != ch:
                break
        else:
            return start
    return -1
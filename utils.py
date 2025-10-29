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
        return -1
    
    n = len(kratky)
    for start in range(len(dlouhy) - n + 1):
        for i, ch in enumerate(kratky):
            c2 = dlouhy[start + i]
            if c2 != '0' and c2 != ch:
                break
        else:
            return start
    return -1

def vrat_texty_radek_sloupec(matice: list[str], souradnice: list[tuple[int, int]]) -> list[str]:
    """
    Vybere řádky a sloupce z matice na zadaných souřadnicích.
    
    Args:
        matice: Seznam řetězců představující matici
        souradnice: Seznam souřadnic ve formátu [(řádek, sloupec), ...]
    
    Returns:
        Seznam obsahující vybrané sloupce a řádky jako řetězce
    """
    if not matice or not matice[0]:
        raise ValueError("Prázdná matice")

    vysledek = []
    for radek, sloupec in souradnice:
        if radek < 0 or radek >= len(matice) or sloupec < 0 or sloupec >= len(matice[0]):
            raise ValueError(f"Neplatné souřadnice ({radek}, {sloupec})")
        
        vybrany_sloupec = ''.join(row[sloupec] for row in matice)
        vybrany_radek = matice[radek]
        
        vysledek.extend([vybrany_sloupec, vybrany_radek])
    
    return vysledek


def vrat_texty_uhlopricne(matice: list[str], souradnice: list[tuple[int, int]]) -> list[str]:
    """
    Vrací celé úhlopříčky jako řetězce, které procházejí zadanými souřadnicemi.
    Úhlopříčky začínají a končí na hranici matice.

    Args:
        matice: Seznam řetězců představující matici (řádky)
        souradnice: Seznam souřadnic [(řádek, sloupec)]

    Returns:
        Seznam řetězců z obou úhlopříček (↖ a ↙) pro každou souřadnici
    """
    vysledek = []
    max_radek = len(matice)
    max_sloupec = len(matice[0])

    for r, s in souradnice:
        if r < 0 or r >= max_radek or s < 0 or s >= max_sloupec:
            raise ValueError(f"Neplatné souřadnice ({r}, {s})")

        # ↖ úhlopříčka: najdi start na hranici
        i, j = r, s
        while i < max_radek - 1 and j < max_sloupec - 1:
            i += 1
            j += 1
        diag_up_left = ""
        while i >= 0 and j >= 0:
            diag_up_left += matice[i][j]
            i -= 1
            j -= 1

        # ↙ úhlopříčka: najdi start na hranici
        i, j = r, s
        while i > 0 and j < max_sloupec - 1:
            i -= 1
            j += 1
        diag_down_left = ""
        while i < max_radek and j >= 0:
            diag_down_left += matice[i][j]
            i += 1
            j -= 1

        vysledek.append(diag_up_left)
        vysledek.append(diag_down_left)

    return vysledek

def obraceni_textu(pole: list[str]) -> list[str]:
    """
    Vrátí pole textů pozpátku.
    
    Args:
        pole: Seznam řetězců, které mají být obráceny.
    
    Returns:
        Seznam obrácených řetězců.
    """
    return [text[::-1] for text in pole]
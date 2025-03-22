# Szyfr Vigenere'a i Kryptoanaliza

## Opis

Szyfr Vigenere'a jest zestawem szyfrów Cezara, gdzie kluczem jest układ liczb \( k = <k_0, k_1, ..., k_{n-1}> \), który jest zapisywany raczej w postaci liter. Każda litera tekstu jawnego jest szyfrowana (i odszyfrowywana) za pomocą szyfru Cezara przy użyciu kolejnych liczb klucza. Dokładniej, dla \( x \) będącego m-tą literą tekstu jawnego, oraz \( j = m \mod n \) (reszta z dzielenia m przez długość klucza n), szyfrowanie i deszyfrowanie odbywa się według wzoru:

- \( E(k, x) = x + k_j \)
- \( D(k, y) = y - k_j \)

Gdzie:
- \( E(k, x) \) to funkcja szyfrująca,
- \( D(k, y) \) to funkcja odszyfrowująca.

## Kryptoanaliza

Kryptoanaliza szyfru Vigenere'a jest łatwa w przypadku znajomości długości klucza i przynajmniej n par tekstu jawnego oraz zaszyfrowanego. Jednakże, jeśli mamy tylko szyfrogram, metoda przeszukiwania wyczerpującego staje się niepraktyczna, ponieważ przestrzeń kluczy ma rozmiar \( 26^n \), co jest zbyt dużą przestrzenią nawet dla niewielkich wartości n. W tym przypadku stosuje się analizę częstotliwości.

### Częstotliwość liter w języku angielskim:

Wektory częstotliwości występowania liter w języku angielskim (w promilach) są następujące:

| Litera | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wartość| 82 | 15 | 28 | 43 | 127 | 22 | 20 | 61 | 70 | 2 | 8 | 40 | 24 | 67 | 75 | 29 | 1 | 60 | 63 | 91 | 28 | 10 | 23 | 1 | 20 | 1 |

### Kryptoanaliza przez przesunięcia:

1. **Krok 1: Znalezienie długości klucza**  
   Aby znaleźć długość klucza, dla kolejnych liczb \( j = 1, 2, \dots \) dokonuje się przesunięcia tekstu zaszyfrowanego o \( j \) pozycji i oblicza liczbę koincydencji (identycznych liter) na tych samych pozycjach w oryginalnym tekście i przesuniętym. Znalezienie wielu koincydencji wskazuje na wielokrotność długości klucza. Najmniejsza taka liczba to długość klucza \( n \).

2. **Krok 2: Kryptoanaliza częstotliwości**  
   Po znalezieniu długości klucza, dla każdego \( i = 0, 1, \dots, n-1 \), wydzielamy część kryptogramu na pozycjach \( i \mod n \). Dla każdej z takich części obliczamy wektor \( V \) częstotliwości występowania liter w tej części. Zakłada się, że ten wektor jest zbliżony do wektora \( W \) z pewnym przesunięciem. Przesunięcie to jest kluczem szyfru Cezara na tej pozycji.

## Zadanie

Zaprogramuj szyfrowanie i odszyfrowywanie wiadomości przy użyciu szyfru Vigenere'a. Zakłada się, że tekst jawny jest ciągiem małych liter bez spacji, cyfr i znaków przestankowych. Taki tekst jawny można przygotować z dostępnego tekstu przy użyciu odpowiedniego narzędzia.

### Opcje programu:

Program o nazwie `vigenere` powinien umożliwiać wywołanie z linii komend z następującymi opcjami:

- `-p` - Przygotowanie tekstu jawnego do szyfrowania.
- `-e` - Szyfrowanie.
- `-d` - Odszyfrowywanie.
- `-k` - Kryptoanaliza wyłącznie na podstawie kryptogramu.

### Pliki:

- `plain.txt` - Plik z tekstem jawnym.
- `crypto.txt` - Plik z tekstem zaszyfrowanym.
- `decrypt.txt` - Plik z tekstem odszyfrowanym.
- `key.txt` - Plik zawierający klucz.
- `orig.txt` - Oryginalny tekst przed przygotowaniem do szyfrowania.
- `key-found.txt` - Plik z kluczem znalezionym w wyniku kryptoanalizy.

### Uwagi:

- Kryptoanaliza jest bardziej skuteczna w przypadku dłuższych kryptogramów (np. artykułów prasowych), które zawierają setki lub więcej znaków. Krótkie kryptogramy mogą być trudniejsze do odszyfrowania bez znajomości klucza.

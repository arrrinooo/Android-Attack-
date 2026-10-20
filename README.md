# Android Attack

Prosta gra zręcznościowa (arcade) stworzona w języku Python przy użyciu biblioteki Pygame.

## Zasady gry

Twój cel jest prosty: przetrwać jak najdłużej i zebrać jak najwięcej punktów.

1.  **Sterowanie:**
    * Użyj klawisza **W**, aby lecieć w górę.
    * Użyj klawisza **S**, aby lecieć w dół.
2.  **Punkty:**
    * Zbieraj **Gwiazdki**. Każda gwiazdka to +10 punktów.
    * Z czasem gra przyspiesza, a gwiazdki i wrogowie poruszają się szybciej.
3.  **Zagrożenia:**
    * Unikaj **Androidów**. Zderzenie z nimi zabiera jedno życie.
    * Masz tylko **3 życia**. Po ich utracie gra się kończy.
4.  **High Score:**
    * Gra automatycznie zapamiętuje Twój najlepszy wynik (zapisuje go w pliku `highscore.txt`). Spróbuj go pobić!

## Technologie i Narzędzia

Gra została napisana w **Pythonie** i korzysta z następujących technologii:

* **Silnik gry:** [Pygame 2.6.1](https://www.pygame.org/docs/)
    * Biblioteka posłużyła do obsługi grafiki, sterowania oraz kolizji.

### Grafika i Design:
* **Pixel Art (Rakieta, wrogowie, gwiazdki):** Stworzone przy użyciu edytora [LibreSprite](https://libresprite.github.io/#!/).
* **Ramka automatu (Overlay):** Wygenerowana przy pomocy sztucznej inteligencji [PixVerse AI](https://app.pixverse.ai/).

## Źródła i Inspiracje

Projekt powstał w celach edukacyjnych. Przy jego tworzeniu korzystałam z następujących źródeł:

* **Główna inspiracja:** Tutorial na kanale Clear Code na YouTube: [Oglądaj tutaj](https://www.youtube.com/watch?v=-FoziIlV7N0&t=3532s). To wideo pomogło mi zrozumieć podstawy struktury gry w Pygame.
* **Literatura i podstawy:**
    * Podstawy języka Python i programowania opanowałam dzięki książce **"Hello World! Computer Programming for Kids and Other Beginners"** (Warren Sande, Carter Sande). [Link do materiałów](https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Python/Hello%20World%20-%20Computer%20Programming%20for%20Kids%20and%20Other%20Beginners%2C%20Fourth%20printing%20%282009%29.pdf).
* **Dokumentacja Pygame i wiedza ogólna:**
    * Rozwiązania dotyczące mechaniki ruchu oraz obsługa przycisków myszką zostały zaimplementowane w oparciu o oficjalną [dokumentację Pygame](https://www.pygame.org/docs/) oraz ogólnodostępne poradniki programistyczne.


---
## Miłej gry!
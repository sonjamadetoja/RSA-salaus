# Testausdokumentti (alustava versio)

## Yksikkötestauksen kattavuusraportti

Raportti löytyy Codecovista, [klikkaa tästä](https://app.codecov.io/gh/sonjamadetoja/RSA-salaus/).
    
## Mitä on testattu ja miten?

Ohjelmaa testataan yksikkötesteillä, jotka on automatisoitu käyttäen unittestiä. GitHub Actions suorittaa testit automaattisesti jokaisen commitin yhteydessä ja Codecov kertoo testikattavuuden. 

Yksikkötesteillä on testattu KeyCreationMachine-luokka 99% kattavuudella. KeyPair-luokka sisältää vain gettereitä, joten sitä ei ole varsinaisesti testattu.

Koodin laatua on testattu Pylintillä. Pistemäärä on 10.0/10.

## Minkälaisilla syötteillä testaus tehtiin?

Syötteitä on käytetty check_if_prime-funktion testauksessa. Testeissä käytettiin syötteenä kahta suurta lukua, joista toinen on alkuluku ja toinen ei.

## Miten testit voidaan toistaa?

Testit voidaan toistaa terminaalissa komennolla 'pytest'. 

Testikattavuus voidaan hakea terminaalissa seuraavasti:
1. Anna komento 'coverage run --branch -m pytest'
2. Anna komento 'coverage report -m' nähdäksesi raportin terminaalissa.

TAI 

2. Anna komento 'coverage html' tuottaaksesi raportin html muodossa.

Koodin laadun testauksen voi toistaa terminaalissa komennolla 'pylint src'.

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa


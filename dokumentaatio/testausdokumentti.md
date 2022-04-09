# Testausdokumentti (alustava versio)

## Yksikkötestauksen kattavuusraportti

Raportti löytyy Codecovista, [klikkaa tästä](https://app.codecov.io/gh/sonjamadetoja/RSA-salaus/branch/main).
    
## Mitä on testattu ja miten?

Ohjelmaa testataan yksikkötesteillä, jotka on automatisoitu käyttäen unittestiä. GitHub Actions suorittaa testit automaattisesti jokaisen commitin yhteydessä ja Codecov kertoo testikattavuuden. 

Yksikkötesteillä on testattu KeyCreationMachine-luokka 99% kattavuudella. KeyPair-luokka sisältää vain gettereitä, joten sitä ei ole varsinaisesti testattu.

Myös MessageProcessing-luokka on testattu yksikkötesteillä 100% kattavuudella.

Koodin laatua on testattu Pylintillä. Pistemäärä on 10.0/10.

## Minkälaisilla syötteillä testaus tehtiin?

Syötteitä on käytetty check_if_prime-funktion testauksessa. Testeissä käytettiin syötteenä kahta suurta lukua, joista toinen on alkuluku ja toinen ei.

Lisäksi salauksen toiminnan testaamisessa käytettiin testiviestinä satunnaisesti generoitua viestiä: "En rihmoihin taallakin olevinasi parjaavat kaksikaan se." Salausavaimina käytettiin sovelluksen tuottamia avaimia.

## Suorituskykytestaus

Suorituskykytestausta aloitin kokeilemalla luoda 100 kertaa salausavainparin käyttäen 1024 bitin kokoisia alkulukuja. Keskiarvo alkulukuparin luomisen kestolle oli 3.297859284877777242e+00 eli noin 3,3 sekuntia.


## Miten testit voidaan toistaa?

Testit voidaan toistaa terminaalissa komennolla 'pytest'. 

Testikattavuus voidaan hakea terminaalissa seuraavasti:
1. Anna komento 'coverage run --branch -m pytest'
2. Anna komento 'coverage report -m' nähdäksesi raportin terminaalissa.

TAI 

2. Anna komento 'coverage html' tuottaaksesi raportin html muodossa.

Koodin laadun testauksen voi toistaa terminaalissa komennolla 'pylint src'.


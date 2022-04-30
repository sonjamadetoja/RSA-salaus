# Testausdokumentti (alustava versio)

## Yksikkötestauksen kattavuusraportti

Raportti löytyy Codecovista, [klikkaa tästä](https://app.codecov.io/gh/sonjamadetoja/RSA-salaus/branch/main).
    
## Mitä on testattu ja miten?

Ohjelmaa testataan yksikkötesteillä, jotka on automatisoitu käyttäen unittestiä. GitHub Actions suorittaa testit automaattisesti jokaisen commitin yhteydessä ja Codecov kertoo testikattavuuden. 

Yksikkötesteillä on testattu KeyCreationMachine-luokka 99% kattavuudella. KeyPair-luokka sisältää vain gettereitä, joten sitä ei ole varsinaisesti testattu.

Myös MessageProcessing-luokka on testattu yksikkötesteillä 92% kattavuudella.

Koodin laatua on testattu Pylintillä. Pistemäärä on 9.80/10.

## Minkälaisilla syötteillä testaus tehtiin?

Syötteitä on käytetty check_if_prime-funktion testauksessa. Testeissä käytettiin syötteenä erilaisia alkulukuja ja yhdistettyjä lukuja.

Salauksen ja purkamisen toiminnan testaamisessa käytettiin testiviestinä kovakoodattua viestiä: "En rihmoihin taallakin olevinasi parjaavat kaksikaan se." Lisäksi käytettiin kahta satunaisesti generoitua merkkijonoa, joista toiselle arvotaan pituus välillä 1-128 ja toiselle välillä 129-256.

Salausavaimina käytettiin sovelluksen tuottamia avaimia.

## Suorituskykytestaus

Suorituskykytestausta aloitin kokeilemalla luoda 100 kertaa salausavainparin käyttäen 1024 bitin kokoisia alkulukuja. Keskiarvo salausavainparin luomisen kestolle oli 3.297859284877777242e+00 eli noin 3,3 sekuntia ennen Eratostheneen seulan käyttöönottoa. Seulan käyttöönoton jälkeen sama keskiarvo oli 1.428238835334777912e+00 eli noin 1,4 sekuntia.

Viestin salausta testasin viestillä "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae proin. Nulla porttitor massa id neque aliquam vestibulum morbi bla", joka on 256 bittiä pitkä. Salasin viestin 100 kertaa ja purin salauksen 100 kertaa. Keskiarvo salauksen kestolle oli 0.00017 sekuntia, ja keskiarvo purun kestolle oli 0.00019 sekuntia.

## Miten testit voidaan toistaa?

Ennen testaamista projekti täytyy alustaa komennolla 'poetry install'

### Yksikkötestit

Yksikkötestit voidaan toistaa terminaalissa komennolla 'pytest'.

Testikattavuus voidaan hakea terminaalissa seuraavasti:
1. Anna komento 'coverage run --branch -m pytest'
2. Anna komento 'coverage report -m' nähdäksesi raportin terminaalissa.

TAI 

2. Anna komento 'coverage html' tuottaaksesi raportin html muodossa.

### Pylint

Koodin laadun testauksen voi toistaa terminaalissa komennolla 'pylint src'.

### Suorituskykytestaus

Suoritustestauksen voi toistaa seuraavasti:

1. Käynnistä virtuaaliympäristö komennolla 'poetry shell'
2. Käynnistä testitiedosto komennolla 'python3 src/performance.py'

Ohjelma tulostaa toiminnan keston 100 toiston keskiarvot salausavainparin luomiselle, esimerkkitekstin salaamiselle ja salauksen purkamiselle.

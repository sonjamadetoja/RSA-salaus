# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman koostuu neljästä luokasta: UI sisältää käyttöliittymän, KeyCreationMachine sisältää salausavainten luomiseen tarvittavat toiminnot, MessageProcessing sisältää salaukseen ja salauksen purkamiseen vaadittavat toiminnot, ja KeyPair-luokka muodostaa avainpariolion, joka sisältää avainparin osaset.

### Miller-Rabin
Miller-Rabinin metodia käytetään testaamaan onko luku alkuluku. Tämän metodin avulla voidaan generoida suuria alkulukuja salauksen pohjaksi. Metodia käytetään funktiossa one_test, jota puolestaan kutsutaan funktiosta check_if_prime, joka toistaa testin silmukassa niin monta kertaa, kun funktiolle annetussa argumentissa on määritelty. Koska kyseessä on probabilistinen testi, toistoja tulee olla riittävästi. Tällä kertaa on käytetty 40 toistoa.

Miller-Rabinin testi perustuu havaintoon, että pariton luku n voidaan kirjoittaa muodossa 2^s⋅d + 1, niin että s ja d ovat positiivisia kokonaislukuja ja d on pariton. Tällöin on olemassa todennäköinen alkuluku a, joka on suurempi kuin 0 ja pienempi kuin n, ja jolle pätee että kun se korotetaan potenssiin d, se on kongruentti 1:n kanssa modulo n, ja kun se korotetaan potenssiin 2^r⋅d, se on kongruentti -1:n kanssa modulo n. 

#### Aika- ja tilavaativuudet

Miller-Rabin testin aikavaativuus on O(k log^3 n), jossa n on testattava luku ja k kierrosten määrä, ja tilavaativuus on O(1).

### Eukleideen algoritmi
Eukleideen algoritmilla etsitään kahdelle luvulle suurin yhteinen tekijä. Käytän sitä funktiossa calculate_gcd_ext, joka toimii rekursiivisesti.

Eukleideen algoritmissa muodostetaan kyseisille luvuille jakoyhtälö, ja sen jälkeen toinen luvuista jaetaan yhtälön jakojäännöksellä. Tätä toistetaan niin kauan, kunnes jakojäännös on nolla. Tällöin suurin yhteinen tekijä on viimenen jakojäännös, joka ei ole nolla. Algoritmin laajennetussa versiossa puolestaan prosessi toistetaan päinvastaiseen suuntaan, jotta saadaan selville, millä luvuilla alkuperäiset luvut tulee kertoa, jotta niiden summasta muodostuu suurin yhteinen tekijä.

#### Aika- ja tilavaativuudet

Laajennetun Eukleideen algoritmin aikavaativuus on O(log n), eli se toimii logaritmisessa ajassa, ja tilavaativuus on O(1).

### Eratostheneen seula

Eratostheneen seula on vanha algoritmi, jolla voi etsiä kaikki tiettyä lukua pienemmät alkuluvut. Se merkitsee yhdistetyksi luvuksi kaikki sellaiset luvut, jotka ovat jaollisia jollain aiemmalla luvulla. Luvut löydetään käymällä läpi kakkosesta ylöspäin kaikki sellaiset luvut, joita ei ole jo merkitty yhdistetyksi luvuksi. Lukuja käydään läpi ylärajan neliöjuureen saakka.

Ohjelmassa käytän Eratostheneen seulaan generoimaan listan pieniä alkulukuja, ja käytän sitä apuna alkulukutarkistuksessa niin, että ensin tarkistan onko testattava luku jaollinen pienimmillä alkuluvuilla, ja vasta sen jälkeen luvulle tehdään tarvittaessa Miller-Rabinin testi. Tämä nopeuttaa testausta.

#### Aika- ja tilavaativuudet

Eratostheneen seulan aikavaativuus on O(n log log n) ja tilavaativuus O(n).

### Salausavainten luominen

Salausavainten luominen alkaa kahden toisistaan poikkeavan alkuluvun luomisella. Sen jälkeen muodostetaan luku n (eli modulus) niiden tulona. Seuraavaksi valitaan eksponentti e, ja lasketaan e:n ja n:n avulla eksponentti d seuraavasti: kummastakin alkuluvusta vähennetään 1 ja etsitään niiden pienin yhteinen jakaja Eukleideen algoritmin avulla, ja kerrotaan se e:llä. E:n valinnasta: sen tulee olla suurempi kuin yksi ja pienempi kuin yhdellä vähennettyjen alkulukujen tulo, jonka kanssa sen tulee myös olla keskenään jaoton. Salaus on tehokkaampaa, jos sillä on lyhyt bittipituus ja pieni Hamming-paino, joten usein käytetään lukua 2^16 + 1 = 65537 - niin tässäkin ohjelmassa.

Julkisen avaimen muodostavat e ja n, ja salaisen avaimen muodostavat d ja n.

### Salaaminen ja purkaminen

Viesti salataan korottamalla se potenssiin e ja ottamalla modulo n. Salattu viesti puretaan korottamalla se potenssiin d ja ottamalla modulo n.

## Työn mahdolliset puutteet ja parannusehdotukset

Työhön ei ole toteutettu paddingiä, joka tarkoittaa ylimääräisten merkkien lisäämistä turvallisuuden takaamiseksi. Tämä on edellytys turvalliselle salaukselle.

Ohjelma toimii vain viesteillä, jotka ovat korkeintaan 256 bittiä pitkiä.

Tällä hetkellä luotavan salausavaimen pituus on kovakoodattu ohjelmaan, mutta sen voisi jättää myös käyttäjän määriteltäväksi.

Ohjelma voisi myös ilmoittaa, jos salatessa tai purkaessa yrittää antaa virheellisen avaimen.

## Lähteet
* [RSA](https://fi.wikipedia.org/wiki/RSA)
* [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
* [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
* [Euclidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
* [Extended Euclidian algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
* [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
* [Modulaarinen aritmetiikka](https://fi.wikipedia.org/wiki/Modulaarinen_aritmetiikka)
* [Keskenään jaottomat luvut](https://fi.wikipedia.org/wiki/Kesken%C3%A4%C3%A4n_jaottomat_luvut)


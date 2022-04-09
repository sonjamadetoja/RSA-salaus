# Toteutusdokumentti (alustava versio)

## Ohjelman yleisrakenne

Ohjelman koostuu neljästä luokasta: UI sisältää käyttöliittymän, KeyCreationMachine sisältää salausavainten luomiseen tarvittavat toiminnot, MessageProcessing sisältää salaukseen ja salauksen purkamiseen vaadittavat toiminnot, ja KeyPair-luokka muodostaa avainpariolion, joka sisältää avainparin osaset.

### Miller-Rabin
Miller-Rabinin metodia käytetään testaamaan onko luku alkuluku. Tämän metodin avulla voidaan generoida suuria alkulukuja salauksen pohjaksi. Metodia käytetään funktiossa one_test, jota puolestaan kutsutaan funktiosta check_if_prime, joka toistaa testin silmukassa niin monta kertaa, kun funktiolle annetussa argumentissa on määritelty. Koska kyseessä on probabilistinen testi, toistoja tulee olla riittävästi. Tällä kertaa on käytetty 40 toistoa.

Miller-Rabinin testi perustuu havaintoon, että pariton luku voidaan kirjoittaa muodossa 2^s⋅d + 1, niin että s ja d ovat positiivisia kokonaislukuja ja d on pariton. Tällöin on olemassa todennäköinen alkuluku a, joka on suurempi kuin 0 ja pienempi kuin n, ja jolle pätee että kun se korotetaan potenssiin d, se on kongruentti 1:n kanssa modulo n, ja kun se korotetaan potenssiin 2^r⋅d, se on kongruentti -1:n kanssa modulo n. 

### Eukleideen algoritmi
Eukleideen algoritmilla etsitään kahdelle luvulle suurin yhteinen tekijä. Käytän sitä funktiossa calculate_gcd_ext, joka toimii rekursiivisesti.

Eukleideen algoritmissa muodostetaan kyseisille luvuille jakoyhtälö, ja sen jälkeen toinen luvuista jaetaan yhtälön jakojäännöksellä. Tätä toistetaan niin kauan, kunnes jakojäännös on nolla. Tällöin suurin yhteinen tekijä on viimenen jakojäännös, joka ei ole nolla. Algoritmin laajennetussa versiossa puolestaan prosessi toistetaan päinvastaiseen suuntaan, jotta saadaan selville, millä luvuilla alkuperäiset luvut tulee kertoa, jotta niiden summasta muodostuu suurin yhteinen tekijä.

### Salausavainten luominen

Salausavainten luominen alkaa kahden toisistaan poikkeavan alkuluvun luomisella. Sen jälkeen muodostetaan luku n (eli modulus) niiden tulona. Seuraavaksi valitaan eksponentti e, ja lasketaan e:n ja n:n avulla eksponentti d seuraavasti: kummastakin alkuluvusta vähennetään 1 ja etsitään niiden pienin yhteinen jakaja Eukleideen algoritmin avulla, ja kerrotaan se e:llä. E:n valinnasta: sen tulee olla suurempi kuin yksi ja pienempi kuin yhdellä vähennettyjen alkulukujen tulo, jonka kanssa sen tulee myös olla keskenään jaoton. Salaus on tehokkaampaa, jos sillä on lyhyt bittipituus ja pieni Hamming-paino, joten usein käytetään lukua 2^16 + 1 = 65537 - niin tässäkin ohjelmassa.

Julkisen avaimen muodostavat e ja n, ja salaisen avaimen muodostavat d ja n.

### Salaaminen ja purkaminen

Viesti salataan korottamalla se potenssiin e ja ottamalla modulo n. Salattu viesti puretaan korottamalla se potenssiin d ja ottamalla modulo n.

## Saavutetut aika- ja tilavaativuudet

## Työn mahdolliset puutteet ja parannusehdotukset

Työhön ei ole toteutettu paddingiä, joka tarkoittaa ylimääräisten merkkien lisäämistä turvallisuuden takaamiseksi. Tämä on edellytys turvalliselle salaukselle.

Ohjelma ei vielä toimi kovin pitkillä viesteillä.

Testeissä voisi vielä suorittaa alkulukutestausta suuremmilla määrillä alkulukuja ja ei-alkulukuja.

## Lähteet
[RSA](https://fi.wikipedia.org/wiki/RSA)
[RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
[Euclidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
[Extended Euclidian algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
[Modulaarinen aritmetiikka](https://fi.wikipedia.org/wiki/Modulaarinen_aritmetiikka)
[Keskenään jaottomat luvut](https://fi.wikipedia.org/wiki/Kesken%C3%A4%C3%A4n_jaottomat_luvut)


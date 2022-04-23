# Viikkoraportti 5

## Mitä olen tehnyt?

Tällä viikolla olen tehnyt vertaisarvioinnin ja korjannut sovellukseni tyyppimuunnostoimintoja sekä kirjoitusvirheitä.

Olen käynyt huolellisesti läpi itse saamani vertaisarvioinnit ja tehnyt muutoksia ohjelmaani niiden perusteella. Olen lisännyt syötteiden tarkistukset sekä virheilmoituksia virheellisten syötteiden varalta. Olen lisännyt viimeksi generoidun salausavaimen tallentamisen ohjelman käytön ajaksi sekä mahdollisuuden poistaa tallennuksen. Olen ohjelmoinut Eratostheneen seulan nopeuttamaan alkulukutestausta. Sen pohjana käytin Wikipediasta löytyvää pseudokoodia: [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode) Lisäksi olen parantanut testausdokumenttia. Seulan käyttöönoton jälkeen avaimen luomisen keston keskiarvo sadalla toistolla laski 3,3:sta 1,4:een sekuntiin. Olen myös ohjelmoinut salausavaimen tallentamisen tekstitiedostoon.

Olen myös kirjoittanut ohjelmalle [käyttöohjeen](https://github.com/sonjamadetoja/RSA-salaus/blob/main/dokumentaatio/kayttoohje.md) ja päivittänyt [toteutusdokumentin](https://github.com/sonjamadetoja/RSA-salaus/blob/main/dokumentaatio/toteutusdokumentti.md).

Yritin löytää jotain sopivaa alkulukulistaa alkulukutestausfunktion testaamiseen, mutta en löytänyt mitään sopivaa kohtuullisella vaivalla.

## Mitä olen oppinut?

Opin muuntamaan tekstin numeroksi järkevästi encode() ja decode() sekä from_bytes() ja to_bytes() toimintoja hyödyntäen. Toiminto from_bytes() tarvitsee argumentiksi tekstin pituuden tavuina, jonka saa laskettua seuraavasti: (teksti.bit_length()+7)//8.

Moduluksen (n) pituus on salausavaimen pituus, ja kahden sen luomiseen käytetyn alkuluvun tulisi olla hieman eri pituisia. [Lähde](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation) Laitoin ohjelmaani niin, että toinen on 1024 bittiä ja toinen 1030 bittiä. Näin moduluksen ja siten salausavaimenpituukseksi tulee 2053 tai 2054 bittiä. NIST on suositellut vuodesta 2015 lähtien 2048 bitin pituisia salausavaimia RSA:han, ja RSA Security on arvioinut, että 2048 bitin pituiset avaimet pysyvät murtumattomina vuoteen 2030 saakka. [Lähde](https://en.wikipedia.org/wiki/Key_size#Asymmetric_algorithm_key_lengths)

Jos modulus on 2048 bittiä pitkä, sillä voi salata viestejä, joiden pituus on maksimissaan 256 tavua (eli moduluksen pituus 2048 bittiä / 8).

Olen oppinut toteuttamaan Eratostheneen seulan.

Olen kerrannut pythonin file-toimintoja.

## Mikä jäi epäselväksi?

Mitä mun kannattaisi vielä lisätä ohjelmaan saadakseni paremman arvosanan? Mikä olisi hyödyllisin asia oppia tässä vaiheessa projektia? Mihin kannattaa keskittyä ja panostaa tässä vaiheessa?

Avaimen tallentaminen tiedostoon on nyt minulla sovelluksen käyttöliittymässä. Onko tämä ok vai missä luokassa sen tulisi olla? Pohdin sen siirtämistä KeyCreationMachine-luokkaan, mutta en ole varma. Pitäisikö luoda sille oma luokka? Se tuntuu tarpeettomalta, koska kyseessä on niin pieni toiminto.

## Mitä teen seuraavaksi?

Ainakin aika- ja tilavaativuusanalyysit pseudokoodista ja ehkä lisää suorituskykytestausta. En ole varma mitä muuta kannattaisi tehdä tässä vaiheessa. Pitäisikö lisätä ominaisuuksia sovellukseen?

## Kuinka paljon aikaa käytin tällä viikolla?

12 h

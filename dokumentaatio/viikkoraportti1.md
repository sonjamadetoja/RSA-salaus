# Viikkoraportti 1

## Mitä olen tehnyt?

Tällä viikolla olen perehtynyt aiheeseen selvittäen, miten RSA-salaus toimii pääpiirteittäin, ja millaisia algoritmeja siinä käytetään, lukemalla lähteitä ja keskustelemalla ohjaajan kanssa. Olen kirjoittanut määrittelydokumentin ja luonut projektin GitHubiin. Lisäksi olen tutustunut kurssimateriaaliin ja rekisteröitynyt kurssille Labtoolissa.

## Mitä olen oppinut?

Olen oppinut miten RSA-avain luodaan, ja miksi salaus toimii. Siinä käytetään hyväksi suuria satunnaisia alkulukuja ja moduloa. Sen toteuttamisessa hyödynnetään Miller-Rabin-menetelmää ja laajennettua Eukleideen algoritmia. Salausta voi käyttää myös digitaalisten allekirjoitusten luomiseen. Viesti täytyy muuttaa tekstistä heksadesimaaleiksi, jotta se voidaan salata, ja siihen täytyy lisätä ylimääräisiä merkkejä, jotta se on tarpeeksi monimutkainen luotettavasti salattavaksi. Pythonissa on toiminnot, joilla tekstin voi muuttaa ensin binääriksi ja sitten heksadesimaaleiksi.

## Mikä jäi epäselväksi?

En ole varma osaanko toteutta 'paddingiä' eli ylimääräisten merkkien lisäystä. Siihen on olemassa Optimal asymmetric encryption padding -niminen kaavio, mutta en täysin ymmärrä kaaviota, enkä ole varma osaanko toteuttaa sitä ohjelmoimalla.

## Mitä teen seuraavaksi?

Ensi viikolla suunnittelen ohjelman rakennetta ja alan ohjelmoida suuria satunnaislukuja tuottavaa toimintoa. Se jälkeen teen salausavaimen tuottavan toiminnon, ja lopuksi salaus- ja purkamistoiminnot.

Ensi viikolla alustan projektin Poetry-ympäristön, ja otan koodiin käyttöön Docstringin ja Pylintin. Testaamisessa käytän Unittestiä ja Codecovia. Testien suorittamisen automatisoimiseen käytän GitHubin Actions-toimintoa.

## Kuinka paljon aikaa käytin tällä viikolla?

Noin neljä tuntia.

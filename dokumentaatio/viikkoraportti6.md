# Viikkoraportti 6

## Mitä olen tehnyt?

Olen lisännyt erilaisia alkulukuja sekä yhdistettyjä lukuja check_if_prime-funktion testeihin. Olen lisännyt salaus- ja purkamistoimintoille testit, jotka testaavat niitä satunnaisesti arvotuilla satunnaisen pituisilla merkkijonoilla. Olen refaktoroinut käyttöliittymäkoodia, lisännyt repositorioon koodin suorituskykytestien toistamiselle ja kirjoittanut dokumentaatiota (testaus- ja toteutusdokumentti).

Pieniä korjauksia, mm: lisäsin Pylintin Actions workflowhun ja poistin performance.py:n ja keypair.py:n coverage-raportista, koska ensimmäistä ei tarvitse testata (se ei ole osa varsinaista ohjelmaa) ja toisessa on vain gettereitä. Nyt raportti antaa totuudenmukaisen tuloksen.

Lisäksi perehdyin toisen opiskelijan sovellukseen huolellisesti ja tein siitä vertaisarvion.

## Mitä olen oppinut?

Opin sekä kertasin erinäisiä Pythonin toimintaan liittyviä seikkoja, jotka liittyivät yllä kerrottuihin tehtäviin.

## Mikä jäi epäselväksi?

Onko alkulukutestauksessa nyt sopiva määrä syötteitä? Milloin testi on niin aikaavievä, että se pitää siirtää erilliseen testiohjelmaan? Miten sellainen kannattaa toteuttaa? Pitääkö niitä salauksen ja purkamisen testejä, joissa arvotaan satunnainen viesti, toistaa useita kertoja?

Yritin tehdä testin, joka testaa, message_processing.py-tiedoston riviä 35-36, että tuleeko UnicodeDecodeError virheellisellä avaimella purkaessa. Käytettäessä sovellus kyllä toimii oikein niissä tilanteissa, ja antaa halutun virheilmoituksen, mutta en millään saanut testiä toimimaan. Jostain syystä se ei saanut poikkeusta kiinni.

Seuraavia tapoja:

```bash
with self.assertRaises(UnicodeDecodeError) as context:
    self.MP.message_to_string(message_as_int)
```
    
```bash
self.assertRaises(UnicodeDecodeError, self.MP.message_to_string, message_as_int)
```

Olen kirjoittanut [toteutusdokumenttia](https://github.com/sonjamadetoja/RSA-salaus/blob/main/dokumentaatio/toteutusdokumentti.md). Onko se riittävä? Olen ilmoittanut tila- ja aikavaativuudet kunkin algoritmin kohdalla. Onko tämä sopiva ja riittävä tapa? 

Onko [testausdokumentti](https://github.com/sonjamadetoja/RSA-salaus/blob/main/dokumentaatio/testausdokumentti.md) riittävä?

## Mitä teen seuraavaksi?

En tiedä. Varmaan korjailen ilmenneitä puutteita ja valmistaudun demo-tilaisuuteen.

## Kuinka paljon aikaa käytin tällä viikolla?

6 h

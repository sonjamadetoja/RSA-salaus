# Käyttöohje

Ohjelmalla voi luoda ja käyttää epäsymmetrisiä salausavainpareja. Niihin kuuluu kolme osaa: modulus, julkinen osa ja yksityinen osa.

Viesti salataan moduluksen ja julkisen osan avulla. Voit halutessasi antaa ne muille, jotta he voivat salata viestejä.

Viestin salaus puretaan moduluksen ja yksityisen osan avulla. Älä koskaan paljasta salausavaimen yksityistä osaa muille.

# Asennus

Asenna ohjelma komennolla 'poetry install'.

# Käynnistys

Käynnistä virtuaaliympäristö komennolla 'poetry shell' ja sen jälkeen käynnistä ohjelma komennolla 'python3 src/index.py'.

# Toiminnot

Valitse numerolla haluamasi toiminto ja paina enter. Toiminnot:
1 Luo salausavainpari
2 Salaa viesti
3 Pura viestin salaus
4 Poista viimeksi luotu avain muistista
5 Lopeta

## Luo salausavainpari

Valitse päävalikossa numero '1'. Toiminto luo salausavainparin ja tulostaa sen osat näytölle, josta ne voi kopioida. Älä paljasta yksityistä osaa kenellekään muulle. Ohjelma myös tallentaa viimeisimmäksi luodun salausavaimen käyttöä varten ohjelman käynnissäoloajaksi.

## Salaa viesti

Valitse päävalikossa numero '2'.

Ensin ohjelma pyytää salattavaa viestiä. Viestin pituus voi olla korkeintaan 256 tavua.

Jos olet luonut ohjelmalla salausavaimen, ohjelma kysyy haluatko käyttää sitä salaamiseen. Vastaa 'kyllä' tai 'ei'. Jos vastaat ei, tai jos et ole luonut avainta tällä käyttökerralla, ohjelma pyytää antamaan salausavaimen moduluksen ja julkisen osan. Sen jälkeen ohjelma tulostaa viestin salatussa muodossa.

## Pura viestin salaus

Valitse päävalikossa numero '3'.

Ensin ohjelma pyytää salattua viestiä. Sen tulee olla numeromuodossa.

Jos olet luonut ohjelmalla salausavaimen, ohjelma kysyy haluatko käyttää sitä salaamiseen. Vastaa 'kyllä' tai 'ei'. Jos vastaat ei, tai jos et ole luonut avainta tällä käyttökerralla, ohjelma pyytää antamaan salausavaimen moduluksen ja yksityisen osan. Sen jälkeen ohjelma tulostaa viestin puretussa muodossa tekstinä.

## Poista viimeksi luotu avain muistista

Jos olet luonut uuden salausavaimen ohjelman tällä käyttökerralla, on se ohjelman muistissa ja voit käyttää sitä helposti viestin salaamiseen ja purkamiseen. Jos haluat poistaa sen muistista, voit tehdä niin valikossa valitsemalla '4'. Jos luodut uuden avaimen, edellinen avain korvautuu sillä. Muistissa oleva avain poistuu muistista myös, jos suljet sovelluksen.

## Lopeta

Sovelluksen voi sulkea päävalikossa valitsemalla '5'.

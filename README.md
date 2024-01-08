# chessLV - automatizēta šaha turnīru pieteikšanās sistēma

## Problēmas raksturojums

Ikdienā projekta autors nodarbojas ar šaha spēlēšanu, tai skaitā, piedaloties dažādos Latvijas organizētos turnīros, kur ņem vērā FIDE reitingu. Lai piedalītos šajos turnīros ir jānosūta pieteikums, kā izveidošana satur vairākas darbības, kas noteikti var aizņemt apmēram no 5 līdz 10 minūtēm:
1. Latvijas Šaha Federācijas [mājaslapā](https://www.sahafederacija.lv/) ir jāatrod sadaļā "Kalendārs" vēlamais turnīrs, kuram vēlas pieteikties.
2. Pie atbilstošā turnīra ir nepieciešams lejupielādēt turnīra nolikumu.
3. Nolikumā pie sadaļas "Pieteikšanās" ir norādīts kā pietiekties un kāda informācija ir jānorāda. Reizēm ir iespēja pieteikties piezvanot pa norādīto tālruni, taču tas ne vienmēr ir iespējams.
4. Parasti pieteikumā ir jānorāda sekojoša informācija: *vārds, uzvārds, atbilstošā tipa reitings (klasika, rapid vai blitz), sporta klase/tituls un pilsēta vai klubs*.
5. FIDE reitingu [mājaslapā](https://ratings.fide.com/) ir jāatrod savs profils, kur ir norādīts pašreizējais reitings.
6. Tad ir jānosūta pieteikums uz norādīto e-pastu. Nosūtot e-pastu, pieteikums ir veikts.

## Projekta uzdevums

Šī projekta ietvaros ir uztaisīta interaktīva sistēma, ko izmantojot ir iespējams veikt automātisku pieteikšanos dažu klikšķu laikā. Šajā projektā izmantotas metodes no sekojošām tēmām:

* Datu saglabāšana un nolasīšana no Excel .xlsx faila;
* Teksta failu apstrāde un nolasīšana, saglabājot tajā pēdējo failu lejupielādes laiku;
* Datu nolasīšana no PDF failiem (turnīra nolikumi), kas satur nepieciešamo informāciju;
* Tīmekļa skrāpēšana, lejupielādējot nolikumus un nolasot pašreizējo reitingu;
* Automātiska e-pasta nosūtīšana;
* Lietojumprogrammatūras automātiska palaišana, izmantojot pakešfailu (Batch script), *pēc izvēles*.

Projekts satur 2 teksta failus (.txt) nepieciešamo Python bibliotēku instalēšanai un pēdējā lejupielādēto failu laika saglabāšanai, 2 Excel failus (.xlsx), kas satur turnīru nolikumu nepieciešamos datus un tiek ģenerēti automātiski, 4 python skriptu failus (.py), lai veiktu nepieciešamās darbības ar failiem, 2 python failu (.py) datu glabāšanai user_info.py, kas tiek saglabāts tikai lokālajā datorā, un user_info_example.py, kur ir norādītas vairāku parametru sākuma vērtības, ko vajag izmainīt. Kā arī vienu python skripa failu (.py) interektīvās sistēmas palaišanai main.py

## Izmantotās Python bibliotēkas

* from tkinter import *
* from tkinter.ttk import *
* import tksheet

* PyPDF2 - 
* openpyxl - load_workbook, Workbook -
* fnmatch -
* os -
* shutil -
* requests -
* urllib.parse - urljoin -
* bs4 - BeautifulSoup -
* datetime - date, datetime -
* smtplib - 
* email.message - EmailMessage -

* *Download, Read, Ratings, Send, user_info*, kas ir izveidotie Python faili un tiek importēti citos failos. 

## Failu apraksti

## Uzstādīšanas instrukcija

### Izveidot lokālu projekta kopiju
```
git clone 
```

```
pip install -r requirements.txt
```


### Pievienot nepieciešamās vērtības
Izveidot jaunu user_info.py failu

```
cp user_info_example.py user_info.py
```
Rediģēt 
## Programmas lietošanas piemērs


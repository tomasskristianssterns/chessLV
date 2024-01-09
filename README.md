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

* **tkinter, tkinter.ttk** - izmantots, lai izveidotu interaktīvu interfeisu ar lietotāju;
* **tksheet** - izmantots, lai UI varētu attēlot datus tabulas veidā, kur parāda turnīru parametrus;
* **PyPDF2** - datu nolasīšanai no lejupielādētajiem PDF failiem;
* **openpyxl** - (*load_workbook, Workbook*) - excel faila izveidošana un tā ielādēšana;
* **fnmatch** - lejupielādēto PDF failu saskaitīšanai;
* **os** - mapju izveidošana un iedarbībai ar operētājsistēmu;
* **shutil** - mapes dzēšana kopā ar lejupielādētajiem PDF failiem;
* **requests** - pieprasījumu veikšana uz norādīto mājaslapu;
* **urllib.parse** - (*urljoin*) - PDF faila saglabāšanai no tīmekļa lejupielādēšanas;
* **bs4** - (*BeautifulSoup*) - vienkāršota datu strukturizēšana, veicot tīmekļa skrāpēšanu;
* **datetime** - (*date, datetime*) - pašreizējā datuma un laika saglabāšanai, izmantošana kā atskaites punkts;
* **smtplib** - SMTP protokols e-pasta nosūtīšanai;
* **email.message** - (*EmailMessage*) - e-pasta struktūras izveidošanai;
* ***Download, Read, Ratings, Send, user_info***, kas ir izveidotie Python faili un tiek importēti citos failos. 

## Failu apraksti

* **main.py** - interaktīvās sistēmas palaišanas fails
* **Download.py** - visu pieejamo PDF failu lejupielādēšana līdz noteiktam datumam
* **Read.py** - visu lejupielādēto PDF failu lasīšana, lai izgūtu e-pasta adreses un turnīra laika kontroles tipu
* **Ratings.py** - visu 3 reitingu tipu iegūšana no tīmekļa
* **Send.py** - e-pasta nosūtīšanas fails
* **user_info_example.py** - **obligāti** norādāmo datu faila piemērs
* **user_info.py** - **obligāti** norādāmo datu fails, ko lietotājs ģenerē
* **update.txt** - pēdējā lejupielādēto PDF failu laiks
* **requirements.txt** - nepieciešamo bibliotēku lejupielādes fails
* **tournaments.xlsx** - lejupielādēto PDF failu strukturizācija, kas tiek ģenerēti programmas laikā
* **final.xlsx** - lejupielādēto + nolasīto PDF failu strukturizācija, kas tiek ģenerēti programmas laikā
* **README.md** - dokumentācijas fails
* **.gitignore** - git ignorēšanas fails (saglabā norādītos failus tikai lokāli)
* **regulations** - visu lejupielādēto PDF failu mape
* **assets/images** - dokumentācijai nepieciešamās bildes

> [!NOTE]
> user_info.py, tournaments.xlsx, final.xlsx un visi faili "regulations" mapē tiek saglabāti tikai uz lokālā datora

## Uzstādīšanas instrukcija

### Izveidot lokālu projekta kopiju
Lejupielādēt lokālu projekta kopiju, piemēram, izmantojot **git**:
```
git clone https://github.com/tomasskristianssterns/chessLV.git
```
Pēc tam lejupielādēt nepieciešamos python moduļus:
```
pip install -r requirements.txt
```

### Pievienot nepieciešamās vērtības
Izveidot jaunu ***user_info.py*** failu, kopējot parauga failu:

```
cp user_info_example.py user_info.py
```
Rediģēt failā **user_info.py** sekojošas vērtības:

* PATH = r"C:\\\Users\\\{path}\\\chessLV\\\regulations"

PATH tiek nomainīts uz lokālā projekta ceļu, galā pievienojot "regulations", kur tiks saglabāti visi PDF nolikumi. To var uzzināt atverot python interaktīvo režīmu:

```
python
```
Un ievadot sekojošas komandas:
```
import os
os.getcwd()
exit()
```

Iegūto failu ceļu nokopē no saglabā mainīgajā PATH, sākumā saglabājot PATH = r"C:\\\..." un beigās saglabājot "..\\\regulations"

* FIDE_ID = ""

FIDE ID tiek nomainīts uz lietotāja FIDE ID vērtību. Ja lietotājam nav FIDE ID, to ir iespējams iegūt [šeit](https://forms.zohopublic.com/virtualoffice22358/form/63277290379193162845/formperma/pgRPQhvR2cQTqOyqYTQrK_soBIuSEYbhIz7bSIDNOD0). Piemēram, ja lietotājam ir izniegts FIDE ID ar vērtību 0123456789, tad viņš nomaina tā vērtību uz:

```
FIDE_ID = 0123456789
```

* MY_EMAIL = ""
* PASSWORD_KEY = ""
* EMAIL_SERVER = "mail.inbox.lv"

Tālāk ir 3 mainīgie, kur jānorāda e-pasts, paroles atslēga un e-pasta serveris. Ja izmanto *"inbox.lv"*, lai nosūtītu e-pastu, tad EMAIL_SERVER vērtība **NAV** jāmaina. Taču izmantojot citu e-pastu nosūtīšanas aplikāciju ir jānorāda attiecīgais e-pasta serveris, piemēram, gmail.com serveris ir: EMAIL_SERVER = "smtp.gmail.com".

Mainīgais MY_EMAIL ir jānomaina uz attiecīgo e-pasta adresi no kā tiks sūtīti pieteikumi šaha turnīram, piemēram, MY_EMAIL = "example@inbox.lv"

Mainīgais PASSWORD_KEY ir jānomaina uz ģenerētu paroles atslēgu. [Šeit](https://help.inbox.lv/category/10200/question/10473) ir pieejama instrukcija kā to var izdarīt "inbox.lv" e-pasta adresei.

Kad šis ir izdarīts ir nepieciešams atvērt **Send.py** failu un izmainīt sekojošas vērtības:

Ja e-pasta adresei atšķiras ports no standarta vērtības (587), tad mainīgo email_port = 587 ir nepieciešams nomainīt uz attiecīgo vērtību.

Kā arī ir nepieciešams nomainīt ziņojuma tekstu msg.set_content, kur vajag izmainīt sekojošus tekstus, kas ir ievietoti iekavās:

* Vārds: (vārds)

(vārds) uz lietotāja vārdu

* Uzvārds: (uzvārds)

(uzvārds) uz lietotāja uzvārdu

* Sporta klase/tituls: (sporta klase)

(sporta klase) uz sporta klasi vai titulu kas pieder lietotājam

* Pilsēta/klubs: (pilsēta)

(pilsēta) uz pilsētu vai klubu ko lietotājs pārstāv

* (vārds uzvārds)

(vārds uzvārds) uz lietotāja parakstu, kas ir lietotāja vārds un uzvārds 

Kad visas šīs izmaiņas ir veiktas ir iespējams palaist programmu.

## Programmas lietošanas piemērs

Programmu palaiž startējot **main.py** failu. Ja programmu tiek palaista pirmo reizi, tad ir iespējams tikai lejupielādēt nolikumus.

![ ](assets/images/image1.jpg)

Veicot nolikumu lejupielādi, visas pogas kļūs neaktīvas un būs nepieciešams gaidīt kamēr lejupielādējas nolikumi.

> [!NOTE]
> Nolikumu lejupielāde aizņem ~2-3 minūtes.

![ ](assets/images/image2.jpg)

Lejupielādējot nolikumus ir iespēja aplūkot turnīrus vai pieteikties kādam noteiktam turnīram. Kā arī var redzēt pēdējo laiku, kad tika lejupielādēti nolikumi.

![ ](assets/images/image3.jpg)

Aplūkojot turnīrus var tabulas veidā redzēt pieejamos turnīrus, to norises datumu, e-pasts uz kuru jāpiesakās un turnīra tipu. Ja e-pasts un/vai turnīra tips ir "Unknown", tad nebija iespējams viennozīmīgi iegūt nepieciešamo informāciju.

![ ](assets/images/image4.jpg)

Izvēloties turnīru tiek parādīti visi iespējamie turnīri, kuriem var pieteikties. Ja netiek izvēlēts neviens turnīrs, nav iespējams turpināt.

![ ](assets/images/image5.jpg)

Izvēloties kādu turnīru ir iespējams turpināt pieteikšanos.

![ ](assets/images/image6.jpg)

Sekmīga turnīra datu nolasīšanas procesā, ir iespēja apstiprināt pieteikumu, ievadot teksta lodziņā e-pastu uz kuru jāsūta pieteikums. Šāda opcija eksistē, ja gadījumā tiek nolasīts nepareizais e-pasts. Ir iespējams to izmainīt.

![ ](assets/images/image7.jpg)

Teksta lauciņā ievadīt nepieciešamo informāciju un apstiprinot e-pastu varēs nosūtīt pieteikumu.

![ ](assets/images/image8.jpg)

Apstiprinot e-pastu ir iespējams nosūtīt e-pastu.

> [!CAUTION]
> Nosūtot e-pastu, to nevarēs apturēt un tiks nosūtīts ziņojums uz pēdējo apstiprināto e-pastu.

![ ](assets/images/image9.jpg)

Nosūtot ziņojumu, pieteikums ir nosūtīts un vairs nekādas funkcijas nav iespējams veikt.

![ ](assets/images/image10.jpg)

Taču var gadīties, ka izvēloties turnīru, kam piesakās, nevar e-pastu nosūtīt. Šajā gadījumā e-pasts un/vai turnīra tips ir "Unknown". Ja e-pasts ir vienāds ar šādu vērtību, tad nolikumā vai nu nav norādīts e-pasts (pieteikšanās ar kādu linku), vai pieteikuma e-pasts neatbilst standarta norādītajām vērtībām.
Ja turnīra tips nav zināms, tad nolikums nav nepieciešamie atslēgas vārdi, lai viennozīmīgi noteiktu tā tipu. Šādos gadījumos ir ieteicams izlasīt nolikumu un pieteikties manuāli.

![ ](assets/images/image11.jpg)

## Automatizēšanas procesa automatizācija

Var ievērot, ka programma tiek palaista no kādas izstrādātājvides, piemēram, VS Code. Lai katru reizi nevērtu vaļā attiecīgo izstrādātājvidi, lai palaistu programmu, ir iespējams izveidot Windows pakešfailu (angļu - *Batch file*) ar paplašinājumu ".bat", kas automātiski, palaidīs programmu.

```
@echo off

cd "C:\Users\<path to chessLV>\chessLV"

start main.py

Exit
```

Otrajā rindā ir nepieciešams nomainīt uz ceļu, kur atrodas lokālā projekta kopija. Failu var saglabāt uz sākuma ekrāna, tādā gadījumā programmu var palaist ar 1 klikšķi.

> [!NOTE]
> Tieši šāds pakešfaila kods ir uz Windows. Līdzīgu kodus var izveidot arī uz citām operētājsistēmām.
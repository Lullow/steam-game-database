# HEMTENTAN

## LÄS DETTA FÖRST

**DENNA TENTA ÄR INDIVIDUELL - Att kopiera, diskutera eller dela sin lösning behandlas som fusk och kan leda till avstängning. Att spela in sin intervju och sedermera dela den leder till omedelbar avstängning.**

**Deadline**: 60 minuter innan din individuella tid du tilldelats ska din kod vara pushad till github
Kompletteringar annonseras i efterhand.

# Beskrivning:

Likt tidigare labbar har du fått en specifikation med kod. Du ska färdigställa metoderna utifrån valfri ordning, så gott du kan. Datan är verklig och är tagen från en världens största digitala affär och plattform för tv-spel (Steam store), men nedklippt för att inte ta för mycket utrymme, vilket gör att alla spel ej finns med. Du ska skapa en enklare applikation som låter en användare begära ut information, där utgångspunkten är att vi skapar programmet med hjälp av en återanvändbar klass, samt vissa externa paket. 
På VG-nivå kommer du dessutom förväntas strukturera om denna klass "VideoGameDatabase", och utnyttja ytterligare en klass som heter "VideoGame".
Jag vill att du förstår en sak: Ditt program är primärt i main.py. game_utils.py är inte kärnan i ditt program, VideoGameDatabase är bara en återanvändbar klass som lika gärna kunnat komma från ett pip-paket - så ska du tänka. 
Du ska bygga ett program som av "slump" råkar utnyttja denna återanvändbara klass. 

Denna uppgift tränar dig på följande koncept:
- (G) standard OOP
- (G) Separation of concerns
- (G) Reusability
- (G) Encapsulation (protected methods)
- (VG) Cohesion, dvs. idén om att klasser kan höra ihop
- (VG) Refactoring, dvs. att strukturera om kod
- (VG) Entity-pattern, dvs. idén om att vissa klasser representerar data

Du ska använda 2-3 klasser som på ett logiskt sätt ska samspela. Din databas-klass kommer stå för vissa mer generella operationer, medan din Menu-klass ska implementera presentationslogiken (input, print, menyn som ger användaren val) och det mer specifika kopplat till just denna applikation. Båda klasserna ska använda sig av errorhantering, men det är primärt din Menu-klass som faktiskt ska reagera och agera på errors för att utföra handlingar. I praktiken hade vi faktiskt kunnat skippa att utnyttja Menu och bara använt funktioner och globala variabler - men nu försöker vi nyttja mer OOP.

Du kommer sedan få en tid där du ska intervjuas om koden du skrivit.

- Försök först förstå helheten genom att läsa beskrivningarna för klasserna, följt av deras enskilda metoder.
- Databas-klassen kommer ofta använda sig av "raise"-keywordet när du gör try-except, du hanterar sedan detta i din Menu-klass
- Det är strikt förbjudet att överdrivet kommentera sin kod, tex. med kommentarer som förklarar enskilda koncept eller överdrivet beskriver enskilda rader kod.
- Förstå att du är väldigt fri att utnyttja externa paket, tex. pandas, eller göra andra ändringar på specifikationen - du ska dock inte överdrivet ändra uppgiften, tex. i denna uppgift så föredrar jag om ni håller er hyffsat till formatet, jag har inte riktigt möjligheten att spendera 5-10min för att sätta mig in i er kodbas.
- Det är mycket möjligt att datan i sig kan ha problem på olika ställen
- Ni ska sträva efter att färdigställa alla metoder, men du kan fortfarande bli godkänd om du inte hinner färdigt. Det är bättre att du struntar i att implementera en metod om du ej förstår den (tex. om du väljer att AI-generera --> don't!)


**Betyg**: U, G, VG

**G**
- För att få **G** så ska du visa god förståelse för koden du skrivit, ha implementerat de flesta metoderna, och kunna svara på diverse frågor om grundläggande python. Det är möjligt att bli godkänd utan att ha implementerat samtliga metoder - du ska försöka göra så många du hinner/klarar av, helt enkelt.
- Du behöver inte utnyttja VideoGame-klassen, du kan plocka bort den helt om du ej satsar på VG, och alla metoder som innehåller "VG" i docstringen. Däremot måste du utnyttja VideoGameDatabase-klassen.
- Du förväntas ändra docstrings så att dom passar din implementation. Det är OK att göra modifikationer till parametrar, så länge du inte överdrivet ändrar strukturen. 
- Du ska errorhantera med god förståelse
- Du ska utnyttja custom errors / exceptions flitigt när det är rimligt
- Du ska visa på förståelse av vad som gör att en klass blir återanvändbar, och kunna särskilja på vad som inte är återanvändbart

**VG**
- Alla ovanstående punkter för G
- För att få **VG** bör du ha gjort klart de flesta metoderna. Du ska dessutom kunna visa på djupare förståelse för python, i synnerhet objektorienterad programmering, och kunna svara mer detaljerat på de frågor jag ställer. Du ska visa på problemlösningsförmåga vid eventuella uppdagade fel / buggar, dvs. felsökning och påvisa tydlig teknisk känsla.
- KRITISKT: Du ska strukturera om VideoGameDatabase och utnyttja VideoGame-klassen, som ett sätt att representera datan, där det är rimligt. Du behöver fundera på frågan: Hur kan jag strukturera om parametrarna, så att klassen utnyttjar instanser av VideoGame istället? 
- Du ska visa på problemlösande kreativitet genom att utnyttja externa paket, såsom pandas, pillow, matplotlib, requests, etc. när det kan vara lämpligt. Övertänk inte detta, skulle det visa sig att du endast utnyttjar pillow och requests är det helt OK.
- Du ska lägga till 2-3 valfria extra-metoder i VideoGameDatabase 

## Inlämning

- Pusha till github senast 60 minuter innan din utsatta tid
- Ta bort alla onödiga filer, filen som redovisas ska heta main.py och din kod bör vara på den huvudsakliga branchen "main" eller "master".
- Se till att du körde git clone på din EGEN repository för hemtentan.
- Feedback ges muntligt och inte skriftligt


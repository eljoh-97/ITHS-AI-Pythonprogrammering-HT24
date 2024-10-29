# Det egna projektet, steg 1

## Kunna göra förutsägelse av kunders köpbeslut och identifiera vilka nyckelfaktorerna är.

* Problem: Jag vill kunna förstå vad som påverkar kunders beslut att genomföra ett köp eller inte, i B2B-buisness där försäljningscykeln kan vara lång och ibland lite komplex för att förstå anledningarna. Bla. vilka är nyckelfaktorerna som driver kunder till ett köp etc.? Detta kommer att hjälpa företagen på sikt att kunna skapa bättre förståelse och ge rätt insikter kring hur man ska agera i form av försäljningsstratergier, prisättning av produkter samt vilken typ av marknadsföring man ev. ska fokusera på. Problemet är ett regressionsproblem, och min intiala tanke är att använda algoritmer som decision tree, random forest eller gradient boosting för att kunna bygga en modell som kan förutsäga sannolikheterna för ett köp av en kund. Ett mer komplexare alternativ hade såklart varit att använda sig av neural network eller en deep learning modell. 



## Datasetet
* Datan som ska användas är "syntetisk" genererad data via Python ramverket "Faker", jag har försökt att skapa realistisk data utifrån ett B2B perspektiv, med 4st olika dataset som jag i slutet mergea ihop till ett komplett dataset. Datasetet i säg är inte 100% komplett ännu, det beror på att datasetet saknar en target. Min tanke är att utöka detta med att skapa en target baserad på "offerClosed". Dock har jag inte bestämt om jag ska simplifierar värdet till "Binary Classification" eller tillämpa "Multi-Class Classification". 
* Null-värde har hanterats och ersatts av "0".
* Jag inte undersökt ännu om jag har några exterma värden men baserat på datasetet beskrivning så ser jag inga avvikelser ännu.
* Datatyper i datasetet: object, float64, int64 och int64
* Min tanke är att använda samtliga upp-mappade fält för att kunna identifera och förutsäga kunders köpbeslut och dess nyckelfaktorer. Ev. så kan jag behöva modifiera datan ytterliggare med nya features för att kunna få en bra output.
* Min tanke är att omvandla string values (object features) till numeriska värden med hjälp av antingen One-Hot Encoding, Label Encoding eller Hash Encoding. 

### Generell info kring datasetet
* Antal rader: 1000 (genererad data: 1000 kunder, 3000 kontakter, 12500 interactions, 9500 offerter)
* Antal kolumner: 13
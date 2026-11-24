# Exercici 4: seed, repetir l'aleatorietat

**Objectiu:** descobrir que l'«aleatorietat» del model es pot controlar i reproduir.

**Predicció (abans de començar):** si repetiu el mateix prompt amb la mateixa llavor, creieu que sortirà exactament la mateixa resposta?

**La vostra predicció:** Crec que si utilitzem el mateix prompt, la mateixa temperatura i la mateixa llavor, el model donarà la mateixa resposta. Pero si cambiem la llavor segurament seràn diferents

1. **Actualitzeu `lab.py`:** afegiu l'opció `--seed` (per exemple, `--seed 42`), que va dins d'`options` i només s'ha d'enviar si s'indica.
   - Per demanar-ho al model, feu `/bye`, torneu a executar `ollama run gemma3:4b` i enganxeu-hi el vostre `lab.py` escrivint abans «Tinc aquest script de Python, `lab.py`:». Demaneu-li només el canvi nou i que us torni el codi complet. Feu el mateix als exercicis següents.
   - **Comproveu** que l'script imprimeix la llavor entre les opcions i que tot el que ja funcionava continua funcionant: el model pot esborrar codi anterior.
2. Deseu aquest prompt en una variable de PowerShell i executeu-lo **3 vegades** amb temperatura alta i **sense** llavor (aleatòria). Anoteu els noms a la taula:

   ```powershell
   $prompt = "Inventa el nom d'un mòdul optatiu absurd d'un cicle formatiu de grau superior d'informàtica. Respon només amb el nom."
   python lab.py $prompt --vegades 3 --temperature 1.5
   ```

3. Repetiu-ho **amb** la llavor 42 i anoteu els noms a la taula. El número concret de la llavor no importa; el que compta és que sigui el mateix per repetir la resposta i diferent per canviar-la.

   ```powershell
   python lab.py $prompt --vegades 3 --temperature 1.5 --seed 42
   ```

   Si la primera resposta és diferent de les altres dues, repetiu la prova: a vegades la primera resposta d'una sèrie varia lleugerament (és un efecte numèric normal).

| Llavor (seed) | Nom 1 | Nom 2 | Nom 3 | Són iguals? |
| :- | :- | :- | :- | :- |
| Cap (aleatòria) | Simbiosi Quantum de Peluquers | Simbiosi Algorítmica de les Cistel·les | Neuro-Simulació d'Escarabots | No|
| 42 | Bio-algoritmes de Carxofes | Bio-algoritmes de Carxofes | Bio-algoritmes de Carxofes | Sí |

## Preguntes

1. Quan la llavor és la mateixa, els tres noms són iguals o diferents? Proveu ara una altra llavor (per exemple, `--seed 43`): surt el mateix nom?

   **Resposta:** Quan utilitzo la llavor 42, les tres respostes són iguals: "Bio-algoritmes de Carxofes". Quan canvio la llavor a 43, em dona un nom diferent: "Sintaxi de Nebulació Quàntica", que també esrepeteix les tres vegades.

2. Penseu en una situació en què voldríeu obtenir exactament la mateixa resposta dues vegades (per exemple, per trobar un error en un programa). Quina?

   **Resposta:** Utilitzaria la mateixa llavor per fer proves en una aplicació que utilitza IA. Així podria repetir les mateixes respostes i detectar errors més fàcilment, sense que l'aleatorietat del model afectés les proves.

3. Compareu els vostres noms amb els d'una altra persona de la classe que hagi fet servir la mateixa llavor. Són iguals? Per què creieu que pot passar?

   **Resposta:** He comparat amb la Isha y hem obtingut les mateixes respostes. Això passa perquè hem utilitzat el mateix model, el mateix prompt, la mateixa temperatura i la mateixa llavor. O sigui que com que d'lguna manera podem controlar l'aletorietat


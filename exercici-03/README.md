# Exercici 3: la temperatura depèn de la tasca

**Objectiu:** comprovar que no hi ha una temperatura «millor»: una tasca de precisió i una de creativitat necessiten valors diferents. També veureu que una temperatura baixa fa el model més consistent, però no el fa encertar més: si no sap fer una tasca, s'equivoca igualment.

**Predicció (abans de començar):** amb quina temperatura creieu que el model encertarà més una multiplicació? I amb quina proposarà noms més variats?

**La vostra predicció:** Crec que la multiplicacií l'encertarà millor amb la temperatura 0, y amb la tempeatura 1.5 proposara més varietats.

**Script:** aquest exercici no necessita cap paràmetre nou: feu servir `lab.py` tal com el teniu.

1. Deseu els dos prompts en variables de PowerShell. El prompt A mesura la precisió (la resposta correcta és 337491) i el B, la creativitat:

   ```powershell
   $promptA = "Quant fa 487 × 693? Respon només amb el número."
   $promptB = "Dona'm 5 noms originals per a una cafeteria d'informàtics. Respon només amb els noms."
   ```

2. Executeu cada prompt **3 vegades** amb temperatura 0 i **3 vegades** amb temperatura 1.5, i completeu la taula:

   ```powershell
   python lab.py $promptA --vegades 3 --temperature 0
   python lab.py $promptA --vegades 3 --temperature 1.5
   python lab.py $promptB --vegades 3 --temperature 0
   python lab.py $promptB --vegades 3 --temperature 1.5
   ```

| Prompt | Temperatura 0 | Temperatura 1.5 |
| :- | :- | :- |
| A: 487 × 693 (quantes vegades ha encertat?) | 0 de 3. Sempre respon 337821. | 0 de 3. Respon 337851, 337821 i 337851. |
| B: noms de cafeteria (hi ha varietat? són repetits?) |Poca varietat, molts noms es repeteixen.|Més varietat, encara que alguns noms es repeteixen. |

## Preguntes

1. Amb quina temperatura funciona millor cada tasca? Per què?

   **Resposta:** En la multiplicació, cap de les dues temperatures ha funcionat bé, perquè el model no ha encertat cap resposta. Amb temperatura 0 sempre dona el mateix resultat incorrecte, mentre que amb temperatura 1.5 varia una mica.

   Per generar noms de cafeteries funciona millor la temperatura 1.5, perquè dona noms més variats i originals, com Logic Latte o Hex & Honey.

2. Quina temperatura triaríeu per a un assistent de codi? I per un generador de noms de projectes o de startups tecnològiques?
per a un generador d'idees per a un eslògan?

   **Resposta:** Per a un assistent de codi triaria una temperatura baixa, perquè necessito respostes més consistents. Per generar noms de projectes, startups o eslògans, triaria una temperatura de més d'1, perquè es necessita més creativitat i varietat.


3. Amb temperatura 0, el model ha donat sempre la mateixa resposta al prompt A? Era correcta? Que una resposta sigui consistent vol dir que sigui correcta? Com resoldríeu aquest problema en una aplicació real?

   **Resposta:** Sí, les tres vegades ha donat el mateix resultat, 337821, però és incorrecte. Que una resposta sigui consistent no vol dir que sigui correcta. En una aplicació real faria servir una calculadora o una funció de Python per fer les operacions matemàtiques, en lloc de confiar en els càlculs del model.


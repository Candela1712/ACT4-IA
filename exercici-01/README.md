# Exercici 1: la temperatura

**Objectiu:** veure que amb temperatura 0 el model és previsible (però no per això encerta), que a mesura que puja les respostes es fan més variades i que la temperatura no canvia res quan la pregunta només té una resposta correcta.

**Predicció (abans de començar):** què creieu que passarà amb les respostes quan pugeu la temperatura?

**La vostra predicció:** Crec que amb una temperatura baixa el model donarà respostes iguals o molt semblants. Quan augmentem la temperatura, les respostes seran més variades i creatives, però també pot cometre més errors.

## Primera prova: una paraula

1. Inicieu el model i fixeu la temperatura a 0:

   ```
   ollama run gemma3:4b
   >>> /set parameter temperature 0
   ```

2. Escriviu aquest prompt, llegiu la resposta, anoteu-la a la **taula 1** i feu `/clear`. Repetiu-ho fins a tenir **3 respostes** (una a cada columna):

   ```
   Digues una paraula en català de més de 10 lletres. Respon només amb la paraula.
   ```

3. Repetiu el pas 2 amb `/set parameter temperature 0.8` i, després, amb `/set parameter temperature 1.5`. Cada temperatura és una fila de la taula.

**Taula 1: la paraula**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 | Estratègia | Estratègia | Estratègia |
| 0.8 | Excepcionalitat | Eteropeix | Estratègia |
| 1.5 | Estratègia | Excepcionalitat | Il·lustració |

## Segona prova: una pregunta amb una sola resposta

4. Feu el mateix que a la primera prova (3 respostes per temperatura, amb `/clear` entre cadascuna), però només amb les temperatures 0 i 1.5 i amb aquest altre prompt. Comenceu per la temperatura 0: torneu-la a fixar amb `/set parameter temperature 0`, perquè ara la teniu a 1.5. Anoteu les respostes a la **taula 2**, encara que sembli que sempre sortirà el mateix: és justament el que voleu comprovar:

   ```
   Quina és la capital de França? Respon només amb el nom.
   ```

**Taula 2: la capital de França**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 | París | París | París |
| 1.5 | París | París | París |

## Preguntes

1. Mireu la taula 1. Les tres respostes amb temperatura 0 són iguals? Per què? Compteu les lletres de la paraula: en té més de 10? Que sempre surti la mateixa paraula vol dir que sigui correcta?

   **Resposta:** Amb temperatura 0, el model sempre selecciona el token més probable. Per això les respostes solen ser iguals. Però tampoc vol dir que la resposta sigui correcta, perquè el model també es pot equivocar i repetir el mateix error.

2. Què passa quan pugeu la temperatura? Surten paraules diferents? N'hi ha alguna que no tingui més de 10 lletres o que no sembli una paraula real?

   **Resposta:** Quan augmentem la temperatura, el model té més possibilitats de donar respostes diferents. Això fa que sigui més creatiu, però també pot generar paraules incorrectes o que no compleixi o respongui el que es demana exactament

3. Mireu la taula 2. Les respostes sobre la capital canvien tant com les de la paraula quan puja la temperatura? Per què creieu que la temperatura hi té tan poc efecte? (Pista: quantes respostes correctes té cada pregunta? La temperatura només dona varietat quan el model dubta entre diverses opcions.)

   **Resposta:** No haurien de canviar tant, perquè França només té una capital correcta. En canvi, hi ha moltes paraules en català de més de 10 lletres. O sigui, que la temperatura té menys efecte quan hi ha una resposta molt més probable que les altres.

4. Amb les vostres paraules: què fa el paràmetre `temperature`?

   **Resposta:** La temperatura controla l'aleatorietat de les respostes del model. Una temperatura baixa fa que les respostes siguin més previsibles i una temperatura alta fa que siguin més variades, però a la vegada poden ser menys precises.


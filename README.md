# platzi_regex
***
## Expresiones Regulares

Son una herramienta muy potente a la hora de procesamiento de cadenas de texto. Al usar las expresiones regulares creamos patrones en donde derminados grupos de caracteres hacen o no coincidencia para un posterior uso de ellos.

https://regexr.com/

* Encontrar un número hexadecimal `[a-fA-F0-9]{3,6}`

* Los matches mas pequeños posibles para una linea como esta:
`csv1,csv2,csv3,csv4,csv5` es: `.+?,` el `?` es para que haya o no haya algo o para que las busquedas sean lo más pequeñas posibles, es decir el primer match... como en este caso.

* Para un número de telefono con formato de tres grupos de digitos `(\d{2,2}[\-\. ]{0,1}){3,3}`

* Inicio de linea `^` final de linea `$` estos dos nos encierran lo que se requiere en la expresión que contenga una linea.

* El `^` Es inicio de lines pero tambien es negación

* Encontrar sólo los WARN de un Log del servidor `^\[LOG.*\[WARN\].*$`

* URL: `https?:\/\/[\w\-\.]+\.\w{2,5}\/?\S*`

* Mail: `[\w\-\._]{5,30}\+?[\w]{0,10}@[\w\-\.]+\.\w{2,5}\/?\S*`

* Ubicaciones de tipo  `-99.205646,19.429707,2275.10` usando la expresión `^\-?\d{1,3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6},.*$`

* Ubicaciones de tipo `-99 12' 34.08"W, 19 34' 56.98"N`usando la expresión `^\-?\d{1,3}\s\d{1,2}'\s\d{1,2}\.\d{2,2}"[WE],\s?\-?\d{1,3}\s\d{1,2}'\s\d{1,2}\.\d{2,2}"[NS]$`

* Mapas con 3 palabras: https://map.what3words.com/ (Agregar a mi blog)

* Nombres en Colombia `^([A-ZÁÉÍÓÚ][a-zñáéíóúñ]{2,}\s?){2,5}$`

* Para el archivo de peliculas `^\d+::([\w\s,\(\)'\.\-&!\/\*\$\?]+:?[\w\s,\(\)'\.\-&!\/\*\$\?]+)\s?\((\d\d\d\d)\)::.*$` en donde el primer grupo se puede conservar usando `$1` y el segundo `$2` ... podemos generar sentencias **sql** haciendo por ejemplo: `insert into movies (year, title) values ($2, '$2'):`

* Para extraer variables en querys GET como esta: `https://www.google.com/search?client=ubuntu&channel=fs&q=comprar+camellos+en+espa%C3%B1a&ie=utf-8&oe=utf-8` usaremos `[\?&](\w+)=([^&\n]+)` y podemos por ejemplo remplazarlos por: `$1 = '$2'`

* La bandera que usamos para que la expresión no sea case sensitive es `/i`

***

# Glosario extra

^ — Negación de una determinada expresión

\t — Representa un tabulador.

\r — Representa el “retorno de carro” o “regreso al inicio” o sea el lugar en que la línea vuelve a iniciar.

\n — Representa la “nueva línea” el carácter por medio del cual una línea da inicio. Es necesario recordar que en Windows es necesaria una combinación de \r\n para comenzar una nueva línea, mientras que en Unix solamente se usa \n y en Mac_OS clásico se usa solamente \r.

\a — Representa una “campana” o “beep” que se produce al imprimir este carácter.

\e — Representa la tecla “Esc” o “Escape”

\f — Representa un salto de página

\v — Representa un tabulador vertical

\x — Se utiliza para representar caracteres ASCII o ANSI si conoce su código. De esta forma, si se busca el símbolo de derechos de autor y la fuente en la que se busca utiliza el conjunto de caracteres Latin-1 es posible encontrarlo utilizando “\xA9”.

\u — Se utiliza para representar caracteres Unicode si se conoce su código. “\u00A2” representa el símbolo de centavos. No todos los motores de Expresiones Regulares soportan Unicode. El .Net Framework lo hace, pero el EditPad Pro no, por ejemplo.

\d — Representa un dígito del 0 al 9.

\w — Representa cualquier carácter alfanumérico.

\s — Representa un espacio en blanco.

\D — Representa cualquier carácter que no sea un dígito del 0 al 9.

\W — Representa cualquier carácter no alfanumérico.

\S — Representa cualquier carácter que no sea un espacio en blanco.

\A — Representa el inicio de la cadena. No un carácter sino una posición.

\Z — Representa el final de la cadena. No un carácter sino una posición.

\b — Marca la posición de una palabra limitada por espacios en blanco, puntuación o el inicio/final de una cadena.

\B — Marca la posición entre dos caracteres alfanuméricos o dos no-alfanuméricos.

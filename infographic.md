## Números de Telefonos

556789

23-45-78

45.77.65

36.54-87

34 76 09

36y75d65

**Extra**

65-35-66#124

334544p123

545543e123

+521565811

`(...\-...\-....)`

`(\d\d\d\-\d\d\d\-\d\d\d\d)`

`(\d{3,4}[\-\s])`

***
Para un número de telefono con formato de tres grupos de digitos

* `(\d{2,2}[\-\. ]{0,1}){3,3}`

* `\d{2,2}\D?\d{2,2}\D?\d{2,2}`

* `(\d{2,2}\D?){2,2}\d{2,2}`

* `(\d{2,2}\W?){2,2}\d{2,2}`

***
Para acertar a todos los ejemplos

* `^\+?\d{2,3}[^\da-z]?\d{2,3}[^\da-z]?\d{2,3}[#pe]?\d*$` ✔️
* `^\+?(\d{2,3}[^\da-z]?){2,2}\d{2,3}[#pe]?\d*$`

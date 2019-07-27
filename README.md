# Ciudades
Sitio web con Django


Ejercicio: Realizar una aplicación en Python que reciba el número de una
columna y diga cuál es su conversión en letras. De la misma manera que lo
hace Excel, PERO adicionando la letra “Ñ”

Realizar una aplicación web responsive en el framework Django que
permita registrar regiones y municipios, la aplicación debe contar con las
siguientes características:
• Cada municipio permite guardar los siguientes campos:
o Código numérico único
o Texto como nombre del municipio
o Estado que puede ser Activo o Inactivo
o Ejemplo de un municipio (código: 5005, nombre: “Santa
rosa”, estado: Inactivo)
• Cada región permite guardar los siguientes campos:
o Código numérico único
o Texto como nombre de la región
o Ejemplo de una región (código: 7, nombre: “Vallede
aburra”)
 Una región contiene municipios y puede tener ninguno o varios
municipios asociados
 Se debe poder listar, editar y eliminar los municipios
 Se debe poder listar, editar y eliminar las regiones. Al editar una región
se debe poder agregar o quitar municipios.
 Un municipio puede estar en diferentes regiones, por ejemplo el municipio
“Medellín” puede estar en una región “Andina”, también en una región
“Valle de aburra”, otra “Latina”, “Paisa”, etc.
 Los municipios que tienen las regiones solo puede ser municipios con
estados activos, si al editar un municipio se pone a estado “Inactivo”, este
municipio ya no pertenece a la región (Es decir que la asociación
desaparece).

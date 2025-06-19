# Aplicaciones para MDS

En [este repositorio](https://github.com/rmartinsanta/docencia-mds/) iremos publicando el código fuente de las aplicaciones y retos desarrolladas para las prácticas de Metodologías de Desarrollo Seguro.
Se irá ampliando de forma progresiva cada año, tras finalizar las correspondientes convocatorias.
Existen dos tipos de problemas diferentes, en función de la plataforma para la que están preparados: DomJudge y CTFd.

## Retos Domjudge
Se trata de retos que pueden ser importados en DomJudge, utilizando por ejemplo [domjudge-automation](https://github.com/rmartinsanta/domjudge-automation) para desplegarlo.
Para subir un reto, es necesario crear un fichero comprimido ZIP en el que los ficheros `domjudge-problem.ini` y `problem.yaml` se encuentren en la raíz.
Cada reto puede resolverse en cualquiera de los lenguajes de programación soportados por Domjudge, en la asignatura utilizamos Java y Python.

## Retos CTFd
Retos para importar en la plataforma [CTFd](https://github.com/CTFd/CTFd), también de código abierto. Cada ejercicio es una aplicación independiente, que puede ejecutarse en local o desplegarse en un servidor remoto. Resumen:

- 10fastfingers: escribe las palabras solicitadas en el menor tiempo posible, sin superar el máximo tiempo configurado. ¿Serás lo suficientemente rápido?
- Whack-a-mole: juego de los topos, el usuario tiene que lograr llegar a la puntuación objetivo. ¿Habrá alguna forma de no tener que estar cazando topos durante semanas?
- Agenda C: App de terminal para almacenar contactos escrita en C, ¿usará la memoria de forma razonable? Empaquetada como un contenedor Docker para facilitar su gestión y despliegue.
- Blog: Página con cientos de páginas de información, ¿podrás encontrar la información relevante? Empaquetada como un contenedor Docker para facilitar su gestión y despliegue.

En general, para las asignaturas que quieran utilizar los retos, se recomienda hostear una copia de los mismos con la flag real en un servidor controlado por el docente, y dar una copia del código fuente de los retos al estudiante con una flag con el valor por defecto.

## Autores
- Isaac Lozano Osorio
- Raúl Martín Santamaría

## Licencia
MIT, ver [license](LICENSE) para más detalle.

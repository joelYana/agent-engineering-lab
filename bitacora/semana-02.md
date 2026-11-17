# Semana 2 (2 nov - 16 nov)

## Qué hice

- Llevé las clases 1, 2 y 3 de condicionales, bucles y excepciones.
- Implementé la Calculadora v2 con validaciones, bucles y excepciones.
- Problem Set 1 con los 3 ejercicios de bank, interpreter y meal.
- Problem Set 2 con los 3 ejercicios de camel, coke y plates.
- Tests actualizados, ahora son 32, entre 23 de la calculadora y 9 del interpreter.
- Ejercicio de math interpreter rehecho para rechazar entradas inválidas sin caerse.
- Revisión de documentación de pytest raises.

## Horas (tiempo transcurrido desde que abro el día hasta que lo cierro)


| Día | Cerrado el | Tiempo |
|-----|------------|--------|
| D8  | 3 nov      | 27h    | 
| D9  | 5 nov      | 43h    | 
| D10 | 6 nov      | 13h    | 
| D11 | 10 nov     | 22h    |
| D12 | 16 nov     | 128h   | 
| D13 | 17 nov     | 14h    | 

Días en cero: 7 (6–8 nov y 11–14 nov). Con aviso: 0.

## Qué funcionó

- Predicciones antes de las ejecuciones, especificar antes de programar las nuevas versiones y los tests.

- El test de 20 que atrapó el `< 20` en `test_calculadora_sisop.py`. Si no existiera ese test de probar con un valor límite que es 20, ignoraría este error y estaría mal la implementación.

- `5 ^ 2` en `interpreter.py`, el `else` contenía este tipo de operaciones y lo calculaba como división, por lo que ajusté un `elif` y dejé en `else` ese caso. Es un error silencioso, que daba un resultado falso sin avisar, y eso es peor que un error que detiene el programa.

- El uso de una bandera, la cual fue `hay_numero` en `plates.py`, permitía que, al identificar un número, se activara la bandera para luego validar si se encontraba una letra, pero ya estaba activada la bandera y rechazaba.

- Distinguir entre las funciones de `valida_texto` y `pide_nota`. `valida_texto` se puede probar porque no depende del teclado; con la misma entrada da el mismo resultado.

## Qué falló o me costó

- Incumplí dos plazos: el domingo 8 y el jueves 12 de noviembre.

- Cuando algo de la universidad salía mal, me desconectaba del plan sin avisar.

- No terminaba los días el mismo día que los empezaba, como es esperable. La mayoría los acababa al día siguiente, por temas de cansancio al llegar de la U tarde.

- Se tenía planeado acabar la semana en una semana calendario y me tomó dos semanas en total, mejor que la primera semana, pero ese no era el punto de comparación, es ser disciplinados con el plan.

- Entre el 6 y el 8 fueron días en 0, mayormente por mi preparación para mi PC de Gobierno, el sábado salí y el domingo tuve que avanzar tesis.

- Entre el 11 y el 14, tuve que prepararme para mi lab de Sistemas de Información, pero eso fue solo dos días, los demás fueron falta de ganas y confianza, ya que me fue mal y estuve desganado. Me faltó avisar, aunque sinceramente no es excusa, ningún día en 0 sin aviso es la clave.

- En cuanto a lo técnico, programar la regla de las minúsculas en camelCase, el `True` que devolvía `valida_texto` o mi mala costumbre de usar paréntesis al usar `if`.

## Pausa

- 6–8 nov: preparación para mi PC de Gobierno, salida el sábado y tesis el domingo sin aviso.

- 11–14 nov: preparación de lab de Sistemas de Información, falta de confianza y 0 ganas de continuar sin aviso.

## Siguiente paso

Empezar la semana 3 el día 17 de noviembre

## Pendientes

Hablar con mi papá a más tardar el jueves 19: cuándo empiezo con los casos golden, cuántas horas les dedico y validar los acuerdos.

## Reflexión

Mi primer objetivo con esta semana 2 era hacerla en menos tiempo que la semana 1. Era un objetivo interno no escrito y lo cumplí. Por ese lado, es un pequeño logro para mí, pero en cuanto a lo escrito, no cumplí con lo pactado y tardé una semana de más. La desconfianza y el desgano que me producía la U es un tema que tengo que trabajar porque se viene la parte más pesada, por lo que puedo fallar un día pero no desaparecer. Recordar siempre los acuerdos que planteo y mantener siempre contacto con Claude sobre mis avances es mi prioridad, ya que, siendo totalmente honesto, quizás si hubiera empezado desde el día que me entregaron el documento, a día de hoy lo tendría acabado. Esa es mi mayor motivación para no perder más días y cumplir, porque se vienen bastantes cosas y la disciplina no es negociable.

## Acuerdos

Los de la semana 1:

- Ningún día en cero sin aviso; mínimo 30 minutos diarios: no cumplido. Evidencia: 7 días en cero, 0 con aviso.

- El día antes del laboratorio es descanso planificado y lo compenso el fin de semana: no aplicó. Evidencia: no hubo laboratorios de SISOP en estas dos semanas.

- Preguntarle esta semana a mi papá cuándo empiezo con los casos golden y cuántas horas semanales les dedico: no cumplido, aún no conversé con mi papá.

### Nuevos acuerdos

- **Comunicación:** Avisar a Claude antes de las 9:00 p. m. si no puedo cumplir con el día por motivos universitarios u otros imprevistos, y recuperar el avance al día siguiente.

- **Constancia:** Mantener un mínimo de 30 minutos diarios de trabajo, incluso durante la semana de finales.

- **Descansos planificados:** El día previo a cualquier evaluación (práctica, laboratorio o examen) será de descanso, sin obligación de cumplir el mínimo diario.

- **Fecha límite:** Cerrar la semana 3 como máximo el lunes 23 de noviembre.
# Lewis et al. (2020) — Retrieval-Augmented Generation

## Fuente
Patrick Lewis, Ethan Perez, et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, NeurIPS 2020.  
https://arxiv.org/abs/2005.11401

## Resumen
Los modelos actuales que solo cuentan con memoria paramétrica no pueden actualizarse, no muestran la procedencia de sus fuentes y recaen en alucinaciones. Frente a esto, se plantea una relación con la memoria no paramétrica, en la cual un componente llamado recuperador buscará fragmentos relevantes en un índice de documentos, y luego un segundo componente llamado generador redactará la respuesta con la pregunta y los fragmentos seleccionados. Con esto se producen respuestas con el modelo RAG más fácticas, específicas y diversas.

## Evidencia
Se probaron en 4 tareas: respuestas a preguntas de dominio abierto, abstractivas, Jeopardy y verificación de hechos. Se compararon frente a los dos baselines: BART y las arquitecturas que recuperan un fragmento y extraen la respuesta de él. Con esto, el resultado que se obtuvo fue que RAG superó el estado del arte en las tres tareas de preguntas de dominio abierto, y en generación produjo texto más fáctico, específico y diverso que BART.

## Limitaciones
Como primera limitación propia, es que la información almacenada en memoria podía ser vulnerada al contener documentos importantes confidenciales, y otra propuesta por el paper, que si los datos estaban erróneos, el modelo los presentaba como correctos con plena seguridad y no había manera de distinguirlos.

## Aplicación al proyecto
En nuestro agente vertical, los documentos serían la información oficial de admisión (requisitos, fechas, costos, carreras). El agente puede citar la fuente de cada respuesta y se va actualizando conforme cambien los documentos, y no se reentrenará.

## Decisión
Se probará, se tomará a RAG como la base del agente de admisión del capstone y se implementará en la fase de LangGraph con pgvector.
import streamlit as st

st.set_page_config(
    page_title="Glosario de IA",
    page_icon="",
    layout="wide"
)

st.sidebar.title("Información del Trabajo")
st.sidebar.info(
    """
    **Materia:** Fundamentos de Inteligencia Artificial  
    **Actividad:** Subproducto No. 4 - Glosario  
    """
)

st.image(
    "https://s03.s3c.es/imag/_v0/1200x655/4/3/0/IA.jpg",
    use_container_width=True
)

st.title("Glosario de Inteligencia Artificial")
st.write("Explora los conceptos clave de la Inteligencia Artificial. Haz clic sobre cualquier término para ver su definición o utiliza el buscador para filtrar la lista.")

glosario = {
    "1. Agentes de IA": "Una aplicación que logra un objetivo a través del procesamiento de entradas, realización de razonamientos con herramientas disponibles y toma de medidas según sus decisiones. Consiste en orquestación, perfil, memoria, razonamiento, modelo y herramientas.",
    "2. Ventana de contexto": "La cantidad de tokens que un modelo de base puede procesar en una instrucción determinada. Una ventana más grande permite procesar más información para generar respuestas más coherentes y completas.",
    "3. Incorporación (Embedding)": "Representación numérica de datos (texto, imágenes o video) mediante vectores que capturan las relaciones y significados semánticos entre diferentes entradas, reduciendo la dimensionalidad.",
    "4. Modelo de base": "Modelos grandes y potentes entrenados con grandes cantidades de datos (texto, imágenes, video, audio) que usan modelado estadístico para predecir respuestas y generar contenido nuevo.",
    "5. Llamadas a función": "Función que conecta los modelos de lenguaje grandes (LLM) a herramientas externas, como APIs y bases de datos, para responder con información y servicios en tiempo real.",
    "6. Tokenización (Asignación de tokens)": "Proceso automatizado mediante el cual los analizadores dividen el texto, términos complejos o entradas multimodales en unidades con significado semántico llamadas tokens.",
    "7. Fundamentación (Grounding)": "Proceso de conectar el resultado de un modelo a fuentes de información verificables para mejorar la exactitud de los resultados y reducir las alucinaciones.",
    "8. Modelo de Lenguaje Grande (LLM)": "Modelo de base basado en texto entrenado con grandes volúmenes de datos. Procesa el lenguaje natural imitando la forma en que se comunican los humanos.",
    "9. Latencia": "El tiempo que tarda un modelo en procesar una instrucción de entrada y generar una respuesta. Incluye el Tiempo hasta el primer token (TTFT) y el Tiempo hasta el último token (TTLT).",
    "10. Ingeniería de instrucciones (Prompt Engineering)": "Proceso iterativo de crear y perfeccionar una instrucción (prompt) para guiar la respuesta del modelo hacia resultados precisos y de alta calidad.",
    "11. Instrucción (Prompt)": "Solicitud de lenguaje natural (o imágenes, código, etc.) que se envía a un modelo de IA generativa indicándole qué tarea realizar.",
    "12. Parámetros del modelo": "Variables internas ajustables que el modelo usa para procesar entradas y generar resultados. Incluyen parámetros de instrucción como temperature, topP, topK y maxOutputTokens.",
    "13. Generación Mejorada por Recuperación (RAG)": "Técnica que combina la búsqueda de datos en fuentes externas con el modelo para responder con información actualizada, confiable y verificable.",
    "14. Tokens": "Unidad básica de datos que procesa un modelo. Las palabras, subpalabras o entradas multimodales se dividen en tokens para su análisis computacional.",
    "15. Ajuste (Tuning)": "Proceso de adaptar un modelo de base mediante el ajuste de sus parámetros con conjuntos de datos específicos para mejorar su rendimiento en tareas particulares.",
    "16. Alucinaciones": "Instancias en las que un modelo de IA generativa crea o responde con contenido inexacto o falso sin fundamentación en la realidad.",
    "17. Plugins": "Complementos que permiten a las aplicaciones de IA conectarse con otros programas, software y servicios externos para ampliar sus capacidades sin modificar el modelo base.",
    "18. Modelos multimodales": "Sistemas de IA capaces de procesar, comprender y combinar diferentes tipos de datos simultáneamente (texto, imágenes, audio, video).",
    "19. TTFT (Time To First Token)": "Métrica de latencia que mide el tiempo exacto que tarda el modelo en generar el primer token de respuesta tras recibir una instrucción.",
    "20. Vocabulario de Tokens": "El conjunto completo e integral de todos los tokens únicos que un modelo de lenguaje o modelo de base reconoce y puede procesar."
}

busqueda = st.text_input("Buscar término o palabra clave:", "")

st.markdown("---")

encontrados = 0
for concepto, definicion in glosario.items():
    if busqueda.lower() in concepto.lower() or busqueda.lower() in definicion.lower():
        with st.expander(concepto):
            st.write(definicion)
        encontrados += 1

if encontrados == 0:
    st.warning("No se encontraron conceptos relacionados con tu búsqueda.")

st.markdown("---")
st.subheader("Referencias Bibliográficas")
st.markdown(
    """
    * Google Cloud. (s. f.). *Glosario de IA generativa*. Documentación de Google Cloud. https://docs.cloud.google.com/docs/generative-ai/glossary?hl=es-419
    * Ray, S. (6 de noviembre de 2023). *10 términos de IA que todos deberían conocer*. Microsoft Source LATAM. https://news.microsoft.com/source/latam/features/ia/10-terminos-de-ia-que-todos-deberian-conocer/
    """
)

st.markdown("---")
st.caption("© 2026 Todos los derechos reservados. Desarrollado para la materia de Fundamentos de Inteligencia Artificial.")

import base64
import streamlit as st

st.set_page_config(
    page_title="Glosario e Historia de IA", page_icon="🧠", layout="wide"
)

# Estilos CSS personalizados para mejorar el diseño
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Tipografía global */
    html, body, [class*="css"], .stMarkdown, .stText {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Mejora en las imágenes */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08);
    }

    /* Estilizado de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #e9ecef;
    }

    /* Tarjeta informativa en la barra lateral */
    [data-testid="stSidebar"] [data-testid="stAlert"] {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
    }

    /* Buscador mejorado */
    .stTextInput input {
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 10px 14px;
    }

    /* Acordeones del glosario */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #1f2937;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
    }

    /* Pie de página */
    .footer-text {
        font-size: 0.85rem;
        color: #6b7280;
        text-align: center;
        padding: 20px 0;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Función para renderizar el PDF con vista previa compatible
def mostrar_pdf(nombre_archivo):
    try:
        with open(nombre_archivo, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        st.download_button(
            label="Descargar archivo PDF",
            data=base64.b64decode(base64_pdf),
            file_name=nombre_archivo,
            mime="application/pdf",
        )

        # Visor universal de PDF mediante pdf.js
        pdf_display = f"""
            <iframe 
                src="https://mozilla.github.io/pdf.js/web/viewer.html?file=data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="800px" 
                style="border: 1px solid #e5e7eb; border-radius: 10px; margin-top: 15px;"
            ></iframe>
        """
        st.components.v1.html(pdf_display, height=820)
    except FileNotFoundError:
        st.error(
            f"Asegúrate de haber subido el archivo '{nombre_archivo}' a tu repositorio de GitHub."
        )


# Navegación en la barra lateral
st.sidebar.title("Navegación")
opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "Glosario de IA",
        "Antecedentes de la IA",
        "IA débil o estrecha",
        "IA fuerte o general",
        "IA superinteligente",
    ],
)

st.sidebar.markdown("---")
st.sidebar.title("Información del Trabajo")
st.sidebar.info(
    """
    **Materia:** Fundamentos de Inteligencia Artificial  
    **Actividad:** Subproducto No. 4 - Glosario  
    """
)

# VISTA 1: GLOSARIO DE IA
if opcion == "Glosario de IA":
    st.image(
        "https://s03.s3c.es/imag/_v0/1200x655/4/3/0/IA.jpg",
        use_container_width=True,
    )

    st.title("Glosario de Inteligencia Artificial")
    st.write(
        "Explora los conceptos clave de la Inteligencia Artificial. Haz clic sobre cualquier término para ver su definición o utiliza el buscador para filtrar la lista."
    )

    glosario = {
        "1. Agentes de IA": (
            "Una aplicación que logra un objetivo a través del procesamiento"
            " de entradas, realización de razonamientos con herramientas"
            " disponibles y toma de medidas según sus decisiones. Consiste en"
            " orquestación, perfil, memoria, razonamiento, modelo y"
            " herramientas."
        ),
        "2. Ventana de contexto": (
            "La cantidad de tokens que un modelo de base puede procesar en una"
            " instrucción determinada. Una ventana más grande permite procesar"
            " más información para generar respuestas más coherentes y"
            " completas."
        ),
        "3. Incorporación (Embedding)": (
            "Representación numérica de datos (texto, imágenes o video)"
            " mediante vectores que capturan las relaciones y significados"
            " semánticos entre diferentes entradas, reduciendo la"
            " dimensionalidad."
        ),
        "4. Modelo de base": (
            "Modelos grandes y potentes entrenados con grandes cantidades de"
            " datos (texto, imágenes, video, audio) que usan modelado"
            " estadístico para predecir respuestas y generar contenido nuevo."
        ),
        "5. Llamadas a función": (
            "Función que conecta los modelos de lenguaje grandes (LLM) a"
            " herramientas externas, como APIs y bases de datos, para"
            " responder con información y servicios en tiempo real."
        ),
        "6. Tokenización (Asignación de tokens)": (
            "Proceso automatizado mediante el cual los analizadores dividen el"
            " texto, términos complejos o entradas multimodales en unidades con"
            " significado semántico llamadas tokens."
        ),
        "7. Fundamentación (Grounding)": (
            "Proceso de conectar el resultado de un modelo a fuentes de"
            " información verificables para mejorar la exactitud de los"
            " resultados y reducir las alucinaciones."
        ),
        "8. Modelo de Lenguaje Grande (LLM)": (
            "Modelo de base basado en texto entrenado con grandes volúmenes de"
            " datos. Procesa el lenguaje natural imitando la forma en que se"
            " comunican los humanos."
        ),
        "9. Latencia": (
            "El tiempo que tarda un modelo en procesar una instrucción de"
            " entrada y generar una respuesta. Incluye el Tiempo hasta el"
            " primer token (TTFT) y el Tiempo hasta el último token (TTLT)."
        ),
        "10. Ingeniería de instrucciones (Prompt Engineering)": (
            "Proceso iterativo de crear y perfeccionar una instrucción (prompt)"
            " para guiar la respuesta del modelo hacia resultados precisos y de"
            " alta calidad."
        ),
        "11. Instrucción (Prompt)": (
            "Solicitud de lenguaje natural (o imágenes, código, etc.) que se"
            " envía a un modelo de IA generativa indicándole qué tarea"
            " realizar."
        ),
        "12. Parámetros del modelo": (
            "Variables internas ajustables que el modelo usa para procesar"
            " entradas y generar resultados. Incluyen parámetros de"
            " instrucción como temperature, topP, topK y maxOutputTokens."
        ),
        "13. Generación Mejorada por Recuperación (RAG)": (
            "Técnica que combina la búsqueda de datos en fuentes externas con"
            " el modelo para responder con información actualizada, confiable"
            " y verificable."
        ),
        "14. Tokens": (
            "Unidad básica de datos que procesa un modelo. Las palabras,"
            " subpalabras o entradas multimodales se dividen en tokens para"
            " su análisis computacional."
        ),
        "15. Ajuste (Tuning)": (
            "Proceso de adaptar un modelo de base mediante el ajuste de sus"
            " parámetros con conjuntos de datos específicos para mejorar su"
            " rendimiento en tareas particulares."
        ),
        "16. Alucinaciones": (
            "Instancias en las que un modelo de IA generativa crea o responde"
            " con contenido inexacto o falso sin fundamentación en la realidad."
        ),
        "17. Plugins": (
            "Complementos que permiten a las aplicaciones de IA conectarse con"
            " otros programas, software y servicios externos para ampliar sus"
            " capacidades sin modificar el modelo base."
        ),
        "18. Modelos multimodales": (
            "Sistemas de IA capaces de procesar, comprender y combinar"
            " diferentes tipos de datos simultáneamente (texto, imágenes,"
            " audio, video)."
        ),
        "19. TTFT (Time To First Token)": (
            "Métrica de latencia que mide el tiempo exacto que tarda el modelo"
            " en generar el primer token de respuesta tras recibir una"
            " instrucción."
        ),
        "20. Vocabulario de Tokens": (
            "El conjunto completo e integral de todos los tokens únicos que un"
            " modelo de lenguaje o modelo de base reconoce y puede procesar."
        ),
    }

    busqueda = st.text_input("Buscar término o palabra clave:", "")

    st.markdown("---")

    encontrados = 0
    for concepto, definicion in glosario.items():
        if (
            busqueda.lower() in concepto.lower()
            or busqueda.lower() in definicion.lower()
        ):
            with st.expander(concepto):
                st.write(definicion)
            encontrados += 1

    if encontrados == 0:
        st.warning(
            "No se encontraron conceptos relacionados con tu búsqueda."
        )

# VISTA 2: ANTECEDENTES DE LA IA
elif opcion == "Antecedentes de la IA":
    st.title("Antecedentes de la IA")
    try:
        st.image("linea_del_tiempo.jpg", use_container_width=True)
    except Exception:
        st.error(
            "Asegúrate de subir el archivo 'linea_del_tiempo.jpg' a tu"
            " repositorio de GitHub."
        )

# VISTA 3: IA DÉBIL O ESTRECHA
elif opcion == "IA débil o estrecha":
    st.title("IA débil o estrecha")
    mostrar_pdf("ia_debil.pdf")

# VISTA 4: IA FUERTE O GENERAL
elif opcion == "IA fuerte o general":
    st.title("IA fuerte o general")
    mostrar_pdf("ia_fuerte.pdf")

# VISTA 5: IA SUPERINTELIGENTE
elif opcion == "IA superinteligente":
    st.title("IA superinteligente")
    mostrar_pdf("ia_superinteligente.pdf")

# Pie de página
st.markdown("---")
st.subheader("Referencias Bibliográficas")
st.markdown(
    """
    * Google Cloud. (s. f.). *Glosario de IA generativa*. Documentación de Google Cloud. https://docs.cloud.google.com/docs/generative-ai/glossary?hl=es-419
    * Ray, S. (6 de noviembre de 2023). *10 términos de IA que todos deberían conocer*. Microsoft Source LATAM. https://news.microsoft.com/source/latam/features/ia/10-terminos-de-ia-que-todos-deberian-conocer/
    """
)

st.markdown("---")
st.markdown(
    '<p class="footer-text">© 2026 Todos los derechos reservados. Desarrollado'
    " para la materia de Fundamentos de Inteligencia Artificial.</p>",
    unsafe_allow_html=True,
)

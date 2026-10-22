import base64
import streamlit as st

st.set_page_config(
    page_title="Glosario e Historia de IA", page_icon="🧠", layout="wide"
)

# Estilos CSS adaptados para Modo Oscuro y navegación moderna
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Tipografía global */
    html, body, [class*="css"], .stMarkdown, .stText {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Bordes y sombras adaptables para imágenes */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    /* Botones de navegación personalizados en la barra lateral */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        background-color: rgba(255, 255, 255, 0.05);
        color: inherit;
        padding: 10px 16px;
        text-align: left;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        border-color: #3b82f6;
        background-color: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
    }

    /* Tarjeta informativa lateral */
    [data-testid="stSidebar"] [data-testid="stAlert"] {
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        background-color: rgba(255, 255, 255, 0.03);
    }

    /* Pie de página */
    .footer-container {
        text-align: center;
        padding: 20px 0;
        font-size: 0.88rem;
        opacity: 0.8;
    }

    .footer-container a {
        color: #60a5fa;
        text-decoration: none;
        font-weight: 600;
    }

    .footer-container a:hover {
        text-decoration: underline;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Función para desplegar PDF en el visor Mozilla PDF.js
def mostrar_pdf(nombre_archivo):
    try:
        with open(nombre_archivo, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        st.download_button(
            label="📄 Descargar archivo PDF",
            data=base64.b64decode(base64_pdf),
            file_name=nombre_archivo,
            mime="application/pdf",
        )

        pdf_display = f"""
            <iframe 
                src="https://mozilla.github.io/pdf.js/web/viewer.html?file=data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="800px" 
                style="border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; margin-top: 15px;"
            ></iframe>
        """
        st.components.v1.html(pdf_display, height=820)
    except FileNotFoundError:
        st.error(
            f"Asegúrate de haber subido el archivo '{nombre_archivo}' a tu"
            " repositorio de GitHub."
        )


# Estado de la sesión para manejar la navegación por botones
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Glosario de IA"

# NAVEGACIÓN MODERNA EN LA BARRA LATERAL
st.sidebar.title("Navegación")

modulos = [
    "Definición de Inteligencia Artificial",
    "Glosario de IA",
    "Algoritmos de Búsqueda",
    "Antecedentes de la IA",
    "IA débil o estrecha",
    "IA fuerte o general",
    "IA superinteligente",
]

for modulo in modulos:
    # Marca visual si la opción está seleccionada
    etiqueta = (
        f"🔹 {modulo}"
        if st.session_state.seccion_activa == modulo
        else f"   {modulo}"
    )
    if st.sidebar.button(etiqueta, key=modulo):
        st.session_state.seccion_activa = modulo

st.sidebar.markdown("---")
st.sidebar.title("Información del Trabajo")
st.sidebar.info(
    """
    **Materia:** Fundamentos de Inteligencia Artificial  
    **Actividad:** Subproducto No. 4 - Glosario  
    """
)

# VISTA 0: DEFINICIÓN DE INTELIGENCIA ARTIFICIAL
if st.session_state.seccion_activa == "Definición de Inteligencia Artificial":
    st.title("Definición de Inteligencia Artificial")

    st.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80",
        caption="Red neuronal y representación del aprendizaje automático",
        use_container_width=True,
    )

    st.markdown(
        """
        ### ¿Qué es la Inteligencia Artificial?
        
        La **Inteligencia Artificial** es un campo interdisciplinario dedicado al diseño de sistemas capaces de realizar 
        tareas asociadas con la inteligencia humana, como **aprender, razonar, reconocer patrones, comprender lenguaje, 
        resolver problemas y tomar decisiones**.
        """
    )

# VISTA 1: GLOSARIO DE IA
elif st.session_state.seccion_activa == "Glosario de IA":
    st.image(
        "https://s03.s3c.es/imag/_v0/1200x655/4/3/0/IA.jpg",
        use_container_width=True,
    )

    st.title("Glosario de Inteligencia Artificial")
    st.write(
        "Explora los conceptos clave de la Inteligencia Artificial. Haz clic"
        " sobre cualquier término para ver su definición o utiliza el buscador"
        " para filtrar la lista."
    )

    glosario = {
        "1. Aprendizaje Automático (Machine Learning)": (
            "Rama de la inteligencia artificial enfocada en el desarrollo de"
            " algoritmos y modelos matemáticos que permiten a las computadoras"
            " aprender, identificar patrones y tomar decisiones a partir de"
            " datos, sin necesidad de ser programadas explícitamente para cada"
            " tarea.\n\n"
            "**Ejemplo práctico:**\n"
            "En un videojuego de rol (RPG), un sistema de Machine Learning detecta bots tramposos "
            "en la casa de subastas analizando el tiempo de reacción exacto que tarda un usuario "
            "en hacer clic sobre un objeto desde el milisegundo en que aparece en pantalla; por "
            "ejemplo, si una espada mítica se publica y un jugador presiona 'Comprar' a los 0.042 "
            "segundos, el modelo procesa este dato de entrada medido en segundos con decimales para "
            "compararlo con el límite fisiológico humano y determinar si la compra fue realizada por "
            "una persona real o por un programa automatizado.\n\n"
            "**Tipo de dato:** `Float`.\n\n"
            "**¿Por qué?**\n"
            "Porque es un número que contiene decimales (puntos flotantes). Como el tiempo de "
            "reacción se mide en fracciones de segundo con gran precisión (0.042, 0.185, 0.005), "
            "se necesita un tipo de dato continuo como `float` (o `double`) para no perder esa "
            "información. Un número entero (`int`) no serviría porque redondearía el dato a 0 o 1, "
            "perdiendo toda la precisión necesaria para detectar al bot."
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
        "21. Sistema Inteligente": (
            "Un sistema computacional interactivo capaz de percibir su entorno "
            "a través de datos o sensores, procesar dicha información mediante "
            "algoritmos de razonamiento o aprendizaje, tomar decisiones autónomas "
            "y ejecutar acciones para alcanzar un objetivo específico de manera eficiente.\n\n"
            "### Esquema del Ecosistema de un Sistema Inteligente\n\n"
            "```text\n"
            "                ┌──────────────────────────────────────────┐\n"
            "                │               ENTORNO / MEDIO            │\n"
            "                │   (El mundo real, datos, usuarios)       │\n"
            "                └────────────────────┬─────────────────────┘\n"
            "                                     │\n"
            "                          [ Realidad / Estímulos ]\n"
            "                                     │\n"
            "                                     ▼\n"
            "┌─────────────────────────────────────────────────────────────────────────┐\n"
            "│                           SISTEMA INTELIGENTE                           │\n"
            "│                                                                         │\n"
            "│  1. PERCEPCIÓN (Entrada)                                                │\n"
            "│  └─► Sensores / Captura de Datos (Cámaras, APIs, Teclado, Micrófono)    │\n"
            "│                                    │                                    │\n"
            "│                                    ▼                                    │\n"
            "│  2. PROCESAMIENTO Y DECISIÓN (Cerebro)                                  │\n"
            "│  └─► Modelo de IA / Algoritmos / Aprendizaje / Base de Conocimiento     │\n"
            "│                                    │                                    │\n"
            "│                                    ▼                                    │\n"
            "│  3. ACCIÓN (Salida)                                                     │\n"
            "│  └─► Actuadores / Ejecución (Motores, Interfaz, Notificaciones, Pantalla)│\n"
            "│                                                                         │\n"
            "└───────────────────────────────────┬─────────────────────────────────────┘\n"
            "                                     │\n"
            "                             [ Cambio / Feedback ]\n"
            "                                     │\n"
            "                                     ▼\n"
            "                ┌──────────────────────────────────────────┐\n"
            "                │        RETROALIMENTACIÓN AL ENTORNO      │\n"
            "                │    (El entorno cambia tras la acción)    │\n"
            "                └──────────────────────────────────────────┘\n"
            "```"
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

# NUEVA VISTA: ALGORITMOS DE BÚSQUEDA
elif st.session_state.seccion_activa == "Algoritmos de Búsqueda":
    st.title("🔎 Algoritmos de Búsqueda en Inteligencia Artificial")
    
    st.markdown("""
    En Inteligencia Artificial, la resolución de problemas a menudo se formula como la búsqueda de una secuencia de acciones que conducen desde una situación inicial hasta un estado meta deseado.
    """)

    st.markdown("---")

    # a) Definición
    st.subheader("a) Definición de Algoritmo de Búsqueda")
    st.info(
        "Un **Algoritmo de Búsqueda** es un método sistemático o conjunto de reglas estructuradas que explora "
        "un **espacio de estados** (un conjunto de configuraciones o situaciones posibles) para encontrar un camino o una "
        "solución que vaya desde un **estado inicial** hasta un **estado objetivo o meta**, optimizando habitualmente "
        "recursos como el tiempo, la distancia o el costo."
    )

    # b) Elementos
    st.subheader("b) Elementos que Intervienen en un Algoritmo de Búsqueda")
    st.markdown("""
    Para formalizar un problema de búsqueda se requieren los siguientes componentes clave:
    
    1. **Estado Inicial:** La configuración o punto de partida del sistema antes de iniciar la búsqueda.
    2. **Conjunto de Estados (Espacio de Estados):** El conjunto de todas las situaciones o configuraciones alcanzables a través de acciones.
    3. **Operadores / Acciones:** Las reglas o transiciones permitidas que transforman un estado en otro.
    4. **Prueba de Meta (Goal Test):** Una función o condición booleana que verifica si un estado determinado corresponde al objetivo buscado.
    5. **Costo del Camino (Cost Function):** Una función numérica que asigna un valor/peso al trayecto recorrido (por ejemplo, distancia, tiempo, combustible, energía).
    6. **Frontier / Lista de Abiertos:** Estructura de datos donde se almacenan los nodos/estados generados pero aún no explorados.
    """)

    # c) Ejemplo
    st.subheader("c) Ejemplo Práctico Identificando Elementos")
    st.write("#### Ejemplo: Un GPS calculando la ruta de Ciudad A (Puebla) a Ciudad B (Ciudad de México)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Estado Inicial:** Estar ubicado en la posición actual (*Puebla*).
        * **Espacio de Estados:** Todas las ciudades, intersecciones y casetas conectadas por la red de carreteras del país.
        * **Acciones / Operadores:** Transitar por un tramo de autopista hacia una ciudad contigua (ej. *Tomar la autopista México-Puebla hacia Ixtapaluca*).
        """)
    with col2:
        st.markdown("""
        * **Prueba de Meta:** ¿La ubicación actual es *Ciudad de México*? (Verdadero/Falso).
        * **Costo del Camino:** La suma de los kilómetros recorridos o minutos del trayecto.
        * **Solución Encontrada:** La ruta óptima que minimiza la distancia total o el tiempo de viaje.
        """)

    # d) Clasificación
    st.subheader("d) Clasificación de los Algoritmos de Búsqueda")
    
    tab1, tab2, tab3 = st.tabs(["1. Búsqueda No Informada (A Ciegas)", "2. Búsqueda Informada (Heurística)", "3. Búsqueda Adversarial"])
    
    with tab1:
        st.markdown("""
        #### Búsqueda No Informada (Uninformed / Blind Search)
        No utiliza conocimiento específico sobre el dominio del problema más allá de la definición de los estados y operadores. Explora de forma ciega.
        * **Búsqueda en Anchura (BFS - Breadth-First Search):** Explora nodo por nodo nivel a nivel. Garantiza encontrar la solución más corta en grafos no ponderados.
        * **Búsqueda en Profundidad (DFS - Depth-First Search):** Explora lo más profundo posible a lo largo de cada rama antes de retroceder (backtracking).
        * **Búsqueda de Costo Uniforme (UCS / Dijkstra):** Evalúa nodos expandiendo siempre el de menor costo acumulado $g(n)$.
        """)
        
    with tab2:
        st.markdown("""
        #### Búsqueda Informada (Informed / Heuristic Search)
        Utiliza conocimiento previo o guías estimadas (**función heurística $h(n)$**) para dirigir la búsqueda de manera eficiente hacia la meta.
        * **Búsqueda Primero el Mejor (Greedy Best-First Search):** Elige expandir el nodo que parece estar más cerca de la meta según la heurística $h(n)$.
        * **Algoritmo A* (A-Star):** Combina el costo real acumulado $g(n)$ con la estimación heurística $h(n)$ mediante la función $f(n) = g(n) + h(n)$. Es óptimo y completo.
        """)

    with tab3:
        st.markdown("""
        #### Búsqueda Adversarial (Juegos)
        Se aplica en entornos competitivos donde dos o más agentes persiguen objetivos opuestos.
        * **Algoritmo Minimax:** Utilizado en juegos de suma cero de dos jugadores (ej. Ajedrez, Tres en Raya). Minimiza la máxima pérdida posible del jugador.
        * **Poda Alfa-Beta ($\alpha-\beta$ Pruning):** Optimización de Minimax que elimina ramas del árbol de búsqueda que no afectarán la decisión final.
        """)

# VISTA 2: ANTECEDENTES DE LA IA
elif st.session_state.seccion_activa == "Antecedentes de la IA":
    st.title("Antecedentes de la IA")
    try:
        st.image("linea_del_tiempo.jpg", use_container_width=True)
    except Exception:
        st.error(
            "Asegúrate de haber subido el archivo 'linea_del_tiempo.jpg' a tu"
            " repositorio de GitHub."
        )

# VISTA 3: IA DÉBIL O ESTRECHA
elif st.session_state.seccion_activa == "IA débil o estrecha":
    st.title("IA débil o estrecha")
    mostrar_pdf("ia_debil.pdf")

# VISTA 4: IA FUERTE O GENERAL
elif st.session_state.seccion_activa == "IA fuerte o general":
    st.title("IA fuerte o general")
    mostrar_pdf("ia_fuerte.pdf")

# VISTA 5: IA SUPERINTELIGENTE
elif st.session_state.seccion_activa == "IA superinteligente":
    st.title("IA superinteligente")
    mostrar_pdf("ia_superinteligente.pdf")

# Pie de página y referencias
st.markdown("---")
st.subheader("Referencias Bibliográficas")
st.markdown(
    """
    * Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
    * Google Cloud. (s. f.). *Glosario de IA generativa*. Documentación de Google Cloud. https://docs.cloud.google.com/docs/generative-ai/glossary?hl=es-419
    * Ray, S. (6 de noviembre de 2023). *10 términos de IA que todos deberían conocer*. Microsoft Source LATAM. https://news.microsoft.com/source/latam/features/ia/10-terminos-de-ia-que-todos-deberian-conocer/
    """
)

st.markdown("---")
st.markdown(
    """
    <div class="footer-container">
        © 2026 Todos los derechos reservados. Desarrollado por <strong>Martín Romero Vélez</strong>.<br>
        <a href="https://github.com" target="_blank">🐙 Visitar perfil de GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Programa: Juego de preguntas y respuestas
# Tema: Algoritmos de búsqueda y ordenamiento
# Materia: Programación I - UTN
# Integrantes: Federico Duarte y Natalia Córdoba
# ---------------------------------------------------------------------------------------------------

# CREACIÓN DE UNA FUNCIÓN PARA ARMAR LISTAS UTIL PARA EXPLICAR EL MÉTODO DE BÚSQUEDA BINARIO
def generar_lista():
    return list(range(1,100,3))
lista_binario=generar_lista()

# PREGUNTAS DEL JUEGO
PREGUNTAS = [
    # Nivel 1: Búsqueda Lineal
    {"nivel": 1,
        "texto": "Si Tienes la siguiente lista: [5, 3, 8, 2, 9, 1]. \nDebes buscar el número 8 recorriéndola elemento por elemento. ¿Qué algoritmo utilizarías?",
        "opciones": ["Búsqueda lineal", "Búsqueda binaria"],
        "respuesta_correcta": "1"
    },
    # Nivel 2: Búsqueda Binaria
    {"nivel": 2,
        "texto": f"Si tienes la siguiente lista: {lista_binario} \nDebes buscar el número 82 en ella, pensando en la eficiencia de busqueda  y la cantitad de valores de la lista . ¿Qué algoritmo utilizarías ?",
        "opciones": ["Búsqueda lineal", "Búsqueda binaria"], 
        "respuesta_correcta": "2"
    },
    # Nivel 3: Bubble Sort (Ordenamiento por burbuja)
    {"nivel": 3,
        "texto": "Tienes la siguiente lista: [19, 32, 71, 13, 4, 58]. \n¿Cuál de los siguientes algoritmos usarías para comparar cada elemento de la lista con el siguiente y luego intercambiarlos si no están en el orden correcto?",
        "opciones": ["Selection Sort", "Bubble Sort", "Insertion Sort", "Quick Sort"],
        "respuesta_correcta": "2"  
    },
    # Nivel 4: Selection Sort (Ordenamiento por selección)
    {"nivel": 4,
        "texto": "Tienes la siguiente lista: [66, 23, 17, 4, 33]. \n¿Qué algoritmo utilizarías para encontrar el elemento menor de la lista y luego colocarlo en el primer elemento, repitiendo este proceso con todos los elementos?",
        "opciones": ["Insertion Sort", "Quick Sort", "Selection Sort", "Bubble Sort"],
        "respuesta_correcta": "3"
    },
    # Nivel 5: Insertion Sort (Ordenamiento por inserción) 
    {"nivel": 5,
    "texto": "¿Qué algoritmo de ordenamiento construye la lista ordenada elemento por elemento, insertando cada nuevo elemento en la posición correcta?",
    "opciones": ["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort"],
    "respuesta_correcta": "3"
    },
    # Nivel 6: Quick Sort (Ordenamiento rápido)
    {
    "nivel": 6,
    "texto": "¿Cuál de los siguientes algoritmos utiliza el concepto de divide y vencerás para ordenar una lista utilizando un pivote?",
    "opciones": ["Bubble Sort", "Quick Sort", "Insertion Sort", "Selection Sort"],
    "respuesta_correcta": "2"
    },
]

# FUNCIÓN PARA MOSTRAR LAS PREGUNTAS AL USUARIO
def hacer_pregunta(pregunta):
    print(f"\nNivel {pregunta['nivel']}:")
    print(f"{pregunta['texto']}")
    for i, opcion in enumerate(pregunta['opciones'], 1):
        print(f"{i}. {opcion}")
    
    while True:
        respuesta = input(f"Tu respuesta (número): ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta['opciones']):
            break
        print(f"¡Opción inválida! Ingresa un número entre 1 y {len(pregunta['opciones'])}" )
    
    if respuesta == pregunta['respuesta_correcta']:
        print("="*80)
        print( "¡Correcto!")
        resolver_algoritmo(pregunta['nivel'])
        print("="*80)
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era: {pregunta['opciones'][int(pregunta['respuesta_correcta'])-1]}" )
        return False
    
# FUNCIONES PARA LOS ALGORITMOS DE BÚSQUEDA
# Función busqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
# Función busqueda binaria
def busqueda_binaria(lista_binario, objetivo):
    izquierda, derecha = 0, len(lista_binario) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_binario[medio] == objetivo:
            return medio
        elif lista_binario[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# FUNCIONES PARA LOS ALGORITMOS DE ORDENAMIENTO
# Función Bubble_sort 
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
# Función selection_sort
def selection_sort(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
# Función insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
# Función quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# FUNCION RESOLVER ALGORÍTMO (cuando la respuesta del usuario es correcta)
def resolver_algoritmo(nivel):
    # Búsqueda lineal
    if nivel == 1:
        lista = [5, 3, 8, 2, 9, 1]
        print(f"Buscando el número 8 en {lista}" )
        print(f"El nuero se encuentra en la posicion  {busqueda_lineal(lista, 8) + 1} ")
        print(f"Explicacion: La respuesta corresta es lineal, dado que la lista es relativamente corta y es la manera de buscar elemento por elemento")
    # Busqueda Binaria 
    elif nivel == 2:
        lista = lista_binario
        print(f"Buscando  el número 82 en {lista} ")
        print(f"Se encuentra en la posicion {busqueda_binaria(lista, 82) + 1} de la lista" )
        print(f"Explicacion: La respuesta corresta es binaria, dado que la lista es bastante grande y se ve claramente que el valor requerido esta mas alla de la mitad y este es el modo mas eficiente para este tipo de busquedas")
    # Bubble Sort
    elif nivel == 3:
        lista = [19, 32, 71, 13, 4, 58]
        lista_ordenada = selection_sort(lista.copy())
        print(f"La lista {lista} ordenada con Bubble sort es {lista_ordenada}" )
        print(f"Explicacion:  Bubble Sort compara elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso hasta que la lista esté completamente ordenada.")
    # Selection Sort
    elif nivel == 4:
        lista = [66, 23, 17, 4, 33]
        lista_ordenada = selection_sort(lista.copy())
        print(f"La lista {lista} ordenada con Selection es {lista_ordenada}")
        print(f"Explicación: Selection Sort busca el elemento más pequeño en cada iteración y lo coloca en su posición correcta.")        
    # Ordenamiento Insertion Sort
    elif nivel == 5:
        lista = [19, 32, 71, 13, 4, 58]
        lista_ordenada = insertion_sort(lista.copy())
        print(f"La lista {lista} ordenada con Isertion es {lista_ordenada}")
        print(f"Explicación: Insertion Sort construye la lista ordenada un elemento a la vez, tomando cada nuevo elemento y colocándolo en la posición correcta dentro de la parte ya ordenada.")
    # Ordenamiento Quick Sort
    elif nivel == 6:
        lista = [19, 32, 71, 13, 4, 58]
        lista_ordenada = quick_sort(lista.copy())
        print(f"La lista {lista} ordenada con Quick sort es {lista_ordenada}")
        print(f"Explicación: Quick Sort utiliza la técnica 'divide y vencerás': selecciona un 'pivote', divide la lista en elementos menores y mayores al pivote, y luego repite el proceso recursivamente con cada sublista.")

# MENÚ PRINCIPAL DEL JUEGO
def jugar():
    while True:
        print("="*80)
        print("BIENVENIDO/A AL QUIZZ DE ALGORITMOS")
        print("="*80)
        aciertos = 0
        
#ACA AGREGO OPCIONES GRAFICAS PARA RESALTAR 

        for pregunta in PREGUNTAS:
            if hacer_pregunta(pregunta):
                aciertos += 1
        print("="*80)
        print(f"Juego terminado. Aciertos: {aciertos}")
        if aciertos == 6:
            print(f"¡Perfecto! Has respondido correctamente todas las preguntas.")
        elif aciertos >= 4:
            print(f"¡Muy bien! Has respondido bien más de la mitad de las preguntas.")
        else:
            print(f"Debes practicar un poco más.")
        
        volver_a_jugar= input("\n¿Quieres jugar de nuevo? (sí/no): ").lower().strip()
        if volver_a_jugar != 'si' and volver_a_jugar != 'sí':
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break

# ENTRADA AL JUEGO
if __name__ == "__main__":  # Ejecuta el juego solo si el archivo se ejecuta directamente
    jugar()
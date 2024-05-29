# Ingeniería del Software I - Tema 5: Diseño

## Objetivos
- **Objetivo**: Conocer la etapa de diseño del software y los diagramas utilizados en esta etapa tanto para el modelado estático (estructural) como dinámico.

## Bibliografía
1. Booch, G., Rumbaugh, J., Jacobson, I. (2006). El lenguaje Unificado de Modelado. Addison Wesley.
2. Arlow, J., Neustadt, I. (2006). UML 2 and the Unified Process. Practical Object Oriented Analysis and Design, 2nd Edition. Addison-Wesley.

---

## Introducción al Diseño de Software
- **Diseño**: Es el proceso creativo de transformación del problema en una solución; la descripción de una solución también se llama diseño (Pfleeger, 2002).
- **Objetivo del diseño**: A partir de la especificación de requisitos (entre ellos el modelo de casos de uso) se obtiene el diseño del sistema.
- **Criterios del diseño**:
  - Un diseño es adecuado si y solo si satisface todos los requisitos.
  - Pueden existir múltiples diseños para un mismo problema.
  - Es necesario decidir cuál diseño conviene más.
  - El diseño puede variar durante el ciclo de desarrollo debido a cambios de requisitos tras el análisis.

### ¿Qué es diseñar?
- "Diseñar un sistema es determinar el conjunto de componentes y de interfaces entre componentes que satisfagan un conjunto específico de requisitos" (DeMarco, 1982).

---

## Modelado Estructural

### Diagramas UML para Modelado Estructural
1. **Diagramas de Clases**:
   - Representan la estructura estática del sistema.
   - Incluyen clases, interfaces, y colaboraciones.
   - Ejemplo: Un diagrama de clases para un sistema de biblioteca puede incluir clases como `Libro`, `Usuario`, `Préstamo`, con relaciones de asociación entre ellas.

2. **Diagramas de Objetos**:
   - Representan instancias de clases en un momento específico.
   - Ejemplo: Instancias de `Libro` como `libro1:Libro`, `libro2:Libro`, y sus relaciones en un momento dado.

3. **Diagramas de Estructura Compuesta**:
   - Muestran la estructura interna de una clase o colaboración.
   - Ejemplo: La clase `Ordenador` puede tener componentes como `CPU`, `Memoria`, `Almacenamiento`.

4. **Diagramas de Artefactos**:
   - Representan artefactos físicos en el sistema y sus relaciones.
   - Ejemplo: Archivos ejecutables, bases de datos y su relación con el software.

5. **Diagramas de Componentes**:
   - Muestran los componentes de software y sus relaciones.
   - Ejemplo: Componentes de un sistema de e-commerce como `Catálogo`, `Carrito`, `Pago`, y sus dependencias.

6. **Diagramas de Despliegue**:
   - Representan la configuración física del hardware y software del sistema.
   - Ejemplo: Un servidor web conectado a una base de datos y su interacción con los usuarios.

### Elementos de los Diagramas de Clases
- **Clases**:
  - Descriptor de un conjunto de objetos con los mismos atributos, métodos, relaciones y comportamiento.
  - **Nombre**: Identificación de la clase. Debe ser simple y descriptivo.
  - **Atributos**: Propiedades compartidas por todos los objetos de la clase.
  - **Métodos**: Implementación de servicios que la clase puede proporcionar.
  - **Responsabilidades**: Contratos u obligaciones de una clase.
  - Ejemplo: La clase `Libro` puede tener atributos como `titulo`, `autor`, `ISBN` y métodos como `prestar()`, `devolver()`.

- **Relaciones**:
  - **Asociación**: Relación estructural entre clases. Ejemplo: `Usuario` asociado a `Préstamo`.
  - **Dependencia**: Relación de uso que indica que un cambio en una clase puede afectar a otra. Ejemplo: `Pedido` depende de `Producto`.
  - **Generalización (Herencia)**: Relación “es-un” entre una clase general (padre) y una clase específica (hija). Ejemplo: `Vehículo` generaliza a `Coche` y `Moto`.
  - **Agregación**: Relación “todo/parte” que indica que una clase está compuesta por otras clases. Ejemplo: `Clase` tiene `Estudiantes`.

### Notas, Estereotipos y Valores Etiquetados
- **Notas**: Proporcionan información adicional sobre un elemento.
- **Estereotipos**: Extienden el vocabulario UML, proporcionando un significado adicional a los elementos del modelo.
- **Valores Etiquetados**: Información adicional sobre las relaciones y elementos del modelo.

---

## Diagramas de Clases

### Uso y Ejemplos
- **Modelan la vista estática de diseño del sistema**: Definen las clases y las relaciones estáticas entre ellas.
- **Base para otros diagramas**: Son la base para diagramas de componentes y de despliegue.
- **Ejemplos**:
  - **Sistema de Gestión de Pedidos**:
    - Clases: `Cliente`, `Pedido`, `LíneaPedido`, `Producto`.
    - Relaciones: `Cliente` realiza `Pedidos`, `Pedido` contiene `LíneaPedido`, `LíneaPedido` se refiere a `Producto`.
  - **Modelado de Colaboraciones Simples**: Identificar clases y relaciones que colaboran para realizar un comportamiento específico.

---

## Ingeniería Directa e Inversa

### Ingeniería Directa
- **Transformación de un modelo en código**: A través de una correspondencia con un lenguaje de implementación.
- **Pasos**:
  - Identificar las reglas de correspondencia modelo-lenguaje.
  - Restringir según el lenguaje destino.
  - Utilizar valores etiquetados para especificar el lenguaje destino.
  - Usar herramientas para ingeniería directa.
- **Ejemplo**: Generar código Java a partir de un diagrama de clases de un sistema de gestión de inventarios.

### Ingeniería Inversa
- **Transformación de código en un modelo**: A través de una correspondencia con un lenguaje específico.
- **Pasos**:
  - Identificar las reglas de correspondencia.
  - Utilizar herramientas para inspeccionar el código y generar el modelo.
  - Crear el diagrama de clases a partir del modelo generado.
- **Ejemplo**: Analizar un sistema de gestión de ventas y generar su diagrama de clases UML.

---

## Modelado del Comportamiento

### Diagramas UML para Modelado del Comportamiento
1. **Diagramas de Casos de Uso**:
   - Capturan el comportamiento deseado del sistema sin especificar cómo se implementa.
   - Ejemplo: Un caso de uso "Realizar Pedido" que incluye acciones como "Seleccionar Producto", "Añadir al Carrito", "Pagar".

2. **Diagramas de Interacción**:
   - Modelan aspectos dinámicos de las colaboraciones.
   - Ejemplo: Un diagrama de secuencia que muestra la interacción entre el usuario y el sistema durante el proceso de compra.

3. **Diagramas de Estados**:
   - Centrados en el estado cambiante de un sistema dirigido por eventos.
   - Ejemplo: Estados de un pedido como "Nuevo", "Procesado", "Enviado", "Entregado".

4. **Diagramas de Actividad**:
   - Centrados en el flujo de control de actividades.
   - Ejemplo: Flujo de actividades para el procesamiento de un pedido desde la recepción hasta la entrega.

### Diagramas de Interacción

#### Conceptos Básicos
- **Enlaces**:
  - Conexiones semánticas entre objetos (instancias de asociaciones).
  - Especifican un camino a lo largo del cual un objeto puede enviar un mensaje a otro objeto (o a sí mismo).
  
- **Mensajes**:
  - Necesarios para modelar los aspectos dinámicos.
  - Especificación de una comunicación entre objetos que transmite información con la expectativa de que se desencadenará una actividad.
  - Tipos de acciones en UML:
    - **Llamada**: Invocación de un método.
    - **Retorno**: Respuesta de una llamada.
    - **Envío**: Envío de una señal.
    - **Creación**: Instanciación de un objeto.
    - **Destrucción**: Eliminación de un objeto.

#### Diagramas de Secuencia
- **Características y Elementos**:
  - **Objetos**: Colocados en la parte superior del diagrama (eje X).
  - **Mensajes**: Colocados a lo largo del eje Y en orden de sucesión en el tiempo.
  - **Línea de Vida**: Representa la existencia de un objeto a lo largo del tiempo.
  - **Foco de Control**: Representa el período durante el cual un objeto ejecuta una acción.
  - **Fragmentos Combinados**: Modelan estructuras de control como alternativas y bucles.

- **Cómo Crear un Diagrama de Secuencia**:
  1. Establecer el contexto de la interacción.
  2. Colocar los objetos que participan en la interacción en la parte superior del diagrama.
  3. Colocar los mensajes que los objetos envían y reciben a lo largo del eje Y, en orden de sucesión en el tiempo.
  4. Si es necesario, visualizar el anidamiento de mensajes o el intervalo de tiempo en el que tiene lugar la computación.
  5. Especificar restricciones de tiempo o espacio si es necesario.

- **Ejemplo**: Interacción entre `Usuario`, `Sistema`, y `Base de Datos` para el proceso de autenticación.

#### Diagramas de Comunicación
- **Características y Elementos**:
  - **Objetos**: Colocados como nodos del grafo.
  - **Enlaces**: Conexiones entre objetos.
  - **Mensajes**: Comunicación entre objetos con numeración de secuencia.

- **Cómo Crear un Diagrama de Comunicación**:
  1. Establecer el contexto de la interacción.
  2. Colocar los objetos que participan en la colaboración como nodos del grafo.
  3. Representar los enlaces que conectan esos objetos como arcos del grafo.
  4. Adornar los enlaces con los mensajes que envían y reciben los objetos.
  5. Establecer la numeración de secuencia para indicar el orden temporal de los mensajes.

- **Ejemplo**: Interacción estructural entre `Cliente`, `Vendedor`, y `Sistema de Inventario`.

#### Diagramas de Vista Global de la Interacción
- Tipo especial de diagramas de actividad donde cada nodo se refiere a otras interacciones.
- **Ejemplo**: Resumen de todas las interacciones de un sistema de comercio electrónico.

#### Diagramas de Tiempos
- Destacan aspectos de tiempo real de la interacción.
- **Ejemplo**: Sincronización de mensajes en un sistema de monitoreo en tiempo real.

---

## Máquinas de Estados

### Conceptos Básicos
- **Eventos**: Acontecimientos que ocurren y ocupan un lugar en el tiempo y espacio.
  - Tipos: Síncronos (llamadas), Asíncronos (señales, paso del tiempo, cambio de estado).
- **Estado**: Momento en la vida de un objeto en el que se satisface alguna condición, realiza alguna actividad o espera algún evento.
- **Transición**: Relación entre dos estados que indica que un objeto realiza ciertas acciones para pasar de un estado a otro.
  - **Estado origen**: Estado del que parte dicha transición.
  - **Evento de disparo**: Provoca la transición al estado destino.
  - **Condición de guarda**: Expresión booleana que se activa por la recepción de un evento.
  - **Acción**: Computación atómica ejecutable que actúa sobre el objeto asociado a la máquina de estados.
  - **Estado destino**: El estado donde finaliza la transición.

### Diagramas de Estados
- Muestran una máquina de estados que describe la secuencia de estados por las que pasa un objeto a lo largo de su vida en respuesta a eventos, junto con la respuesta a esos eventos.
- Los diagramas de estados pueden asociarse a clases, casos de uso o sistemas completos para modelar la dinámica de un objeto individual (Objeto Reactivo).
- Útiles para objetos que tienen un ciclo de vida bien definido cuyo comportamiento se ve afectado por su pasado.
- **Ejemplo**: Un `Pedido` en una tienda online puede tener estados como "Pendiente", "Procesando", "Enviado", "Entregado".

---

## Diagramas de Actividades

### Modelado de Flujo de Trabajo
- **Actividades**: Ejecución no atómica que produce acciones y cambios de estado.
- **Elementos**: Modelan el flujo de objetos y el flujo de control de una operación.
- **Uso en Ingeniería Directa/Inversa**: Visualización, especificación y construcción de la dinámica del sistema.
- **Ejemplo**: Un diagrama de actividad que muestra los pasos para el procesamiento de un pedido desde la recepción hasta la entrega.

---

# Patrones GOF Creacionales en Python

Repositorio académico que contiene la implementación de dos patrones de diseño creacionales del catálogo **GOF (Gang of Four)** utilizando **Python**:

- **Factory Method**
- **Abstract Factory**

Estos ejercicios fueron desarrollados como parte del estudio de los patrones de diseño y arquitectura de software, aplicando los conceptos teóricos a casos prácticos que demuestran cómo desacoplar la creación de objetos del código cliente.

---

# Objetivos

- Comprender el funcionamiento de los patrones creacionales.
- Identificar cuándo utilizar Factory Method y cuándo utilizar Abstract Factory.
- Aplicar principios de diseño orientado a objetos.
- Reducir el acoplamiento entre el cliente y las clases concretas.
- Facilitar la extensión y mantenimiento del software.

---

# Estructura del proyecto

```text
patrones-creacionales-python
│
├── factory-method-notificaciones
│   └── main.py
│
├── abstract-factory-ui
│   └── main.py
│
└── README.md
```

---

# Ejercicio 1: Sistema de Notificaciones

## Patrón utilizado

Factory Method

## Descripción

Una empresa de software necesita un sistema capaz de enviar notificaciones utilizando diferentes canales de comunicación:

- Correo electrónico
- SMS
- Notificaciones Push

El objetivo es permitir la incorporación de nuevos canales sin modificar el código cliente que utiliza el servicio.

## Estructura del patrón

### Producto

```text
Notificacion
```

Define la interfaz común para todas las notificaciones.

### Productos concretos

```text
NotificacionEmail
NotificacionSMS
NotificacionPush
```

Implementan el comportamiento específico de cada canal de comunicación.

### Creador

```text
CreadorNotificacion
```

Declara el Factory Method responsable de crear los objetos de tipo Notificación.

### Creadores concretos

```text
CreadorEmail
CreadorSMS
CreadorPush
```

Cada uno crea una instancia específica de notificación.

### Cliente

```text
Cliente
```

Utiliza únicamente las abstracciones y desconoce las clases concretas que están siendo instanciadas.

## Beneficios obtenidos

- Bajo acoplamiento.
- Fácil incorporación de nuevos canales.
- Cumplimiento del principio Abierto/Cerrado.
- Mayor flexibilidad para futuras extensiones.

---

# Ejercicio 2: Suite de Herramientas UI Multiplataforma

## Patrón utilizado

Abstract Factory

## Descripción

Una startup desea desarrollar una aplicación de escritorio que funcione tanto en Windows como en macOS.

La interfaz gráfica debe estar formada por:

- Botones
- Ventanas

Cada sistema operativo requiere componentes visuales diferentes, por lo que se necesita crear familias completas de objetos relacionados sin depender de implementaciones concretas.

## Estructura del patrón

### Productos abstractos

```text
Boton
Ventana
```

Definen las interfaces comunes de los componentes gráficos.

### Productos concretos

#### Familia Windows

```text
BotonWindows
VentanaWindows
```

#### Familia macOS

```text
BotonMac
VentanaMac
```

### Fábrica abstracta

```text
FabricaUI
```

Declara los métodos necesarios para crear todos los productos de una familia.

### Fábricas concretas

```text
FabricaWindows
FabricaMac
```

Generan componentes pertenecientes a una misma familia.

### Cliente

```text
Aplicacion
```

Trabaja exclusivamente con interfaces abstractas y recibe una fábrica concreta mediante inyección de dependencias.

## Beneficios obtenidos

- Independencia respecto a las clases concretas.
- Garantía de compatibilidad entre componentes de una misma familia.
- Facilidad para incorporar nuevas plataformas.
- Mayor mantenibilidad del código.

---

# Diferencia entre Factory Method y Abstract Factory

| Factory Method                                              | Abstract Factory                                                    |
| ----------------------------------------------------------- | ------------------------------------------------------------------- |
| Crea un único producto.                                     | Crea familias completas de productos relacionados.                  |
| Utiliza un método de fabricación.                           | Utiliza una fábrica compuesta por múltiples métodos de fabricación. |
| Menor complejidad.                                          | Mayor complejidad.                                                  |
| Ideal cuando se necesita decidir qué objeto concreto crear. | Ideal cuando se necesita cambiar familias completas de objetos.     |

---

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Clases abstractas (`abc`)
- Patrones de diseño GOF

---

# Cómo ejecutar los ejercicios

## Clonar el repositorio

```bash
git clone https://github.com/AdrianAniel/patrones-creacionales-python.git
```

## Ejecutar el ejercicio Factory Method

```bash
cd factory-method-notificaciones
python main.py
```

## Ejecutar el ejercicio Abstract Factory

```bash
cd abstract-factory-ui
python main.py
```

---

# Conceptos aplicados

- Abstracción
- Herencia
- Polimorfismo
- Inyección de dependencias
- Principio Abierto/Cerrado (OCP)
- Desacoplamiento entre cliente e implementación
- Patrones Creacionales GOF

---

# Autor

**Adrián Aniel Alpizar Pérez**

Repositorio desarrollado con fines académicos para el estudio e implementación de los patrones de diseño creacionales **Factory Method** y **Abstract Factory** en Python.

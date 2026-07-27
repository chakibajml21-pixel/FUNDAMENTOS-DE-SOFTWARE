# 🏦 Quantum Wallet - Semana 6
## Implementación del Patrón de Diseño Singleton

### 📖 Descripción

Este proyecto implementa el **Patrón de Diseño Singleton** utilizando Python.

El objetivo es demostrar cómo garantizar que una clase tenga **una única instancia** durante toda la ejecución del programa y que todos los objetos creados compartan la misma información.

En este caso se desarrolló la clase **GestorBanco**, encargada de administrar la información general del sistema bancario, como clientes, cuentas y transacciones.

---

## Objetivo

Aplicar el patrón de diseño **Singleton** para asegurar que exista un único administrador del sistema bancario, evitando la creación de múltiples objetos con información diferente.

---

## Estructura del proyecto

```
Semana_6/
│
├── banco_central.py
└── README.md
```

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Patrón de Diseño Singleton

---

## Funcionamiento

La clase **GestorBanco** utiliza el método especial `__new__()` para controlar la creación de objetos.

Cuando se intenta crear una nueva instancia:

- Si no existe ninguna, se crea.
- Si ya existe una instancia, simplemente se devuelve la misma.

De esta forma todos los objetos apuntan al mismo espacio de memoria.

---

## Características

- Solo existe una instancia del gestor del banco.
- Administración centralizada de la información.
- Registro de clientes.
- Registro de cuentas.
- Registro de transacciones.
- Compartición de datos entre todas las referencias al objeto.

---

## Ejecución

Desde la terminal, ubicarse en la carpeta del proyecto:

```bash
cd MisProyectosPython/Semana_6
```

Ejecutar:

```bash
python banco_central.py
```

---

## Ejemplo de salida

```text
ID del gestor1: 2384723894
ID del gestor2: 2384723894
¿Son el mismo objeto? True

Cliente 'Carlos Gómez' registrado correctamente.
Cliente 'Laura Martínez' registrado correctamente.

Cuenta 1001 creada.
Cuenta 1002 creada.

========== RESUMEN DEL BANCO ==========
Clientes registrados: 2
Cuentas creadas: 2
Transacciones realizadas: 2
```

---

## Explicación del Singleton

El patrón Singleton garantiza que exista **una sola instancia** de una clase.

En este proyecto:

- `gestor1 = GestorBanco()`
- `gestor2 = GestorBanco()`

Aunque parecen dos objetos distintos, ambos hacen referencia al mismo objeto en memoria.

Esto se puede comprobar con:

```python
print(gestor1 is gestor2)
```

Resultado:

```text
True
```

También ambos poseen el mismo identificador (`id()`), confirmando que son la misma instancia.

---

##  Conceptos aplicados

- Clases
- Objetos
- Métodos especiales (`__new__`)
- Atributos de clase
- Encapsulamiento
- Programación Orientada a Objetos
- Patrón de Diseño Singleton

---

## Autor

**Nombre:** Chakiba Jamal

**Proyecto:** Quantum Wallet

**Asignatura:** Fundamentos de Software

**Semana:** 6

**Tema:** Patrón de Diseño Singleton

---

## Cómo ejecutar
```bash
python usuarios.py         # ver la Quantum Wallet funcionando
python banco_central.py    # ver la única instancia del Singleton
```

# SmartPay

## Sistema inteligente para el registro, validación y clasificación de solicitudes de aplicación de pagos de cartera de créditos

**Autora:** Linda Ortiz  
**Repositorio:** `proyectoFinal_SmartPay`  
**Rama individual de trabajo:** `dev_jcol_10`  
**Rama de consolidación:** `develop`  
**Tipo de proyecto:** Prototipo académico de Machine Learning.

---

## 1. Descripción del proyecto

SmartPay es un prototipo académico que permite registrar, validar y clasificar solicitudes simuladas de aplicación de pagos de cartera de créditos.

La solución combina reglas de negocio determinísticas con un modelo de Machine Learning basado en un Árbol de Decisión (`DecisionTreeClassifier`), con el propósito de estudiar patrones relacionados con solicitudes aceptadas y rechazadas.

El proyecto cuenta con una aplicación gráfica desarrollada en Streamlit, que permite ingresar información ficticia de las solicitudes, verificar las condiciones de negocio y obtener una clasificación experimental del modelo.

SmartPay utiliza exclusivamente datos sintéticos. No se conecta a sistemas bancarios reales, no consulta información financiera de clientes, no ejecuta débitos, no aplica pagos y no realiza integraciones productivas con Wolf ni con herramientas RPA.

## 2. Problema que aborda

Una solicitud de aplicación de pago puede ser rechazada por diferentes inconsistencias o incumplimientos de las condiciones del proceso, entre ellos:

- Datos obligatorios incompletos.
- Números de cuenta o crédito que no contienen exactamente 11 dígitos numéricos.
- Cuenta inactiva.
- Crédito cancelado.
- Crédito que no corresponde al NIT informado.
- Saldo disponible insuficiente.
- Valor del pago incompatible con el tipo de operación.

SmartPay representa estas situaciones mediante datos ficticios y reglas de negocio simuladas para estudiar su validación y clasificación.

## 3. Objetivos del proyecto

### Objetivo general

Desarrollar un prototipo académico que permita registrar, validar y clasificar solicitudes simuladas de aplicación de pagos de cartera mediante reglas de negocio y un modelo básico de Machine Learning.

### Objetivos específicos

1. Construir un dataset sintético de solicitudes de aplicación de pagos.
2. Implementar validaciones para los datos de entrada y las condiciones de negocio.
3. Aplicar técnicas de preprocesamiento y preparación de datos.
4. Entrenar un modelo de clasificación basado en Árbol de Decisión.
5. Evaluar el desempeño del modelo mediante métricas de clasificación y matriz de confusión.
6. Comparar el modelo seleccionado con un modelo de referencia Baseline.
7. Desarrollar una interfaz gráfica que permita interactuar con el prototipo.

## 4. Alcance funcional

### Funcionalidades implementadas

- Registro de solicitudes mediante una interfaz gráfica.
- Validación de campos obligatorios.
- Validación de números de cuenta y crédito con exactamente 11 dígitos numéricos.
- Validación del valor según el tipo de operación.
- Simulación de condiciones de cuenta y crédito.
- Verificación del saldo disponible simulado.
- Verificación de la correspondencia entre crédito y NIT.
- Generación de un dataset sintético.
- Exploración y visualización de los datos.
- Preprocesamiento y división de los conjuntos de entrenamiento y prueba.
- Entrenamiento de un Árbol de Decisión.
- Evaluación mediante Accuracy, Precision, Recall y F1-score.
- Comparación con un modelo de referencia DummyClassifier.
- Presentación de resultados en una aplicación Streamlit.
- Ejecución de pruebas automatizadas de validación.

### Reglas de negocio

Las validaciones principales son:

1. Los números de cuenta y crédito deben contener exactamente 11 dígitos numéricos.
2. El pago de cuota debe coincidir exactamente con la cuota pendiente.
3. El abono a capital debe ser positivo y no superar el capital pendiente.
4. El abono a intereses debe ser positivo y no superar los intereses pendientes.
5. El pago total debe coincidir exactamente con el valor de liquidación.
6. La cuenta debe encontrarse activa.
7. El crédito debe encontrarse vigente.
8. El saldo disponible simulado debe ser suficiente.
9. El crédito debe corresponder al NIT informado.

Las reglas de negocio son los controles principales del prototipo. El modelo de Machine Learning no reemplaza estas validaciones ni autoriza operaciones financieras.

### Funcionalidades fuera del alcance

- Conexión con bases de datos bancarias productivas.
- Consulta de información real de clientes, cuentas o créditos.
- Ejecución de débitos o movimientos de dinero.
- Aplicación efectiva de pagos.
- Integración productiva con Wolf o herramientas RPA.
- Autorización automática de transacciones financieras.

## 5. Tecnologías utilizadas

| Tecnología | Uso dentro del proyecto |
|---|---|
| Python | Lenguaje de programación. |
| pandas | Manipulación y análisis de datos. |
| NumPy | Operaciones numéricas. |
| Matplotlib | Generación de gráficas. |
| scikit-learn | Preprocesamiento, entrenamiento y evaluación de modelos. |
| Streamlit | Desarrollo de la interfaz gráfica. |
| joblib | Almacenamiento y recuperación del modelo entrenado. |
| Git | Control de versiones. |
| GitHub | Administración del repositorio y consolidación del desarrollo. |
| Visual Studio Code | Entorno de desarrollo. |

## 6. Aplicación desarrollada con Streamlit

SmartPay cuenta con una interfaz gráfica desarrollada mediante Streamlit para facilitar el registro, validación y clasificación experimental de solicitudes.

La aplicación se encuentra en:

`src/aplicacion.py`

La interfaz está organizada en tres secciones:

### 6.1. Datos de la solicitud

Permite ingresar:

- NIT ficticio.
- Nombre del cliente ficticio.
- Número de cuenta.
- Tipo de cuenta.
- Número de crédito.
- Tipo de operación.
- Valor del pago.

### 6.2. Condiciones simuladas

Permite ingresar las condiciones necesarias para evaluar la solicitud:

- Cuota pendiente.
- Capital pendiente.
- Intereses pendientes.
- Valor de liquidación.
- Saldo disponible simulado.
- Estado de la cuenta.
- Estado del crédito.
- Correspondencia entre el crédito y el NIT.

### 6.3. Resultado de la validación

La aplicación presenta los mensajes correspondientes a las validaciones realizadas.

Si existen incumplimientos, muestra los errores encontrados e impide ejecutar la clasificación experimental.

Si todas las validaciones se superan y el modelo está disponible, se presenta el resultado de la clasificación del Árbol de Decisión:

- Aceptado.
- Rechazado.

La predicción tiene una finalidad exclusivamente académica y experimental.

### 6.4. Instalación, generación de resultados y ejecución

Para ejecutar SmartPay desde una descarga nueva del repositorio, es necesario generar localmente el dataset, los archivos procesados y el modelo. Estos artefactos no se publican porque están excluidos del control de versiones mediante `.gitignore`.

Los comandos deben ejecutarse desde la carpeta raíz del proyecto y en el siguiente orden.

**Paso 1. Instalar las dependencias**

```bash
python -m pip install -r requirements.txt
```

**Paso 2. Generar el dataset sintético**

```bash
python src/generar_dataset.py
```

**Paso 3. Explorar el dataset y generar las gráficas descriptivas**

```bash
python src/exploracion.py
```

**Paso 4. Realizar el preprocesamiento de los datos**

```bash
python src/preprocesamiento.py
```

**Paso 5. Entrenar el modelo de Machine Learning**

```bash
python src/entrenamiento.py
```

**Paso 6. Evaluar el modelo y generar sus métricas y matriz de confusión**

```bash
python src/evaluacion.py
```

**Paso 7. Comparar el Árbol de Decisión con el modelo Baseline**

```bash
python src/comparacion_baseline.py
```

**Paso 8. Ejecutar la aplicación web**

```bash
python -m streamlit run src/aplicacion.py
```

Streamlit iniciará un servidor local y mostrará la dirección para abrir SmartPay en el navegador.

**Nota:** Los archivos generados se almacenan localmente. Por ello, al descargar el repositorio por primera vez se deben ejecutar los pasos anteriores antes de abrir la aplicación. Si únicamente se desea ejecutar la aplicación y ya existen el dataset procesado y el modelo, basta con ejecutar el comando del paso 8.

### 6.5. Ejecución de pruebas automatizadas

Para ejecutar las pruebas automatizadas de validación, utilizar el siguiente comando desde la carpeta raíz:

```bash
python src/test_validaciones.py
```

La última ejecución registrada reportó 24 pruebas exitosas y ningún error.

## 7. Estructura del proyecto

```text
SmartPay/
│
├── data/
│   ├── raw/
│   │   └── solicitudes_smartpay.csv
│   │
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── docs/
│   ├── 01_dataset.md
│   ├── 02_modelo_y_resultados.md
│   ├── 03_arquitectura_c4.md
│   ├── 04_adr.md
│   ├── 05_riesgos.md
│   ├── 06_analisis_etico.md
│   ├── 07_glosario_referencias.md
│   └── 08_revision_requisitos.md
│
├── models/
│   └── arbol_decision_smartpay.joblib
│
├── reports/
│   ├── evidencias/
│   ├── graficas/
│   └── metricas/
│
├── src/
│   ├── aplicacion.py
│   ├── comparacion_baseline.py
│   ├── entrenamiento.py
│   ├── evaluacion.py
│   ├── exploracion.py
│   ├── generar_dataset.py
│   ├── preprocesamiento.py
│   ├── prueba_validaciones.py
│   ├── test_validaciones.py
│   └── validaciones.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

**Nota:** La estructura representa la organización del proyecto. Los archivos de datos, modelos y resultados que se generan durante la ejecución pueden no encontrarse publicados en GitHub, debido a las reglas establecidas en `.gitignore`. Estos archivos se pueden regenerar mediante los scripts correspondientes.

## 8. Dataset utilizado

El dataset fue generado mediante Python y contiene registros ficticios de solicitudes de aplicación de pagos de cartera.

| Característica | Descripción |
|---|---|
| Archivo | `solicitudes_smartpay.csv` |
| Ubicación | `data/raw/` |
| Registros | 2.000 |
| Variables originales | 17 |
| Solicitudes aceptadas | 1.000 |
| Solicitudes rechazadas | 1.000 |
| Valores faltantes observados | 0 |
| Filas duplicadas observadas | 0 |

Después del preprocesamiento se obtuvieron 19 variables predictoras, incluyendo variables categóricas codificadas e indicadores derivados de la longitud válida de cuenta y crédito.

### 8.1. Muestra de registros del dataset

La siguiente tabla presenta cuatro registros de ejemplo tomados del archivo sintético `data/raw/solicitudes_smartpay.csv`. Los identificadores y valores son ficticios y se muestran únicamente con fines académicos.

| ID solicitud | Tipo de operación | Valor del pago | Valor de referencia | Saldo disponible | Resultado |
|---|---|---:|---:|---:|---|
| SP0454 | Abono a capital | 3.726.000 | Capital pendiente: 4.674.000 | 4.389.000 | Aceptado |
| SP0389 | Pago de cuota | 203.000 | Cuota pendiente: 203.000 | 653.000 | Aceptado |
| SP0636 | Pago de cuota | 743.000 | Cuota pendiente: 743.000 | 1.359.000 | Aceptado |
| SP1909 | Abono a intereses | 270.000 | Intereses pendientes: 415.000 | 269.000 | Rechazado |

En el último registro, el saldo disponible es inferior al valor del pago, por lo que la solicitud se clasifica como rechazada por saldo insuficiente. La muestra permite observar cómo se relacionan algunos campos de entrada con el resultado registrado.

### 8.2. Distribución de los datos

La división utilizada fue estratificada:

| Conjunto | Registros | Porcentaje |
|---|---:|---:|
| Entrenamiento | 1.600 | 80 % |
| Prueba | 400 | 20 % |
| Total | 2.000 | 100 % |

La variable objetivo es `resultado_procesamiento`, con las siguientes clases:

- `Aceptado`: 1.
- `Rechazado`: 0.

La información detallada sobre las variables, su descripción y el proceso de generación se encuentra en `docs/01_dataset.md`.

## 9. Modelo de Machine Learning y resultados

Se implementó un modelo de clasificación supervisada basado en un Árbol de Decisión (`DecisionTreeClassifier`).

### 9.1. Justificación del modelo

Se seleccionó el Árbol de Decisión porque permite representar reglas de clasificación mediante condiciones comprensibles y facilita la interpretación de los resultados.

Es un modelo adecuado para el ejercicio académico porque permite trabajar con variables numéricas y categóricas previamente codificadas, además de visualizar su estructura de decisión.

### 9.2. Configuración del modelo

| Parámetro | Valor |
|---|---|
| Modelo | DecisionTreeClassifier |
| Criterio | Gini |
| Profundidad máxima | 8 |
| Mínimo de muestras por hoja | 5 |
| Semilla aleatoria | 42 |

### 9.3. Resultados del entrenamiento

- Registros de entrenamiento: 1.600.
- Variables predictoras: 19.
- Exactitud sobre entrenamiento: 81,81 %.
- Profundidad obtenida del árbol: 8.
- Número de hojas: 29.

### 9.4. Métricas de evaluación

Los resultados obtenidos sobre el conjunto de prueba fueron:

| Métrica | Resultado |
|---|---:|
| Accuracy | 81,00 % |
| Precision (Rechazado) | 84,83 % |
| Recall (Rechazado) | 75,50 % |
| F1-score (Rechazado) | 79,89 % |

**Interpretación:**

- Accuracy: el modelo clasificó correctamente el 81 % de las solicitudes de prueba.
- Precision: de las solicitudes que el modelo clasificó como rechazadas, el 84,83 % realmente pertenecían a esa clase.
- Recall: identificó el 75,50 % de las solicitudes que realmente eran rechazadas.
- F1-score: representa el equilibrio entre Precision y Recall para la clase Rechazado.

### 9.5. Matriz de confusión

El orden de las clases es `Rechazado (0)` y `Aceptado (1)`.

| Real / Predicho | Rechazado | Aceptado |
|---|---:|---:|
| Rechazado | 151 | 49 |
| Aceptado | 27 | 173 |

Interpretación de los resultados:

- Verdaderos positivos (TP): 151 solicitudes rechazadas identificadas correctamente.
- Falsos negativos (FN): 49 solicitudes rechazadas clasificadas incorrectamente como aceptadas.
- Falsos positivos (FP): 27 solicitudes aceptadas clasificadas incorrectamente como rechazadas.
- Verdaderos negativos (TN): 173 solicitudes aceptadas identificadas correctamente.

Los 49 falsos negativos evidencian la importancia de mantener las validaciones de negocio como controles obligatorios e independientes de la predicción.

## 10. Comparación con un modelo de referencia (Baseline)

Para determinar si el Árbol de Decisión aporta una mejora frente a una estrategia básica, se implementó un modelo de referencia utilizando `DummyClassifier` de scikit-learn, con la estrategia `most_frequent`.

Este algoritmo predice siempre la clase más frecuente observada durante el entrenamiento, sin aprender relaciones entre las variables predictoras.

La comparación se realizó utilizando los mismos conjuntos de entrenamiento y prueba: 1.600 registros para entrenamiento y 400 para evaluación.

### 10.1. Resultados comparativos

| Métrica | Árbol de Decisión | Baseline |
|---|---:|---:|
| Accuracy | 81,00 % | 50,00 % |
| Precision (Rechazado) | 84,83 % | 50,00 % |
| Recall (Rechazado) | 75,50 % | 100,00 % |
| F1-score (Rechazado) | 79,89 % | 66,67 % |

### 10.2. Interpretación

El Árbol de Decisión obtuvo un Accuracy del 81 %, superior al 50 % alcanzado por el modelo Baseline. Esto representa una diferencia de 31 puntos porcentuales.

El Baseline alcanzó un Recall del 100 % para la clase Rechazado porque clasificó todas las solicitudes como rechazadas. Sin embargo, también clasificó incorrectamente las 200 solicitudes que realmente eran aceptadas.

Por su parte, el Árbol de Decisión logró identificar ambas categorías y obtuvo mejores resultados generales de clasificación.

La comparación evidencia que el Árbol de Decisión aprende patrones presentes en el dataset sintético y ofrece una clasificación más equilibrada que la estrategia básica de referencia.

### 10.3. Evidencias de la comparación

Los resultados se encuentran en:

- `reports/metricas/comparacion_modelos.csv`
- `reports/graficas/matriz_confusion_baseline.png`

El código de comparación se encuentra en `src/comparacion_baseline.py`.

## 11. Criterios de aceptación académicos

Para evaluar el resultado del ejercicio se establecieron los siguientes criterios:

1. El Árbol de Decisión debe superar el Accuracy del modelo Baseline utilizando la misma partición de prueba.
2. El modelo debe alcanzar un Recall mínimo del 75 % para la clase Rechazado, como umbral académico de evaluación.
3. Se deben presentar las métricas Accuracy, Precision, Recall y F1-score.
4. Se debe incluir e interpretar la matriz de confusión.
5. Se deben identificar los falsos negativos y falsos positivos.
6. Las reglas de negocio deben mantenerse independientes de la predicción del modelo.

El Árbol de Decisión cumplió los criterios cuantitativos establecidos: obtuvo 81 % de Accuracy frente al 50 % del Baseline y 75,50 % de Recall para la clase Rechazado.

Estos criterios son académicos y experimentales. No representan umbrales de autorización ni de seguridad para operaciones financieras reales.

## 12. Pruebas de validación

Se desarrollaron pruebas automatizadas para verificar el comportamiento de las funciones de validación del prototipo.

Las pruebas contemplan:

- Validación de números de cuenta y crédito.
- Comprobación de longitud de 11 dígitos.
- Rechazo de identificadores con longitud incorrecta.
- Rechazo de caracteres no numéricos.
- Validación de campos obligatorios.
- Validación de valores de pago positivos.
- Validación de los cuatro tipos de operación.

La última ejecución de las pruebas reportó:

| Indicador | Resultado |
|---|---:|
| Pruebas ejecutadas | 24 |
| Pruebas exitosas | 24 |
| Pruebas fallidas | 0 |
| Resultado | OK |

El código correspondiente se encuentra en:

- `src/test_validaciones.py`
- `src/validaciones.py`

Para ejecutar las pruebas:

```bash
python src/test_validaciones.py
```

## 13. Documentación adicional

La documentación técnica y académica se encuentra organizada en los siguientes archivos:

1. [Descripción del dataset y diccionario de datos](docs/01_dataset.md)
2. [Modelo de Machine Learning y resultados](docs/02_modelo_y_resultados.md)
3. [Arquitectura del sistema y diagrama C4](docs/03_arquitectura_c4.md)
4. [Decisiones de arquitectura (ADR)](docs/04_adr.md)
5. [Riesgos técnicos y mitigaciones](docs/05_riesgos.md)
6. [Análisis ético, sesgos, privacidad y equidad](docs/06_analisis_etico.md)
7. [Glosario y referencias](docs/07_glosario_referencias.md)
8. [Revisión de requisitos y estado del proyecto](docs/08_revision_requisitos.md)

Las evidencias gráficas se encuentran organizadas en las carpetas `reports/evidencias/`, `reports/graficas/` y `reports/metricas/`, según los archivos generados durante la ejecución.

## 14. Limitaciones y oportunidades de mejora

El proyecto cuenta con la generación del dataset sintético, validaciones de negocio, pruebas automatizadas, aplicación Streamlit, entrenamiento del Árbol de Decisión y comparación con un modelo Baseline.

Se identifican las siguientes limitaciones y oportunidades de mejora:

1. **Datos sintéticos:** los resultados corresponden a condiciones simuladas y no representan el comportamiento de una entidad financiera real.
2. **Generalización:** es necesario evaluar el modelo con nuevos escenarios y, si existe autorización, con datos representativos y protegidos.
3. **Validaciones:** se recomienda ampliar las pruebas para cubrir nuevos casos de negocio y situaciones excepcionales.
4. **Evaluación:** se debe prestar especial atención a los falsos negativos, es decir, solicitudes rechazadas que el modelo clasifica como aceptadas.
5. **Seguridad:** una futura implementación requeriría autenticación, autorización, trazabilidad y controles de protección de información.
6. **Integración:** la conexión con sistemas bancarios o herramientas RPA, como Wolf, queda fuera del alcance de este prototipo.
7. **Monitoreo:** cualquier evolución del modelo requeriría seguimiento periódico de sus métricas y revisión de posibles sesgos.

## 15. Uso responsable y consideraciones éticas

SmartPay es un prototipo académico que utiliza exclusivamente datos sintéticos.

Ninguna predicción debe utilizarse para autorizar, rechazar o ejecutar una transacción financiera real.

Las reglas de negocio determinísticas son las responsables de verificar las condiciones de las solicitudes simuladas. El modelo tiene una finalidad experimental y no reemplaza los controles del proceso.

Una futura implementación requeriría datos representativos y autorizados, controles de seguridad, trazabilidad, evaluación independiente, supervisión humana y aprobación de las áreas responsables.

También sería necesario analizar posibles sesgos, garantizar un tratamiento equitativo de la información y mantener transparencia sobre los criterios de clasificación.

## 16. Repositorio y control de versiones

El proyecto se encuentra publicado en GitHub:

[SmartPay - Repositorio del proyecto](https://github.com/Lindorti/proyectoFinal_SmartPay)

Las ramas utilizadas son:

- `main`: rama principal del repositorio.
- `develop`: rama de consolidación del proyecto.
- `dev_jcol_10`: rama individual de desarrollo.
- `feature/linda-dataset`: rama de trabajo anterior.
- `feature/linda-validaciones`: rama de trabajo anterior.

La consolidación del desarrollo individual se realizó mediante Pull Requests desde `dev_jcol_10` hacia `develop`.

Los cambios del proyecto se registraron mediante commits para conservar la trazabilidad del desarrollo.

## 17. Conclusiones

El desarrollo de SmartPay permitió aplicar los conceptos de preparación de datos, validación de información, entrenamiento y evaluación de modelos de Machine Learning en un escenario académico relacionado con solicitudes de aplicación de pagos de cartera.

La implementación del Árbol de Decisión permitió identificar patrones dentro del dataset sintético y obtener un Accuracy del 81 % sobre el conjunto de prueba, superando el resultado del modelo de referencia Baseline, que obtuvo un 50 %.

La aplicación desarrollada con Streamlit facilitó la interacción con el prototipo y permitió visualizar los resultados de las validaciones de negocio y la clasificación experimental.

La comparación de modelos, las pruebas automatizadas y el análisis de la matriz de confusión permitieron identificar fortalezas y oportunidades de mejora, especialmente frente a los falsos negativos.

Finalmente, se reconoce que el uso de datos sintéticos limita la generalización de los resultados. Por tanto, SmartPay constituye un ejercicio académico y no una solución lista para operar en un entorno financiero real.

## 18. Referencias y recursos técnicos

- Python Software Foundation. (s. f.). *Python documentation*. https://docs.python.org/3/
- pandas. (s. f.). *pandas documentation*. https://pandas.pydata.org/docs/
- NumPy. (s. f.). *NumPy documentation*. https://numpy.org/doc/
- Matplotlib. (s. f.). *Matplotlib documentation*. https://matplotlib.org/stable/
- scikit-learn. (s. f.). *scikit-learn documentation*. https://scikit-learn.org/stable/
- Streamlit. (s. f.). *Streamlit documentation*. https://docs.streamlit.io/
- Joblib. (s. f.). *Joblib documentation*. https://joblib.readthedocs.io/
- NumPy. (s. f.). *NumPy documentation*. https://numpy.org/doc/
- Git. (s. f.). *Git documentation*. https://git-scm.com/doc
- GitHub. (s. f.). *GitHub documentation*. https://docs.github.com/
- SmartPay. (2026). *Dataset sintético de solicitudes de aplicación de pagos de cartera* [Conjunto de datos generado mediante `src/generar_dataset.py`]. Elaboración propia.

Las referencias específicas sobre el modelo, los datos, las decisiones técnicas y el análisis ético se amplían en `docs/07_glosario_referencias.md`. La fecha del conjunto de datos corresponde al año de elaboración del proyecto; no representa una fuente externa.

---

**Autora:** Linda Ortiz  
**Proyecto:** SmartPay

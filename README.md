# SmartPay

## Sistema inteligente para el registro, validación y clasificación de solicitudes de aplicación de pagos de cartera de créditos

**Autora:** Linda Ortiz  
**Repositorio:** `proyectoFinal_SmartPay`  
**Rama individual de trabajo:** `dev_jcol_10`  
**Tipo de proyecto:** Prototipo académico de Machine Learning.

## 1. Descripción del proyecto

SmartPay es un prototipo académico que permite estudiar el registro, la validación y la clasificación de solicitudes simuladas de aplicación de pagos de cartera de créditos.

La solución combina reglas de negocio con un modelo de Machine Learning basado en un Árbol de Decisión, con el propósito de identificar patrones asociados con solicitudes aceptadas y rechazadas.

El proyecto utiliza exclusivamente datos sintéticos. No se conecta a sistemas bancarios reales, no consulta saldos reales, no ejecuta débitos, no aplica pagos y no se integra con Wolf ni con herramientas RPA productivas.

## 2. Problema que aborda

Una solicitud de aplicación de pago puede presentar inconsistencias que impiden su procesamiento, como:

- Datos obligatorios incompletos.
- Números de cuenta o crédito que no contienen exactamente once dígitos numéricos.
- Cuentas inactivas.
- Créditos cancelados.
- Relación incorrecta entre el crédito y el NIT.
- Saldo disponible insuficiente.
- Valores incompatibles con el tipo de operación solicitado.

SmartPay representa estas situaciones mediante datos ficticios y reglas de negocio simuladas para estudiar su validación y clasificación.

## 3. Objetivos

### Objetivo general

Desarrollar un prototipo académico que permita validar y clasificar solicitudes sintéticas de aplicación de pagos de cartera de créditos mediante reglas de negocio y un modelo de Machine Learning.

### Objetivos específicos

- Generar un dataset sintético que represente diferentes escenarios de solicitudes.
- Implementar validaciones para los campos y las condiciones de las operaciones.
- Preparar los datos para el entrenamiento del modelo.
- Entrenar un Árbol de Decisión para clasificar las solicitudes.
- Evaluar el modelo mediante métricas de clasificación y matriz de confusión.
- Documentar los resultados, las limitaciones y los aspectos éticos del prototipo.

## 4. Alcance funcional

### Funcionalidades contempladas

- Validación de campos obligatorios.
- Validación de números de cuenta y crédito con exactamente once dígitos numéricos.
- Validación de valores según el tipo de operación: pago de cuota, abono a capital, abono a intereses y pago total.
- Simulación de condiciones de cuentas y créditos mediante datos sintéticos.
- Generación y exploración de un dataset sintético.
- Preprocesamiento de variables.
- Entrenamiento y evaluación experimental de un Árbol de Decisión.

### Funcionalidades fuera del alcance

- Conexión con bases de datos o sistemas bancarios productivos.
- Consulta de información real de clientes, cuentas o créditos.
- Débitos, movimientos de dinero o aplicación efectiva de pagos.
- Integración operativa con Wolf o herramientas RPA.
- Autorización automática de operaciones mediante predicciones de Machine Learning.

**Principio de funcionamiento:** las reglas de negocio son los controles principales. La predicción del modelo tiene carácter experimental y no sustituye las validaciones determinísticas.

## 5. Tecnologías utilizadas

| Tecnología | Utilización |
|---|---|
| Python | Lenguaje principal de desarrollo. |
| Pandas | Manipulación y organización de datos. |
| NumPy | Procesamiento numérico. |
| scikit-learn | Preprocesamiento, entrenamiento y evaluación del modelo. |
| Matplotlib | Generación de visualizaciones. |
| Joblib | Serialización del modelo entrenado. |
| Git y GitHub | Control de versiones y gestión del repositorio. |
| Visual Studio Code | Entorno de desarrollo. |

## 6. Estructura del proyecto

```text
SmartPay/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── 01_dataset.md
│   ├── 02_modelo_y_resultados.md
│   ├── 03_arquitectura_c4.md
│   ├── 04_adr.md
│   ├── 05_riesgos.md
│   ├── 06_analisis_etico.md
│   ├── 07_glosario_referencias.md
│   └── 08_revision_requisitos.md
├── models/
├── reports/
│   ├── evidencias/
│   ├── graficas/
│   └── metricas/
├── src/
│   ├── aplicacion.py
│   ├── entrenamiento.py
│   ├── evaluacion.py
│   ├── exploracion.py
│   ├── generar_dataset.py
│   ├── preprocesamiento.py
│   ├── prueba_validaciones.py
│   └── validaciones.py
├── .gitignore
├── README.md
└── requirements.txt
```

La estructura representa la organización del proyecto. Los archivos generados durante la ejecución, como los datos procesados y el modelo serializado, pueden estar excluidos del control de versiones mediante `.gitignore`.

## 7. Instalación y ejecución

Para ejecutar el proyecto se requiere Python y las dependencias especificadas en `requirements.txt`.

Desde la carpeta raíz de SmartPay:

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar las validaciones

```bash
python src/prueba_validaciones.py
```

### Generar el dataset sintético

```bash
python src/generar_dataset.py
```

### Explorar los datos

```bash
python src/exploracion.py
```

### Preprocesar los datos

```bash
python src/preprocesamiento.py
```

### Entrenar el modelo

```bash
python src/entrenamiento.py
```

### Evaluar el modelo

```bash
python src/evaluacion.py
```

**Importante:** ejecutar el generador antes de la exploración y el preprocesamiento, ya que estos procesos utilizan el archivo CSV generado.

Los comandos corresponden al flujo de trabajo documentado. La ejecución completa desde una instalación limpia debe verificarse antes de la entrega final.

## 8. Dataset utilizado

El dataset se genera mediante Python y contiene registros ficticios de solicitudes de aplicación de pagos.

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

Después del preprocesamiento se obtuvieron 19 columnas predictoras, incluyendo variables codificadas y dos indicadores derivados de la longitud válida de cuenta y crédito.

La división utilizada fue estratificada:

| Conjunto | Registros | Porcentaje |
|---|---:|---:|
| Entrenamiento | 1.600 | 80 % |
| Prueba | 400 | 20 % |
| **Total** | **2.000** | **100 %** |

La información detallada sobre el origen, las variables y el procesamiento se encuentra en `docs/01_dataset.md`.

## 9. Modelo y resultados

Se implementó un modelo de clasificación supervisada basado en un Árbol de Decisión (`DecisionTreeClassifier`).

La configuración utilizada fue:

| Parámetro | Valor |
|---|---|
| Criterio | Gini |
| Profundidad máxima | 8 |
| Mínimo de muestras por hoja | 5 |
| Semilla aleatoria | 42 |

### Métricas de evaluación

Los resultados obtenidos sobre el conjunto de prueba fueron:

| Métrica | Resultado |
|---|---:|
| Accuracy | 81,00 % |
| Precision (Rechazado) | 84,83 % |
| Recall (Rechazado) | 75,50 % |
| F1-score (Rechazado) | 79,89 % |

### Matriz de confusión

Orden de las clases: Rechazado (0) y Aceptado (1).

| Real / Predicho | Rechazado | Aceptado |
|---|---:|---:|
| Rechazado | 151 | 49 |
| Aceptado | 27 | 173 |

Los 49 falsos negativos representan solicitudes realmente rechazadas que el modelo clasificó como aceptadas. Este resultado evidencia la importancia de mantener las validaciones de negocio como controles obligatorios.

Estos resultados describen únicamente el comportamiento del modelo sobre datos sintéticos. No representan ni garantizan su desempeño en una entidad financiera real.

## 10. Documentación adicional

La documentación técnica y académica se encuentra organizada en los siguientes archivos:

- [Descripción del dataset y diccionario de datos](docs/01_dataset.md).
- [Modelo de Machine Learning y resultados](docs/02_modelo_y_resultados.md).
- [Arquitectura del sistema y diagrama C4](docs/03_arquitectura_c4.md).
- [Decisiones de arquitectura (ADR)](docs/04_adr.md).
- [Riesgos técnicos y mitigaciones](docs/05_riesgos.md).
- [Análisis ético, sesgos, privacidad y uso responsable](docs/06_analisis_etico.md).
- [Glosario y referencias](docs/07_glosario_referencias.md).
- [Revisión de requisitos y estado del proyecto](docs/08_revision_requisitos.md).

Las evidencias gráficas y métricas se organizan en `reports/`.

## 11. Limitaciones y trabajo pendiente

El proyecto presenta las siguientes limitaciones y actividades de mejora:

1. **Comparación con baseline:** implementar `DummyClassifier` y comparar sus resultados con el Árbol de Decisión utilizando la misma partición de prueba.
2. **Pruebas automatizadas:** fortalecer las pruebas de las reglas de validación, incluyendo los cuatro tipos de operación y los números de cuenta y crédito de 11 dígitos.
3. **Criterios de aceptación:** establecer criterios verificables para evaluar el funcionamiento del prototipo y el desempeño del modelo.
4. **Aplicación:** verificar el estado de `aplicacion.py`. No se considera una interfaz terminada hasta que esté implementada y probada.
5. **Reproducibilidad:** comprobar las dependencias y la ejecución del proyecto desde una instalación limpia.
6. **Integración en GitHub:** completar la consolidación de los cambios desde `dev_jcol_10` hacia `develop`.

## 12. Uso responsable y consideraciones éticas

SmartPay es un prototipo académico que utiliza exclusivamente datos sintéticos.

Ninguna predicción debe utilizarse para autorizar, rechazar o ejecutar una transacción financiera real.

Una futura implementación requeriría datos representativos y autorizados, controles de seguridad, trazabilidad, evaluación independiente, supervisión humana y aprobación de las áreas responsables.

## 13. Repositorio y control de versiones

El proyecto se encuentra alojado en GitHub:

[proyectoFinal_SmartPay](https://github.com/Lindorti/proyectoFinal_SmartPay)

La rama individual de desarrollo utilizada es `dev_jcol_10`. Los cambios se consolidarán en la rama `develop`, de acuerdo con las instrucciones académicas.


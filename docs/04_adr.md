# 04. Registro de decisiones de arquitectura (ADR)

## 1. Introducción

El proyecto SmartPay, denominado *Sistema inteligente para el registro, validación y clasificación de solicitudes de aplicación de pagos de cartera de créditos*, requiere decisiones técnicas que permitan organizar el desarrollo, procesar datos sintéticos y evaluar un modelo de Machine Learning.

Este documento registra las principales decisiones de arquitectura, sus justificaciones, ventajas y limitaciones.

## ADR-001. Utilización de Python como lenguaje principal

**Estado:** Aceptada.

**Contexto:** El proyecto requiere generar datos sintéticos, implementar validaciones, preparar información y entrenar un modelo de clasificación.

**Decisión:** Utilizar Python como lenguaje principal de desarrollo, apoyándose en bibliotecas como Pandas y scikit-learn.

**Justificación:** Python facilita el procesamiento de datos y dispone de herramientas para construir y evaluar modelos de aprendizaje automático.

**Consecuencias:** Permite organizar el desarrollo mediante scripts independientes y ejecutar experimentos reproducibles. Requiere instalar y administrar correctamente las dependencias.

## ADR-002. Selección del Árbol de Decisión

**Estado:** Aceptada.

**Contexto:** SmartPay necesita clasificar solicitudes simuladas en Aceptado o Rechazado utilizando variables numéricas y categóricas.

**Decisión:** Implementar un modelo de clasificación supervisada basado en un Árbol de Decisión.

**Justificación:** Este algoritmo permite trabajar con diferentes características de las solicitudes y facilita la interpretación de las condiciones que influyen en sus predicciones.

**Consecuencias:** El modelo puede visualizarse y evaluarse mediante métricas de clasificación. Sin embargo, puede presentar sobreajuste y errores de clasificación, por lo que necesita validación y comparación con un modelo de referencia.

## ADR-003. Utilización de datos sintéticos

**Estado:** Aceptada.

**Contexto:** El proyecto aborda un proceso financiero que normalmente involucra información confidencial de clientes, cuentas y créditos.

**Decisión:** Construir un dataset completamente sintético mediante un generador desarrollado en Python.

**Justificación:** Permite representar escenarios de negocio y desarrollar el ejercicio académico sin utilizar información real ni comprometer la privacidad de los clientes.

**Consecuencias:** Facilita las pruebas y el control de escenarios. No obstante, los patrones aprendidos por el modelo pueden no representar el comportamiento de solicitudes reales.

## ADR-004. Almacenamiento local mediante archivos

**Estado:** Aceptada para el prototipo académico.

**Contexto:** El proyecto necesita almacenar solicitudes simuladas, datos procesados, modelos entrenados y resultados de evaluación.

**Decisión:** Utilizar archivos CSV para los datos, archivos Joblib para el modelo entrenado y archivos CSV y PNG para las métricas y gráficos.

**Justificación:** Esta alternativa es sencilla, facilita la reproducción de los experimentos y evita incorporar una base de datos que no es necesaria para el alcance actual.

**Consecuencias:** Reduce la complejidad del prototipo, pero no proporciona las capacidades de concurrencia, auditoría y administración de datos que exigiría un sistema financiero productivo.

## ADR-005. Separación entre reglas de negocio y Machine Learning

**Estado:** Aceptada.

**Contexto:** Una predicción incorrecta podría clasificar como aceptada una solicitud que incumple condiciones importantes.

**Decisión:** Mantener las validaciones determinísticas como controles independientes del modelo de Machine Learning.

**Justificación:** Las reglas sobre longitud de cuenta y crédito, estados, saldos y valores de las operaciones deben verificarse explícitamente. Una predicción estadística no puede sustituirlas.

**Consecuencias:** Mejora la claridad del diseño y permite identificar errores de forma controlada. El modelo se utiliza únicamente para clasificación experimental y no para autorizar operaciones financieras.

## ADR-006. Ejecución local sin integración bancaria

**Estado:** Aceptada para el alcance académico.

**Contexto:** La integración con plataformas bancarias y herramientas de automatización requeriría accesos, permisos, controles de seguridad y pruebas adicionales.

**Decisión:** Desarrollar y evaluar SmartPay localmente, sin conexión a sistemas bancarios de producción ni ejecución de procesos RPA.

**Justificación:** Permite concentrar el proyecto en la validación de datos, el entrenamiento del modelo y la evaluación de resultados.

**Consecuencias:** El prototipo no realiza pagos, débitos ni modificaciones de cuentas o créditos. Una integración futura deberá diseñarse y aprobarse por separado.

## 2. Conclusión

Las decisiones de arquitectura de SmartPay priorizan la simplicidad, la reproducibilidad, la protección de la información y la interpretación de los resultados.

La selección de Python, el Árbol de Decisión, los datos sintéticos y el almacenamiento local responde a los objetivos académicos del proyecto.

La separación entre reglas determinísticas y predicciones de Machine Learning permite delimitar las responsabilidades del sistema y evitar que una clasificación experimental se interprete como autorización de una operación financiera.
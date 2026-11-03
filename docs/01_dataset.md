# 01. Descripción del dataset y diccionario de datos

## 1. Introducción

El proyecto SmartPay utiliza un conjunto de datos sintéticos diseñado para simular solicitudes de aplicación de pagos de cartera de créditos. Este dataset permite desarrollar, entrenar y evaluar un modelo de Machine Learning orientado a clasificar las solicitudes en dos categorías: Aceptado y Rechazado.

Los registros fueron generados mediante un script en Python denominado `generar_dataset.py`, utilizando la biblioteca Pandas para organizar la información y almacenarla en formato CSV.

Los datos son completamente ficticios y se utilizan exclusivamente con fines académicos. No representan clientes, cuentas, créditos ni operaciones financieras reales.

## 2. Características generales del dataset

El archivo utilizado se encuentra en la siguiente ruta:

`data/raw/solicitudes_smartpay.csv`

Sus principales características son:

| Característica | Descripción |
|---|---|
| Nombre del archivo | solicitudes_smartpay.csv |
| Formato | CSV |
| Cantidad de registros | 2.000 solicitudes |
| Cantidad de variables | 17 |
| Registros aceptados | 1.000 |
| Registros rechazados | 1.000 |
| Valores faltantes | 0 |
| Registros duplicados | 0 |
| Origen | Generación sintética mediante Python |
| Codificación | UTF-8 con BOM |

La distribución equilibrada entre solicitudes aceptadas y rechazadas facilita el desarrollo del ejercicio de clasificación. Sin embargo, no representa necesariamente la proporción de resultados de un proceso financiero real.

## 3. Objetivo del dataset

El objetivo principal es proporcionar información simulada que permita identificar las condiciones asociadas con la aceptación o el rechazo de una solicitud de aplicación de pagos.

La variable objetivo es:

`resultado_procesamiento`

Esta variable contiene dos categorías:

- **Aceptado:** solicitud que cumple las condiciones establecidas en las reglas de negocio simuladas.
- **Rechazado:** solicitud que incumple al menos una de las condiciones definidas.

Para el entrenamiento del modelo, la variable objetivo se transforma a valores numéricos:

| Categoría original | Valor numérico |
|---|---:|
| Rechazado | 0 |
| Aceptado | 1 |

## 4. Diccionario de variables

El dataset contiene 17 variables, organizadas de la siguiente manera:

| Variable | Descripción | Tipo de dato |
|---|---|---|
| id_solicitud | Identificador ficticio de cada solicitud. | Texto |
| nit | Identificador tributario ficticio del cliente. | Numérico |
| numero_cuenta | Número ficticio de la cuenta asociada a la solicitud. | Numérico |
| numero_credito | Número ficticio del crédito relacionado con el pago. | Numérico |
| tipo_cuenta | Tipo de cuenta: Ahorros o Corriente. | Categórico |
| tipo_operacion | Operación solicitada: Pago de cuota, Abono a capital, Abono a intereses o Pago total. | Categórico |
| valor_pago | Valor que se desea aplicar a la operación. | Numérico |
| cuota_pendiente | Valor pendiente de la cuota del crédito. | Numérico |
| capital_pendiente | Saldo de capital pendiente. | Numérico |
| intereses_pendientes | Valor de intereses pendientes. | Numérico |
| valor_liquidacion | Valor total simulado para la liquidación del crédito. | Numérico |
| estado_cuenta | Estado de la cuenta: Activa o Inactiva. | Categórico |
| saldo_disponible | Saldo disponible simulado de la cuenta. | Numérico |
| estado_credito | Estado del crédito: Vigente o Cancelado. | Categórico |
| credito_corresponde_nit | Indica si el crédito corresponde al NIT registrado. | Booleano |
| motivo_rechazo | Motivo simulado por el cual se rechaza una solicitud. | Categórico |
| resultado_procesamiento | Resultado final de la solicitud: Aceptado o Rechazado. | Categórico |

## 5. Variables predictoras y variable objetivo

Para el entrenamiento del modelo se seleccionaron inicialmente las siguientes variables predictoras:

- tipo_cuenta
- tipo_operacion
- valor_pago
- cuota_pendiente
- capital_pendiente
- intereses_pendientes
- valor_liquidacion
- estado_cuenta
- saldo_disponible
- estado_credito
- credito_corresponde_nit

Adicionalmente, el proceso de preprocesamiento genera dos variables derivadas:

- **cuenta_longitud_valida:** indica si el número de cuenta contiene exactamente once dígitos numéricos.
- **credito_longitud_valida:** indica si el número de crédito contiene exactamente once dígitos numéricos.

La variable objetivo utilizada es `resultado_procesamiento`.

Las variables `id_solicitud`, `nit` y `motivo_rechazo` no se incluyen directamente como predictores del modelo. Los identificadores no aportan una característica de negocio necesaria para la clasificación, mientras que `motivo_rechazo` describe una razón asociada al resultado y su inclusión podría generar fuga de información.

## 6. Distribución de las solicitudes

El dataset está compuesto por 2.000 registros, distribuidos de manera equilibrada:

| Resultado | Cantidad | Porcentaje |
|---|---:|---:|
| Aceptado | 1.000 | 50 % |
| Rechazado | 1.000 | 50 % |
| **Total** | **2.000** | **100 %** |

Esta distribución permite trabajar con ambas categorías durante el entrenamiento y la evaluación del modelo.

## 7. Distribución por tipo de operación

Las solicitudes se distribuyen entre cuatro tipos de operación:

| Tipo de operación | Cantidad |
|---|---:|
| Abono a capital | 514 |
| Abono a intereses | 513 |
| Pago de cuota | 500 |
| Pago total | 473 |
| **Total** | **2.000** |

La distribución muestra que los cuatro tipos de operación tienen una representación relativamente equilibrada dentro del conjunto de datos.

## 8. Motivos de rechazo simulados

El generador contempla siete posibles motivos de rechazo:

- Cuenta con longitud incorrecta.
- Crédito con longitud incorrecta.
- Cuenta inactiva.
- Saldo insuficiente.
- Crédito cancelado.
- Crédito no corresponde al NIT.
- Valor de operación incorrecto.

Estos motivos se generan mediante alteraciones controladas de las condiciones de cada solicitud. El resultado final se determina evaluando las reglas de negocio implementadas en el generador.

Es importante aclarar que el motivo registrado es una variable descriptiva del resultado y no se utiliza como predictor del modelo.

## 9. Reglas de negocio representadas en los datos

El dataset simula las siguientes validaciones:

1. El número de cuenta debe contener exactamente once dígitos numéricos.
2. El número de crédito debe contener exactamente once dígitos numéricos.
3. La cuenta debe encontrarse activa.
4. El saldo disponible debe ser igual o superior al valor del pago.
5. El crédito debe encontrarse vigente.
6. El crédito debe corresponder al NIT registrado.
7. El valor de la operación debe cumplir las condiciones correspondientes al tipo de pago.

Las reglas específicas de los valores son:

| Tipo de operación | Condición simulada |
|---|---|
| Pago de cuota | El valor debe ser igual a la cuota pendiente. |
| Abono a capital | El valor debe ser mayor que cero y no superar el capital pendiente. |
| Abono a intereses | El valor debe ser mayor que cero y no superar los intereses pendientes. |
| Pago total | El valor debe ser igual al valor de liquidación. |

## 10. Preprocesamiento de los datos

El archivo `preprocesamiento.py` realiza las siguientes actividades:

1. Carga el dataset desde `data/raw/solicitudes_smartpay.csv`.
2. Selecciona las variables predictoras y la variable objetivo.
3. Genera las variables derivadas para validar la longitud de las cuentas y los créditos.
4. Convierte la variable objetivo a valores numéricos: Rechazado = 0 y Aceptado = 1.
5. Aplica codificación One-Hot a las variables categóricas.
6. Convierte la variable booleana a formato numérico.
7. Divide los datos en conjuntos de entrenamiento y prueba.
8. Guarda los archivos procesados en `data/processed/`.

La división se realiza utilizando una proporción del 80 % para entrenamiento y 20 % para prueba, con `random_state=42` y estratificación de las clases.

| Conjunto | Registros | Porcentaje |
|---|---:|---:|
| Entrenamiento | 1.600 | 80 % |
| Prueba | 400 | 20 % |
| **Total** | **2.000** | **100 %** |

La estratificación permite conservar la proporción de las categorías de la variable objetivo en ambos conjuntos.

## 11. Consideraciones y limitaciones

El dataset presenta las siguientes limitaciones:

- Los datos fueron generados artificialmente y no proceden de operaciones financieras reales.
- Las reglas de generación determinan las condiciones que producen las etiquetas de aceptación y rechazo.
- La distribución equilibrada de las clases fue establecida para facilitar el ejercicio académico.
- Los resultados del modelo reflejan su capacidad para identificar patrones dentro de los datos simulados, pero no garantizan el mismo desempeño con información real.
- La presencia de variables relacionadas directamente con las reglas de generación puede facilitar que el modelo aprenda esos patrones sin que esto demuestre capacidad de generalización en un entorno real.

Por lo anterior, los resultados deben interpretarse como una evaluación experimental y académica.

## 12. Conclusión

El dataset de SmartPay constituye la base para desarrollar y evaluar un modelo de clasificación de solicitudes simuladas de aplicación de pagos de cartera de créditos.

Su estructura permite representar diferentes tipos de operación, condiciones de cuentas y créditos, valores pendientes y posibles motivos de rechazo. Además, facilita la aplicación de técnicas de preprocesamiento y entrenamiento mediante Machine Learning.

El uso de datos sintéticos permite desarrollar el prototipo sin comprometer información financiera o personal de clientes. No obstante, cualquier implementación futura requeriría datos representativos y autorizados, validaciones adicionales y una evaluación independiente antes de considerar su utilización en un entorno real.
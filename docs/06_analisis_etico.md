# 06. Análisis ético, sesgos, privacidad y uso responsable

## 1. Privacidad

El proyecto utiliza datos sintéticos. No se incorporan nombres, NIT, cuentas, créditos ni saldos reales de clientes. Los identificadores incluidos en el dataset son ficticios. Si en una etapa futura se utilizaran datos reales, sería indispensable contar con autorización, finalidad definida, controles de acceso, minimización, anonimización o seudonimización y cumplimiento de la normativa aplicable.

## 2. Posibles sesgos

El principal sesgo proviene de la forma en que se generaron los datos. Las reglas, las proporciones de aceptación/rechazo y la frecuencia de los motivos fueron definidas para el ejercicio. El modelo puede reproducir esos supuestos y no necesariamente patrones observados en una operación real.

También puede existir sesgo por cobertura si algunos tipos de operación o condiciones aparecen con mayor o menor frecuencia. La distribución equilibrada de aceptados y rechazados facilita el ejercicio, pero no necesariamente representa la frecuencia real de rechazos.

## 3. Equidad

No se evaluó equidad sobre grupos demográficos reales, porque el dataset no contiene atributos personales ni representa clientes reales. En una implementación futura se deberían definir grupos y métricas de equidad apropiadas, siempre que exista justificación legal y ética para tratar esos datos. No se deben inferir atributos sensibles.

## 4. Impacto social y operativo

Una herramienta de validación puede reducir errores de digitación y reprocesos si se diseña correctamente. Sin embargo, una clasificación errónea puede generar demoras, rechazos injustificados o falsa confianza. Por ello, la predicción no debe ser la única base de una decisión operativa.

## 5. Transparencia y supervisión humana

Las reglas de negocio deben ser visibles y explicables. El usuario debe conocer por qué una solicitud no cumple una regla. Las predicciones del modelo deben presentarse como una señal experimental, no como una decisión definitiva. Debe existir revisión humana y un mecanismo para corregir datos erróneos.

## 6. Interpretación responsable de los errores

En la prueba, 49 solicitudes realmente rechazadas fueron clasificadas como aceptadas (falsos negativos, considerando rechazo como clase positiva). Este error sería especialmente importante en un flujo real, por lo que el modelo no debe sustituir las validaciones de cuenta, crédito, saldo, relación NIT-crédito ni reglas de monto.

## 7. Conclusión ética

El prototipo es aceptable como ejercicio académico con datos sintéticos y alcance limitado. No sería responsable desplegarlo en un entorno financiero real sin datos representativos autorizados, evaluación independiente, pruebas de seguridad, auditoría, monitoreo, gestión de cambios, revisión humana y aprobación de las áreas responsables.
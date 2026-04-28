# Propuesta del Proyecto

## Problema
Los estudiantes de arquitectura de computadoras necesitan herramientas
prácticas para visualizar información del sistema y entender la
interacción entre software de alto nivel y hardware.

## Justificación
Este proyecto permite observar cómo Python interactúa con componentes
de bajo nivel, reforzando conceptos de arquitectura de computadoras.

## Alcance
- Reporte de información del CPU
- Reporte de memoria RAM disponible
- Reporte del sistema operativo
- Medición básica de rendimiento

## Arquitectura
- Capa alta: Python (interfaz y lógica principal)
- Capa media: C (bridge entre Python y Assembly)
- Capa baja: ARM64 Assembly (operaciones de bajo nivel)

## Riesgos
| Riesgo | Mitigación |
|--------|------------|
| Incompatibilidad ARM64 | Probar en entorno Linux ARM64 |
| Límites de Codex gratis | Prompts cortos y específicos |

## Supuestos
- Se usa Python 3.10 o superior
- El entorno es Linux con arquitectura ARM64

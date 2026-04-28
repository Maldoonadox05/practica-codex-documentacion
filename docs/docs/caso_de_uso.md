# Caso de Uso

## Actor Principal
Estudiante de arquitectura de computadoras

## Precondiciones
- Python 3.10 instalado
- Repositorio clonado correctamente

## Flujo Principal
1. El estudiante ejecuta `python src/main.py`
2. El sistema muestra el menú de opciones
3. El estudiante elige una opción
4. El sistema reporta la información solicitada
5. El estudiante puede elegir otra opción o salir

## Escenario Alterno 1 — Error de compilación
1. El estudiante ejecuta el programa
2. Falta una dependencia instalada
3. El sistema muestra mensaje de error claro
4. El estudiante instala la dependencia faltante
5. Reintenta la ejecución

## Escenario Alterno 2 — Arquitectura no compatible
1. El estudiante ejecuta en Windows o x86
2. El componente ARM64 no carga
3. El sistema continúa solo con Python
4. Se muestra advertencia de funcionalidad limitada

## Postcondiciones
- Se muestra la información del sistema correctamente
- El programa termina sin errores

## Criterios de Aceptación
- El menú debe mostrarse correctamente
- Cada opción debe retornar información válida
- El programa no debe cerrarse con errores inesperados

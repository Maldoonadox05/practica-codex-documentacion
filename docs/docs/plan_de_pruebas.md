# Plan de Pruebas

## Estrategia de Pruebas
Pruebas manuales funcionales ejecutadas directamente
en terminal verificando cada opción del menú.

## Casos de Prueba

| ID | Entrada | Resultado Esperado | Criterio de Éxito |
|----|---------|-------------------|-------------------|
| CP-01 | Ejecutar `python src/main.py` | Menú visible | Menú sin errores |
| CP-02 | Opción 1 (Info sistema) | Muestra OS y versión | Datos correctos |
| CP-03 | Opción 2 (Listar archivos) | Lista de archivos | Sin errores |
| CP-04 | Opción 3 (Salir) | Programa termina | Salida limpia |
| CP-05 | Opción inválida | Mensaje de error | No cierra el programa |

## Cobertura Mínima
- 100% de opciones del menú probadas
- Prueba de entrada inválida incluida
- Prueba de salida limpia incluida

## Criterios de Aprobación
- Todos los CP deben pasar sin errores
- El programa no debe cerrarse inesperadamente
- La información mostrada debe ser real y correcta

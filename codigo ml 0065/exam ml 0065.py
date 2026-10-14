# Nahum flores NC 0065

import os
import sys
import importlib.util
import pandas as pd

# 1. Obtener la ruta raíz del proyecto (un nivel arriba del script actual)
directorio_actual = os.path.dirname(__file__)
directorio_raiz = os.path.abspath(os.path.join(directorio_actual, '..'))

# 2. Buscar automáticamente la carpeta de datos de entrada
carpeta_datos = None
for elemento in os.listdir(directorio_raiz):
    ruta_posible = os.path.join(directorio_raiz, elemento)
    if os.path.isdir(ruta_posible) and elemento.lower().startswith('datos'):
        carpeta_datos = ruta_posible
        break

if not carpeta_datos:
    raise FileNotFoundError(
        f"No se encontró ninguna carpeta que comience con 'datos' en: {directorio_raiz}"
    )

# 3. Buscar automáticamente el archivo del diccionario dentro de la carpeta encontrada
archivo_dicc = None
for elemento in os.listdir(carpeta_datos):
    if elemento.lower().startswith('dicc') and elemento.endswith('.py'):
        archivo_dicc = os.path.join(carpeta_datos, elemento)
        break

if not archivo_dicc:
    raise FileNotFoundError(
        f"No se encontró ningún archivo .py que comience con 'dicc' en: {carpeta_datos}"
    )

# 4. Cargar el módulo dinámicamente
spec = importlib.util.spec_from_file_location("modulo_dicc", archivo_dicc)
dicc_modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_modulo)

# 5. Obtener la variable de datos
datos_ciudades = getattr(dicc_modulo, 'datos_ciudades', None)

if datos_ciudades is None:
    raise AttributeError("No se encontró la variable 'datos_ciudades' en el archivo del diccionario.")

# -------------------------------------------------------------------------
# PROCESAMIENTO Y ANÁLISIS DE DATOS
# -------------------------------------------------------------------------

df = pd.DataFrame(datos_ciudades)

print("=" * 55)
print("           DATAFRAME DE CIUDADES DE MÉXICO")
print("=" * 55)
print(df.to_string(index=True))

print("\n" + "=" * 55)
print("             ESTRUCTURA E INFORMACIÓN DEL DF")
print("=" * 55)
df.info()

print("\n" + "=" * 55)
print("              ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 55)
print(df.describe())

print("\n" + "=" * 55)
print("                 ANÁLISIS DE POBLACIÓN")
print("=" * 55)
poblacion_total = df["Poblacion"].sum()
poblacion_promedio = df["Poblacion"].mean()

print(f"Población total registrada : {poblacion_total:,} habitantes")
print(f"Población promedio         : {poblacion_promedio:,.2f} habitantes")

ciudad_max = df.loc[df["Poblacion"].idxmax()]
ciudad_min = df.loc[df["Poblacion"].idxmin()]

print(f"Ciudad más poblada         : {ciudad_max['Ciudad']} ({ciudad_max['Poblacion']:,} habs.)")
print(f"Ciudad menos poblada        : {ciudad_min['Ciudad']} ({ciudad_min['Poblacion']:,} habs.)")

print("\n" + "=" * 55)
print("        CIUDADES CON POBLACIÓN MAYOR A 1,000,000")
print("=" * 55)
df_filtrado = df[df["Poblacion"] > 1000000]
print(df_filtrado.to_string(index=False))
 
print("Nahum flores NC 0065")
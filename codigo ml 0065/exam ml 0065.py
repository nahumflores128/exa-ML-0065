
# Nahum Flores NC 0065

import os
import importlib.util
import io
import pandas as pd

# 1. Buscar la carpeta raíz del proyecto
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_raiz = os.path.abspath(
    os.path.join(directorio_actual, "..")
)

# 2. Buscar carpeta de datos
carpeta_datos = None

for elemento in os.listdir(directorio_raiz):
    ruta = os.path.join(directorio_raiz, elemento)

    if os.path.isdir(ruta) and elemento.lower().startswith("datos"):
        carpeta_datos = ruta
        break

if not carpeta_datos:
    raise FileNotFoundError("No se encontró la carpeta datos.")

# 3. Buscar archivo dicc
archivo_dicc = None

for elemento in os.listdir(carpeta_datos):
    if elemento.lower().startswith("dicc") and elemento.endswith(".py"):
        archivo_dicc = os.path.join(carpeta_datos, elemento)
        break

if not archivo_dicc:
    raise FileNotFoundError("No se encontró el archivo dicc.")

# 4. Cargar el diccionario
spec = importlib.util.spec_from_file_location(
    "modulo_dicc", archivo_dicc
)
dicc_modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_modulo)

datos_ciudades = getattr(dicc_modulo, "datos_ciudades", None)

if datos_ciudades is None:
    raise AttributeError("No existe la variable datos_ciudades.")

# 5. Crear el DataFrame
df = pd.DataFrame(datos_ciudades)

# 6. Crear el resultado en Markdown
resultado = []

resultado.append("# Análisis de ciudades de México")
resultado.append("")
resultado.append("**Alumno:** Nahum Flores")
resultado.append("**Número de control:** 0065")
resultado.append("")
resultado.append("## 1. Datos de las ciudades")
resultado.append("")

def crear_tabla(datos):
    datos = datos.fillna("").astype(str)
    encabezados = list(datos.columns)

    texto = "| " + " | ".join(encabezados) + " |"
    separador = "| " + " | ".join(["---"] * len(encabezados)) + " |"

    filas = [texto, separador]

    for _, fila in datos.iterrows():
        valores = [
            valor.replace("|", "\\|").replace("\n", " ")
            for valor in fila
        ]
        filas.append("| " + " | ".join(valores) + " |")

    return "\n".join(filas)

resultado.append(crear_tabla(df.reset_index(drop=True)))
resultado.append("")

# 7. Información del DataFrame
resultado.append("## 2. Estructura del DataFrame")
resultado.append("")

informacion = io.StringIO()
df.info(buf=informacion)

resultado.append("```text")
resultado.append(informacion.getvalue().strip())
resultado.append("```")
resultado.append("")

# 8. Estadísticas descriptivas
resultado.append("## 3. Estadísticas descriptivas")
resultado.append("")

estadisticas = df.describe().round(2).reset_index()
resultado.append(crear_tabla(estadisticas))
resultado.append("")

# 9. Análisis de población
resultado.append("## 4. Análisis de población")
resultado.append("")

poblacion_total = df["Poblacion"].sum()
poblacion_promedio = df["Poblacion"].mean()

ciudad_max = df.loc[df["Poblacion"].idxmax()]
ciudad_min = df.loc[df["Poblacion"].idxmin()]

resultado.append(
    f"- **Población total:** {poblacion_total:,.0f} habitantes"
)
resultado.append(
    f"- **Población promedio:** {poblacion_promedio:,.2f} habitantes"
)
resultado.append(
    f"- **Ciudad más poblada:** {ciudad_max['Ciudad']} "
    f"({ciudad_max['Poblacion']:,.0f} habitantes)"
)
resultado.append(
    f"- **Ciudad menos poblada:** {ciudad_min['Ciudad']} "
    f"({ciudad_min['Poblacion']:,.0f} habitantes)"
)
resultado.append("")

# 10. Ciudades con más de un millón de habitantes
resultado.append("## 5. Ciudades con más de 1,000,000 de habitantes")
resultado.append("")

df_filtrado = df[df["Poblacion"] > 1000000]
resultado.append(crear_tabla(df_filtrado.reset_index(drop=True)))
resultado.append("")
resultado.append("---")
resultado.append("*Reporte generado con Python y Pandas.*")

# 11. Guardar el resultado
carpeta_resultados = os.path.join(directorio_raiz, "resultados")
os.makedirs(carpeta_resultados, exist_ok=True)

archivo_resultado = os.path.join(
    carpeta_resultados, "resultado_ciudades.md"
)

with open(archivo_resultado, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(resultado))

print("Reporte generado correctamente.")
print(f"Archivo: {archivo_resultado}")
print("Nahum Flores NC 0065")

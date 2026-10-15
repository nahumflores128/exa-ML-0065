# Análisis de ciudades de México

**Alumno:** Nahum Flores
**Número de control:** 0065

## 1. Datos de las ciudades

| Ciudad | Estado | Poblacion |
| --- | --- | --- |
| Guadalajara | Jalisco | 1500000 |
| Monterrey | Nuevo León | 1100000 |
| Puebla | Puebla | 1600000 |
| Tijuana | Baja California | 1800000 |
| Mérida | Yucatán | 900000 |
| Cancún | Quintana Roo | 800000 |

## 2. Estructura del DataFrame

```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Ciudad     6 non-null      str  
 1   Estado     6 non-null      str  
 2   Poblacion  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes
```

## 3. Estadísticas descriptivas

| index | Poblacion |
| --- | --- |
| count | 6.0 |
| mean | 1283333.33 |
| std | 407021.7 |
| min | 800000.0 |
| 25% | 950000.0 |
| 50% | 1300000.0 |
| 75% | 1575000.0 |
| max | 1800000.0 |

## 4. Análisis de población

- **Población total:** 7,700,000 habitantes
- **Población promedio:** 1,283,333.33 habitantes
- **Ciudad más poblada:** Tijuana (1,800,000 habitantes)
- **Ciudad menos poblada:** Cancún (800,000 habitantes)

## 5. Ciudades con más de 1,000,000 de habitantes

| Ciudad | Estado | Poblacion |
| --- | --- | --- |
| Guadalajara | Jalisco | 1500000 |
| Monterrey | Nuevo León | 1100000 |
| Puebla | Puebla | 1600000 |
| Tijuana | Baja California | 1800000 |

---
*Reporte generado con Python y Pandas.*
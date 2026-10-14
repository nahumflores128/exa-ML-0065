=======================================================
           DATAFRAME DE CIUDADES DE MÉXICO
=======================================================
        Ciudad           Estado  Poblacion
0  Guadalajara          Jalisco    1500000
1    Monterrey       Nuevo León    1100000
2       Puebla           Puebla    1600000
3      Tijuana  Baja California    1800000
4       Mérida          Yucatán     900000
5       Cancún     Quintana Roo     800000

=======================================================
             ESTRUCTURA E INFORMACIÓN DEL DF
=======================================================
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

=======================================================
              ESTADÍSTICAS DESCRIPTIVAS
=======================================================
          Poblacion
count  6.000000e+00
mean   1.283333e+06
std    4.070217e+05
min    8.000000e+05
25%    9.500000e+05
50%    1.300000e+06
75%    1.575000e+06
max    1.800000e+06

=========================================


=======================================================
        CIUDADES CON POBLACIÓN MAYOR A 1,000,000
=======================================================
     Ciudad          Estado  Poblacion
Guadalajara         Jalisco    1500000
  Monterrey      Nuevo León    1100000
     Puebla          Puebla    1600000
    Tijuana Baja California    1800000
from gestion_archivos import *

lugares = [
    {"ciudad": "Madrid", "pais": "España", "edad": 34, "codigo": "A1b2C", "activo": True},
    {"ciudad": "París", "pais": "Francia", "edad": 27, "codigo": "X9y8Z", "activo": False},
    {"ciudad": "Londres", "pais": "Reino Unido", "edad": 42, "codigo": "K3l4M", "activo": True},
    {"ciudad": "Berlín", "pais": "Alemania", "edad": 31, "codigo": "Q7w8E", "activo": True},
    {"ciudad": "Roma", "pais": "Italia", "edad": 29, "codigo": "T1y2U", "activo": False},
    {"ciudad": "Lisboa", "pais": "Portugal", "edad": 38, "codigo": "R5t6Y", "activo": True},
    {"ciudad": "Buenos Aires", "pais": "Argentina", "edad": 45, "codigo": "M9n0B", "activo": False},
    {"ciudad": "Santiago", "pais": "Chile", "edad": 36, "codigo": "P2q3S", "activo": True},
    {"ciudad": "México DF", "pais": "México", "edad": 28, "codigo": "V7x8Z", "activo": True},
    {"ciudad": "Bogotá", "pais": "Colombia", "edad": 33, "codigo": "L4m5N", "activo": False}
]

nombre_fichero= "lugares.csv"
de_lista_a_csv(lugares, nombre_fichero)

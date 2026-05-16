# =========================================
# FUNCIONES DEL PROYECTO AQUALIMPIA
# Archivo: funciones.py
# =========================================

import numpy as np
import pandas as pd


# =========================================
# FUNCIÓN: CALCULAR EFICIENCIA
# =========================================

def calcular_eficiencia(dbo_entrada, dbo_salida):
    """
    Calcula la eficiencia del tratamiento
    de aguas residuales.
    """

    eficiencia = (
        (dbo_entrada - dbo_salida)
        / dbo_entrada
    ) * 100

    return eficiencia


# =========================================
# FUNCIÓN: CLASIFICAR DESEMPEÑO
# =========================================

def clasificar_desempeno(eficiencia):
    """
    Clasifica el desempeño operacional
    según la eficiencia obtenida.
    """

    if eficiencia >= 85:
        return "Eficiente"
    
    return "Deficiente"


# =========================================
# FUNCIÓN: VALIDAR VALORES NULOS
# =========================================

def validar_nulos(dataframe):
    """
    Retorna la cantidad de valores
    nulos por columna.
    """

    return dataframe.isnull().sum()


# =========================================
# FUNCIÓN: DETECTAR DUPLICADOS
# =========================================

def contar_duplicados(dataframe):
    """
    Retorna la cantidad de registros
    duplicados.
    """

    return dataframe.duplicated().sum()


# =========================================
# FUNCIÓN: DETECTAR OUTLIERS
# =========================================

def detectar_outliers(columna):
    """
    Detecta valores atípicos utilizando IQR.
    """

    q1 = columna.quantile(0.25)
    q3 = columna.quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    outliers = columna[
        (columna < limite_inferior) |
        (columna > limite_superior)
    ]

    return outliers


# =========================================
# FUNCIÓN: RESUMEN ESTADÍSTICO
# =========================================

def resumen_estadistico(dataframe):
    """
    Genera estadísticas descriptivas.
    """

    return dataframe.describe()
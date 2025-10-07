"""
Módulo para análisis de calidad de datos.
"""

import pandas as pd
import numpy as np


def analyze_data_quality(df):
    """
    Analiza la calidad de datos de un DataFrame calculando:
    - Porcentaje de valores nulos
    - Porcentaje de ceros
    - Porcentaje de infinitos
    - Porcentaje de outliers por IQR
    - Identifica si la variable es categórica o texto (ignora)
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame a analizar
    
    Returns:
    --------
    pandas.DataFrame
        Resumen de calidad de datos por columna
    """
    results = []
    
    for col in df.columns:
        # Obtener la serie de la columna
        series = df[col]
        
        # Determinar si es numérica
        is_numeric = pd.api.types.is_numeric_dtype(series)
        
        # Si no es numérica, saltar esta columna
        if not is_numeric:
            continue
            
        # Calcular estadísticas
        total_rows = len(series)
        
        # Porcentaje de nulos
        null_count = series.isnull().sum()
        null_pct = (null_count / total_rows) * 100
        
        # Porcentaje de ceros
        zero_count = (series == 0).sum()
        zero_pct = (zero_count / total_rows) * 100
        
        # Porcentaje de infinitos
        inf_count = np.isinf(series).sum()
        inf_pct = (inf_count / total_rows) * 100
        
        # Porcentaje de outliers por IQR (solo para valores no nulos)
        non_null_series = series.dropna()
        if len(non_null_series) > 0:
            Q1 = non_null_series.quantile(0.25)
            Q3 = non_null_series.quantile(0.75)
            IQR = Q3 - Q1
            
            # Definir límites para outliers
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Contar outliers
            outliers_count = ((non_null_series < lower_bound) | 
                            (non_null_series > upper_bound)).sum()
            outliers_pct = (outliers_count / len(non_null_series)) * 100
        else:
            outliers_pct = 0
        
        # Agregar resultados
        results.append({
            'Columna': col,
            'Tipo': 'Numérica',
            'Porcentaje_Nulos': round(null_pct, 2),
            'Porcentaje_Ceros': round(zero_pct, 2),
            'Porcentaje_Infinitos': round(inf_pct, 2),
            'Porcentaje_Outliers_IQR': round(outliers_pct, 2),
            'Total_Registros': total_rows,
            'Registros_No_Nulos': len(non_null_series)
        })
    
    # Crear DataFrame con resultados
    results_df = pd.DataFrame(results)
    
    return results_df


def show_categorical_columns(df):
    """
    Muestra las columnas que son categóricas o de texto (ignoradas en el análisis).
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame a analizar
    
    Returns:
    --------
    pandas.DataFrame or None
        DataFrame con información de columnas categóricas o None si no hay
    """
    categorical_cols = []
    
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            categorical_cols.append({
                'Columna': col,
                'Tipo': 'Categórica/Texto',
                'Valores_Únicos': df[col].nunique(),
                'Ejemplo_Valor': df[col].dropna().iloc[0] if len(df[col].dropna()) > 0 else 'N/A'
            })
    
    if categorical_cols:
        return pd.DataFrame(categorical_cols)
    else:
        print("No se encontraron columnas categóricas o de texto.")
        return None


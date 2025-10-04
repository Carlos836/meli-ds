# Meli Data Science Project

Este repositorio contiene el proyecto de ciencia de datos para MercadoLibre.

## Estructura del Proyecto

```
meli-ds/
├── data/                   # Directorio de datos
│   ├── raw/               # Datos sin procesar
│   ├── processed/         # Datos procesados
│   └── external/          # Datos externos
├── notebooks/             # Jupyter notebooks para análisis exploratorio
├── src/                   # Código fuente
│   ├── data/             # Scripts de procesamiento de datos
│   ├── features/         # Ingeniería de características
│   ├── models/           # Modelos de machine learning
│   └── visualization/    # Scripts de visualización
├── tests/                # Tests unitarios
├── docs/                 # Documentación
├── models/               # Modelos entrenados
│   ├── experiments/      # Modelos experimentales
│   └── production/       # Modelos de producción
├── configs/              # Archivos de configuración
├── requirements.txt      # Dependencias de Python
└── README.md            # Este archivo
```

## Configuración del Entorno

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar análisis exploratorio en notebooks/
2. Entrenar modelos en src/models/
3. Ejecutar tests con pytest

## Contribución

1. Crear una rama para la nueva feature
2. Hacer commit de los cambios
3. Crear un Pull Request

## Licencia

Este proyecto es propiedad de MercadoLibre.

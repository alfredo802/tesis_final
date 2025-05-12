# Sistema de Pronóstico de Mareas - Valparaíso

Este sistema permite visualizar y consultar pronósticos de mareas para el Puerto de Valparaíso, incluyendo una interfaz web con gráficos y mapa interactivo.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno (Chrome, Firefox, Edge, etc.)

## Instalación

1. Clonar o descargar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_DIRECTORIO]
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activar el entorno virtual:
   - En Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - En Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

1. Crear un archivo `config.py` en el directorio raíz del proyecto con la siguiente estructura:
```python
# Configuration file for API keys and other sensitive data
GOOGLE_MAPS_API_KEY = 'TU_CLAVE_API_DE_GOOGLE_MAPS'
```

2. Obtener una clave de API de Google Maps:
   - Visitar [Google Cloud Console](https://console.cloud.google.com/)
   - Crear un nuevo proyecto o seleccionar uno existente
   - Habilitar la API de Maps JavaScript
   - Crear credenciales (clave API)
   - Copiar la clave API en el archivo `config.py`

## Estructura del Proyecto

```
proyecto/
│
├── app.py                 # Aplicación principal Flask
├── config.py             # Configuración y claves API
├── requirements.txt      # Dependencias del proyecto
├── static/              # Archivos estáticos
│   ├── css/
│   └── js/
├── templates/           # Plantillas HTML
│   └── index.html
├── resultados/          # Datos de pronósticos
└── README.md           # Este archivo
```

## Ejecución

1. Asegurarse de que el entorno virtual está activado

2. Ejecutar la aplicación:
```bash
python app.py
```

3. Abrir el navegador y visitar:
```
http://localhost:5000
```

## Características

- Visualización de pronósticos de mareas en tiempo real
- Gráfico interactivo de niveles de marea
- Mapa interactivo con la ubicación del Puerto de Valparaíso
- Consulta de pronósticos por rango de fechas
- Información actualizada de pleamares y bajamares

## Uso

1. **Consulta de Pronósticos**:
   - Seleccionar fecha de inicio y fin
   - Hacer clic en "Consultar"
   - O usar "Ver Hoy" para datos del día actual

2. **Visualización**:
   - El gráfico muestra los niveles de marea
   - El mapa muestra la ubicación del puerto
   - La información del puerto muestra datos actualizados

## Solución de Problemas

1. **Error de conexión a la API de Google Maps**:
   - Verificar que la clave API está correctamente configurada
   - Comprobar que la API está habilitada en Google Cloud Console

2. **No se cargan los datos**:
   - Verificar que los archivos de pronóstico están en la carpeta `resultados/`
   - Comprobar la conexión a internet

3. **Error en la aplicación**:
   - Revisar los logs en la consola
   - Verificar que todas las dependencias están instaladas

## Mantenimiento

- Actualizar regularmente las dependencias:
```bash
pip install --upgrade -r requirements.txt
```

- Verificar la validez de la clave API de Google Maps
- Mantener actualizados los datos de pronóstico

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

[Tu Nombre] - [Tu Email]

Link del Proyecto: [https://github.com/tu-usuario/tu-repositorio](https://github.com/tu-usuario/tu-repositorio) 
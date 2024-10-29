<h1 align="center">🚀 Correos Tracking API & Bot</h1>

<p align="center">
  <img src="/api/placeholder/1200/300" alt="Correos Track API Banner">
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-0.68.0+-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI Framework">
  </a>
  <a href="https://core.telegram.org/bots/api">
    <img src="https://img.shields.io/badge/Telegram-Bot_API-2CA5E0?style=flat-square&logo=telegram&logoColor=white" alt="Telegram Bot API">
  </a>
  <a href="https://www.correos.es/es/es/herramientas/localizador/envios">
    <img src="https://img.shields.io/badge/Correos-API-yellow?style=flat-square" alt="Correos API">
  </a>
</p>

<p align="center">
  API REST y Bot de Telegram para el seguimiento automatizado de envíos de Correos España con notificaciones en tiempo real.
</p>

## ✨ Características

- 🚀 **API REST**: Endpoints para gestionar envíos programáticamente
- 📚 **Documentación OpenAPI**: Interfaz Swagger UI integrada
- 🤖 **Bot de Telegram**: Notificaciones y comandos interactivos
- 🔄 **Monitorización Continua**: Seguimiento automático de envíos
- 📱 **Notificaciones**: Alertas en tiempo real de cambios de estado
- 💾 **Persistencia**: Almacenamiento de datos entre reinicios
- 🔐 **Configuración Segura**: Variables de entorno separadas

## 📁 Estructura del Proyecto

```plaintext
proyecto/
├── api.py              # API FastAPI
├── config.py           # Configuración y constantes
├── correos_tracker.py  # Clase principal del tracker
├── requirements.txt    # Dependencias del proyecto
├── .gitignore         # Archivos a ignorar
└── README.md          # Documentación
```

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/yourusername/correos-track-api.git
cd correos-track-api
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables en `config.py`:
```python
TELEGRAM_BOT_TOKEN = "TU_BOT_TOKEN"
TELEGRAM_CHAT_ID = "TU_CHAT_ID"
```

## 💻 Uso

### Iniciar la API y el Bot:
```bash
python api.py
```

La API estará disponible en `http://localhost:8000`

### Documentación API:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints API:

```bash
# Añadir envío
POST /shipments/
{
    "tracking_number": "PKAPBQ0714089710148130G"
}

# Listar envíos
GET /shipments/

# Obtener estado
GET /shipments/{tracking_number}

# Eliminar envío
DELETE /shipments/{tracking_number}
```

### Comandos del Bot:
- `/add NUMERO` - Añade un envío
- `/status NUMERO` - Muestra el estado
- `/list` - Lista todos los envíos
- `/remove NUMERO` - Elimina un envío
- `/help` - Muestra la ayuda

## 🛠️ Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno
- [Python Telegram Bot](https://python-telegram-bot.org/) - API de Telegram
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validación de datos
- [Requests](https://docs.python-requests.org/) - Cliente HTTP

## 📡 Ejemplos de API

### Python
```python
import requests

# Añadir envío
response = requests.post(
    "http://localhost:8000/shipments/",
    json={"tracking_number": "PKAPBQ0714089710148130G"}
)
```

### cURL
```bash
# Añadir envío
curl -X POST "http://localhost:8000/shipments/" \
     -H "Content-Type: application/json" \
     -d '{"tracking_number":"PKAPBQ0714089710148130G"}'
```

## 📱 Capturas de pantalla

<p align="center">
  <img src="/api/placeholder/300/500" alt="API Docs" width="300">
  <img src="/api/placeholder/300/500" alt="Bot Demo" width="300">
</p>

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## 📧 Contacto

Link del Proyecto: [https://github.com/yourusername/correos-track-api](https://github.com/yourusername/correos-track-api)

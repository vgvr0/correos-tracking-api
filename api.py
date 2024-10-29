# api.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import uvicorn
from typing import List, Optional
import threading
from correos_tracker import CorreosTracker
from config import *

app = FastAPI(
    title="Correos Track API",
    description="API para seguimiento de envíos de Correos con notificaciones Telegram",
    version="1.0.0"
)

# Modelo de datos para las peticiones
class Shipment(BaseModel):
    tracking_number: str

class ShipmentResponse(BaseModel):
    tracking_number: str
    status: str
    events: Optional[List[dict]]

# Inicializar el tracker como variable global
tracker = CorreosTracker()

# Iniciar el bot en un hilo separado
def run_bot():
    tracker.run_bot_polling()

# Iniciar el bot en segundo plano al arrancar la API
@app.on_event("startup")
async def startup_event():
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

# Endpoints de la API
@app.post("/shipments/", response_model=ShipmentResponse)
async def add_shipment(shipment: Shipment):
    """Añadir un nuevo envío al seguimiento"""
    try:
        response = tracker.add_tracking(shipment.tracking_number)
        return {
            "tracking_number": shipment.tracking_number,
            "status": "added",
            "events": tracker.get_events(shipment.tracking_number)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/shipments/", response_model=List[ShipmentResponse])
async def list_shipments():
    """Listar todos los envíos en seguimiento"""
    try:
        shipments = []
        for number in tracker.tracking_numbers:
            events = tracker.get_events(number)
            shipments.append({
                "tracking_number": number,
                "status": "tracking",
                "events": events
            })
        return shipments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/shipments/{tracking_number}", response_model=ShipmentResponse)
async def get_shipment(tracking_number: str):
    """Obtener estado de un envío específico"""
    try:
        events = tracker.get_events(tracking_number)
        if not events:
            raise HTTPException(status_code=404, detail="Shipment not found")
        return {
            "tracking_number": tracking_number,
            "status": "tracking",
            "events": events
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/shipments/{tracking_number}")
async def remove_shipment(tracking_number: str):
    """Eliminar un envío del seguimiento"""
    try:
        response = tracker.remove_tracking(tracking_number)
        return {"message": "Shipment removed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

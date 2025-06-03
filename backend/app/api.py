from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.customer_controller import router as customer_router
from controllers.vehicle_controller import router as vehicle_router
from controllers.reservation_controller import router as reservation_router
from controllers.log_controller import router as log_router

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:5173"] si querés limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
#  ENDPOINTS API REST
# =========================

@app.get("/")
def root():
    return {"details": "Hello, World!"}

app.include_router(customer_router)
app.include_router(vehicle_router)
app.include_router(reservation_router)
app.include_router(log_router)

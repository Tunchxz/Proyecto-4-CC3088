# **Proyecto 4 - Sistema de Alquiler de Vehículos - Proyecto Final**  
Proyecto final de Bases de Datos 1. Sistema completo de gestión con backend en FastAPI, frontend en React y base de datos PostgreSQL.

---

## Descripción del Proyecto

Este sistema es una evolución del **Proyecto 3 - Sistema de Alquiler de Vehículos**, ahora desarrollado como proyecto final con mejoras significativas en la arquitectura y tecnologías utilizadas. El sistema permite la gestión completa de un negocio de alquiler de vehículos con funcionalidades avanzadas de reportes, gestión de reservas, contratos, pagos y mantenimientos.

### Características principales:
- Gestión completa de reservas y contratos de alquiler
- Sistema de pagos y control de multas
- Gestión de mantenimientos de vehículos
- Generación de reportes avanzados con filtros múltiples
- Interfaz web moderna y responsiva
- API RESTful robusta
- Base de datos optimizada con triggers, vistas y funciones

---

## **Colaboradores**

- Cristian Túnchez (231359)  
- Dulce Ambrosio (231143)  
- Daniel Chet (231177)  
- Javier Linares (231135)  
- Gadiel Ocaña (231270)

---

## **Estructura del Proyecto**

```
├── README.md
├── backend/                    # API Backend (FastAPI)
│   ├── .dockerignore
│   ├── .env                   # Variables de entorno
│   ├── .gitignore
│   ├── docker-compose.yml     # Orquestación de servicios
│   ├── Dockerfile             # Imagen del backend
│   ├── requirements.txt       # Dependencias Python
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py            # Endpoints de la API
│   │   ├── db.py             # Configuración de base de datos
│   │   ├── main.py           # Punto de entrada principal
│   │   ├── controllers/      # Controladores de la aplicación
│   │   ├── models/          # Modelos SQLAlchemy
│   │   ├── schemas/         # Esquemas Pydantic
│   │   └── services/        # Lógica de negocio
│   └── scripts/
│       ├── data.sql         # Datos iniciales
│       ├── schema.sql       # Esquema generado automáticamente
│       ├── triggers.sql     # Triggers y funciones
│       └── views.sql        # Vistas de la base de datos
└── frontend/                # Frontend (React + Vite)
    ├── .dockerignore
    ├── .env                 # Variables de entorno del frontend
    ├── .gitignore
    ├── docker-compose.yml
    ├── Dockerfile           # Imagen del frontend
    ├── eslint.config.js     # Configuración ESLint
    ├── index.html           # HTML principal
    ├── package.json         # Dependencias Node.js
    ├── vite.config.js       # Configuración Vite
    ├── public/
    │   └── vite.svg
    └── src/
        ├── api.js           # Cliente API
        ├── App.css
        ├── App.jsx          # Componente principal
        ├── index.css
        ├── main.jsx         # Punto de entrada
        └── assets/
```

---

## **Tecnologías Utilizadas**

### Backend
- **Python** con FastAPI
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Base de datos relacional
- **Uvicorn** - Servidor ASGI
- **Psycopg2** - Adaptador PostgreSQL para Python
- **Docker** para containerización

### Frontend
- **React** - Biblioteca para interfaces de usuario
- **JavaScript** (Vanilla)
- **HTML5** y **CSS3**
- **Vite** - Herramienta de build rápida
- **Bootstrap 5** - Framework CSS
- **Bootstrap Icons** - Iconografía
- **Docker** para containerización

### Infraestructura y DevOps
- **Docker Compose** para orquestación de servicios

---

## **Requisitos Previos**

- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/) instalados
- Git

---

## **Instalación y Ejecución**

### Opción 1: Con Docker (Recomendado)

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd Proyecto-4-CC3088
   ```

2. **Configurar variables de entorno**

   Backend (`backend/.env`):
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   POSTGRES_DB=proyecto4_db
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=password123
   ```
   
   Frontend (`frontend/.env`):
   ```env
   VITE_API_URL=http://localhost:8000
   ```

3. **Levantar los servicios**
   Desde el directorio raíz del proyecto:
   ```bash
   docker-compose up --build
   ```
   O bien, iniciar backend y frontend por separado:
   ```bash
   # Backend (incluye PostgreSQL)
   cd backend
   docker-compose up --build
   
   # Frontend
   cd ../frontend
   docker-compose up --build
   ```

   Este comando:
   - Construirá las imágenes de Docker necesarias
   - Levantará los contenedores para backend, frontend y base de datos
   - Configurará la red entre los servicios
   - Ejecutará los scripts de inicialización de la base de datos

4. **Acceder a la aplicación**

   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **Backend API**: [http://localhost:8000](http://localhost:8000)
   - **Documentación API**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **PostgreSQL**: localhost:5432

---

### Opción 2: Desarrollo Local

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## **Servicios y Puertos**

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Documentación API**: http://localhost:8000/docs

---

## **Funcionalidades del Sistema**

El sistema incluye una inicialización automática que:

1. **Crea la base de datos** usando SQLAlchemy
2. **Genera schema.sql** automáticamente desde los modelos
3. **Espera conexión a PostgreSQL** con reintentos automáticos
4. **Inserta datos iniciales** desde `data.sql`
5. **Crea vistas** desde `views.sql`
6. **Configura triggers y funciones** desde `triggers.sql`
7. **Levanta la API** en el puerto 8000

### Gestión de Vehículos
- Registro y actualización de vehículos
- Control de disponibilidad
- Gestión de mantenimientos

### Gestión de Clientes
- Registro de clientes
- Historial de alquileres
- Gestión de información personal

### Sistema de Reservas
- Creación de reservas
- Modificación y cancelación
- Control de disponibilidad por fechas

### Contratos de Alquiler
- Generación automática de contratos
- Gestión de términos y condiciones
- Control de estados del contrato

### Sistema de Pagos
- Registro de pagos
- Control de multas
- Generación de facturas

### Reportes Avanzados
- Reportes de ingresos por período
- Análisis de vehículos más rentados
- Reportes de mantenimientos
- Dashboard con métricas clave

---

## **Estructura de la Base de Datos**

Los modelos están definidos en `backend/app/models/` e incluyen:
- Address, Color, Country, Customer
- Vehicle, VehicleType, Manufacturer, Model
- RentalContract, Reservation, Payment
- Fine, Maintenance, Rates, Refund
- Y más...

---

## **Scripts de Base de Datos**

El proyecto incluye scripts SQL organizados en:

- **`schema.sql`**: Definición de tablas, índices y restricciones (generado automáticamente desde los modelos SQLAlchemy)
- **`data.sql`**: Datos iniciales y de prueba para poblar la base de datos
- **`views.sql`**: Vistas para reportes y consultas complejas
- **`triggers.sql`**: Funciones y triggers automáticos de PostgreSQL

---

## **API Endpoints**

La API REST incluye endpoints para:

- `/api/vehicles` - Gestión de vehículos
- `/api/customers` - Gestión de clientes  
- `/api/reservations` - Sistema de reservas
- `/api/contracts` - Contratos de alquiler
- `/api/payments` - Sistema de pagos
- `/api/reports` - Generación de reportes

---

## **Comandos Útiles**

```bash
# Ver logs del backend
cd backend && docker-compose logs -f

# Ver logs del frontend
cd frontend && docker-compose logs -f

# Reiniciar servicios
docker-compose restart

# Acceder a la base de datos
docker-compose exec postgres psql -U admin -d proyecto4_db
```

---

## **Licencia**

Este proyecto es parte del curso de Bases de Datos 1 en la Universidad del Valle de Guatemala y es únicamente para fines educativos.

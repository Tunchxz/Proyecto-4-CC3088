-- =======================
--  Proyecto 4 (VIEWS)
-- =======================

-- -------------------
--  ELIMINAR VISTAS
-- -------------------
DROP VIEW IF EXISTS customer_view;
DROP VIEW IF EXISTS vehicle_view;
DROP VIEW IF EXISTS reservation_view;

-- -------------------
--  CREAR VISTAS
-- -------------------

-- Vista: Índice para Customer CRUD
CREATE OR REPLACE VIEW customer_view AS
SELECT
    id,
    first_name,
    last_name,
    email,
    phone_number,
    registration_date
FROM customer;

-- Vista: Índice para Vehicle CRUD
CREATE OR REPLACE VIEW vehicle_view AS
SELECT
    v.id,
    v.car_plate,
    v.mileage,
    v.status_id,
    v.model_id,
    v.facility_id,
    v.rates_id
FROM vehicle v;

-- Vista: Índice para Reservation CRUD
CREATE OR REPLACE VIEW reservation_view AS
SELECT
    id,
    customer_id,
    vehicle_id,
    reservation_date,
    start_date,
    end_date,
    status_id
FROM reservation;

-- =======================
--  Proyecto 4 (VIEWS)
-- =======================

-- -------------------
--  ELIMINAR VISTAS
-- -------------------

DROP VIEW IF EXISTS customer_view;
DROP VIEW IF EXISTS vehicle_view;
DROP VIEW IF EXISTS reservation_view;
DROP VIEW IF EXISTS view_reservation_summary;
DROP VIEW IF EXISTS view_vehicle_maintenance_history;
DROP VIEW IF EXISTS view_total_income_per_contract;

-- ----------------------------
--  CREAR VISTAS (ÍNDICES)
-- ----------------------------

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

-- ----------------------------
--  CREAR VISTAS (COMPLEJAS)
-- ----------------------------

-- Resumen de reservas con cliente, vehículo, fechas y estado textual.
CREATE OR REPLACE VIEW view_reservation_summary AS
SELECT
    r.id AS reservation_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    v.car_plate,
    r.start_date,
    r.end_date,
    os.status_name AS reservation_status
FROM reservation r
JOIN customer c ON r.customer_id = c.id
JOIN vehicle v ON r.vehicle_id = v.id
JOIN operationstatus os ON r.status_id = os.id;

-- Historial de mantenimientos por vehículo con descripción, fecha y costo.
CREATE OR REPLACE VIEW view_vehicle_maintenance_history AS
SELECT
    v.car_plate,
    m.maintenance_date,
    m.description,
    m.cost
FROM vehicle_maintenance vm
JOIN vehicle v ON vm.vehicle_id = v.id
JOIN maintenance m ON vm.maintenance_id = m.id
ORDER BY v.car_plate, m.maintenance_date DESC;

-- Ingreso total por contrato, sumando pagos y multas.
CREATE OR REPLACE VIEW view_total_income_per_contract AS
SELECT
    rc.id AS contract_id,
    COALESCE(SUM(p.amount), 0) AS total_payments,
    COALESCE((SELECT SUM(f.amount)
              FROM fine f
              WHERE f.rental_contract_id = rc.id), 0) AS total_fines,
    COALESCE(SUM(p.amount), 0) +
    COALESCE((SELECT SUM(f.amount)
              FROM fine f
              WHERE f.rental_contract_id = rc.id), 0) AS total_income
FROM rentalcontract rc
LEFT JOIN payment p ON p.rental_contract_id = rc.id
GROUP BY rc.id;

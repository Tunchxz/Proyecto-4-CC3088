-- =======================
--  Proyecto 4 (VIEWS)
-- =======================

-- -------------------
--  FUNCIONES SQL
-- -------------------

-- Devuelve la cantidad de días entre dos fechas (inclusive).
CREATE OR REPLACE FUNCTION calculate_rental_days(start_date DATE, end_date DATE)
RETURNS INTEGER AS $$
BEGIN
    RETURN (end_date - start_date + 1);
END;
$$ LANGUAGE plpgsql;
 
 -- Calcula el costo estimado de una reserva con base en las tarifas del vehículo.
 CREATE OR REPLACE FUNCTION calculate_reservation_cost(
    vehicle_id INTEGER,
    start_date DATE,
    end_date DATE
)
RETURNS NUMERIC AS $$
DECLARE
    rental_days INTEGER;
    rate RECORD;
    total NUMERIC := 0;
BEGIN
    SELECT daily_rate, weekly_rate, monthly_rate
    INTO rate
    FROM rates
    WHERE id = (SELECT rates_id FROM vehicle WHERE id = vehicle_id);

    rental_days := calculate_rental_days(start_date, end_date);

    -- Tarificación básica: se prioriza mes > semana > día
    total := (rental_days / 30) * rate.monthly_rate +
             ((rental_days % 30) / 7) * rate.weekly_rate +
             (rental_days % 7) * rate.daily_rate;

    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- -------------------
--  TRIGGERS
-- -------------------

-- Evitar reservas con end_date < start_date
CREATE OR REPLACE FUNCTION validate_reservation_dates()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.end_date < NEW.start_date THEN
        RAISE EXCEPTION 'La fecha final no puede ser menor a la fecha de inicio';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validate_reservation_dates
BEFORE INSERT OR UPDATE ON reservation
FOR EACH ROW EXECUTE FUNCTION validate_reservation_dates();

-- Actualizar el estado del vehículo a 'ocupado' cuando se crea una reserva
CREATE OR REPLACE FUNCTION mark_vehicle_reserved()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE vehicle
    SET status_id = 2
    WHERE id = NEW.vehicle_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_mark_vehicle_reserved
AFTER INSERT ON reservation
FOR EACH ROW EXECUTE FUNCTION mark_vehicle_reserved();

-- Auditoría de pagos registrados
CREATE OR REPLACE FUNCTION log_payment_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO payment_log (payment_id, amount, method)
    VALUES (NEW.id, NEW.amount, NEW.payment_method::TEXT);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_payment_insert
AFTER INSERT ON payment
FOR EACH ROW EXECUTE FUNCTION log_payment_insert();

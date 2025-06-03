
CREATE TABLE address (
	id SERIAL NOT NULL, 
	unit_number VARCHAR(8), 
	street_number VARCHAR(8), 
	address_line_1 VARCHAR(64) NOT NULL, 
	address_line_2 VARCHAR(64), 
	city VARCHAR(64) NOT NULL, 
	region VARCHAR(64), 
	country_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(country_id) REFERENCES country (id)
)

;


CREATE TABLE color (
	id SERIAL NOT NULL, 
	color_name VARCHAR(16) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (color_name)
)

;


CREATE TABLE contract_fine (
	rental_contract_id INTEGER NOT NULL, 
	fine_id INTEGER NOT NULL, 
	PRIMARY KEY (rental_contract_id, fine_id), 
	FOREIGN KEY(rental_contract_id) REFERENCES rentalcontract (id), 
	FOREIGN KEY(fine_id) REFERENCES fine (id)
)

;


CREATE TABLE country (
	id SERIAL NOT NULL, 
	country_name VARCHAR(64) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (country_name)
)

;


CREATE TABLE customer (
	id SERIAL NOT NULL, 
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL, 
	date_of_birth DATE NOT NULL, 
	driver_license_number VARCHAR(64) NOT NULL, 
	email VARCHAR(128) NOT NULL, 
	phone_number VARCHAR(16) NOT NULL, 
	registration_date DATE NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (driver_license_number), 
	UNIQUE (email)
)

;


CREATE TABLE customer_address (
	customer_id INTEGER NOT NULL, 
	address_id INTEGER NOT NULL, 
	PRIMARY KEY (customer_id, address_id), 
	FOREIGN KEY(customer_id) REFERENCES customer (id), 
	FOREIGN KEY(address_id) REFERENCES address (id)
)

;


CREATE TABLE facility (
	id SERIAL NOT NULL, 
	facility_name VARCHAR(128) NOT NULL, 
	facility_phone_number VARCHAR(16) NOT NULL, 
	address_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (facility_name), 
	UNIQUE (facility_phone_number), 
	FOREIGN KEY(address_id) REFERENCES address (id)
)

;


CREATE TABLE fine (
	id SERIAL NOT NULL, 
	rental_contract_id INTEGER NOT NULL, 
	fine_date DATE NOT NULL, 
	amount DECIMAL(10, 2) NOT NULL, 
	reason TEXT NOT NULL, 
	status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (amount >= 0), 
	FOREIGN KEY(rental_contract_id) REFERENCES rentalcontract (id), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id)
)

;


CREATE TABLE maintenance (
	id SERIAL NOT NULL, 
	maintenance_date DATE NOT NULL, 
	description TEXT NOT NULL, 
	cost DECIMAL(10, 2) NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (cost >= 0)
)

;


CREATE TABLE manufacturer (
	id SERIAL NOT NULL, 
	manufacturer_name VARCHAR(128) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (manufacturer_name)
)

;


CREATE TABLE model (
	id SERIAL NOT NULL, 
	manufacturer_id INTEGER NOT NULL, 
	model_name VARCHAR(128) NOT NULL, 
	transmission_type transmissionenum NOT NULL, 
	capacity seatsenum NOT NULL, 
	vehicle_type_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (manufacturer_id, model_name), 
	FOREIGN KEY(manufacturer_id) REFERENCES manufacturer (id), 
	FOREIGN KEY(vehicle_type_id) REFERENCES vehicletype (id)
)

;


CREATE TABLE model_color (
	model_id INTEGER NOT NULL, 
	color_id INTEGER NOT NULL, 
	PRIMARY KEY (model_id, color_id), 
	FOREIGN KEY(model_id) REFERENCES model (id), 
	FOREIGN KEY(color_id) REFERENCES color (id)
)

;


CREATE TABLE payment_log (
	id SERIAL NOT NULL, 
	payment_id INTEGER, 
	log_date TIMESTAMP WITHOUT TIME ZONE, 
	amount NUMERIC, 
	method VARCHAR, 
	PRIMARY KEY (id)
)

;


CREATE TABLE operationstatus (
	id SERIAL NOT NULL, 
	status_name VARCHAR(64) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (status_name)
)

;


CREATE TABLE payment (
	id SERIAL NOT NULL, 
	rental_contract_id INTEGER, 
	fine_id INTEGER, 
	payment_date DATE NOT NULL, 
	amount DECIMAL(10, 2) NOT NULL, 
	payment_method paymentmethodenum NOT NULL, 
	status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (amount >= 0), 
	FOREIGN KEY(rental_contract_id) REFERENCES rentalcontract (id), 
	FOREIGN KEY(fine_id) REFERENCES fine (id), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id)
)

;


CREATE TABLE rates (
	id SERIAL NOT NULL, 
	daily_rate DECIMAL(10, 2) NOT NULL, 
	weekly_rate DECIMAL(10, 2) NOT NULL, 
	monthly_rate DECIMAL(10, 2) NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (daily_rate >= 0), 
	CHECK (weekly_rate >= 0), 
	CHECK (monthly_rate >= 0)
)

;


CREATE TABLE refund (
	id SERIAL NOT NULL, 
	payment_id INTEGER NOT NULL, 
	refund_date DATE NOT NULL, 
	amount DECIMAL(10, 2) NOT NULL, 
	reason TEXT NOT NULL, 
	status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (amount >= 0), 
	FOREIGN KEY(payment_id) REFERENCES payment (id), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id)
)

;


CREATE TABLE rentalcontract (
	id SERIAL NOT NULL, 
	reservation_id INTEGER NOT NULL, 
	start_date DATE NOT NULL, 
	end_date DATE NOT NULL, 
	status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (end_date >= start_date), 
	UNIQUE (reservation_id), 
	FOREIGN KEY(reservation_id) REFERENCES reservation (id), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id)
)

;


CREATE TABLE reservation (
	id SERIAL NOT NULL, 
	customer_id INTEGER NOT NULL, 
	vehicle_id INTEGER NOT NULL, 
	reservation_date DATE NOT NULL, 
	start_date DATE NOT NULL, 
	end_date DATE NOT NULL, 
	status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (end_date >= start_date), 
	FOREIGN KEY(customer_id) REFERENCES customer (id), 
	FOREIGN KEY(vehicle_id) REFERENCES vehicle (id), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id)
)

;


CREATE TABLE vehicle (
	id SERIAL NOT NULL, 
	model_id INTEGER NOT NULL, 
	facility_id INTEGER NOT NULL, 
	car_plate VARCHAR(64) NOT NULL, 
	mileage INTEGER NOT NULL, 
	status_id INTEGER NOT NULL, 
	rates_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (mileage >= 0), 
	FOREIGN KEY(model_id) REFERENCES model (id), 
	FOREIGN KEY(facility_id) REFERENCES facility (id), 
	UNIQUE (car_plate), 
	FOREIGN KEY(status_id) REFERENCES operationstatus (id), 
	FOREIGN KEY(rates_id) REFERENCES rates (id)
)

;


CREATE TABLE vehicle_maintenance (
	vehicle_id INTEGER NOT NULL, 
	maintenance_id INTEGER NOT NULL, 
	PRIMARY KEY (vehicle_id, maintenance_id), 
	FOREIGN KEY(vehicle_id) REFERENCES vehicle (id), 
	FOREIGN KEY(maintenance_id) REFERENCES maintenance (id)
)

;


CREATE TABLE vehicletype (
	id SERIAL NOT NULL, 
	vehicle_type_name VARCHAR(32) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (vehicle_type_name)
)

;


CREATE DATABASE clinicDB;
USE clinicDB;

CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(10) UNIQUE NOT NULL,
    age INT CHECK(age > 0),
    gender VARCHAR(50),
    entry_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_treatment_date DATE
);

CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    appointment_date DATE,
    treatment_type VARCHAR(255) NOT NULL,
    doctor_name VARCHAR(255),
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE Billing (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT, 
    treatment_type VARCHAR(255) NOT NULL,
    treatment_date DATE,
    cost DECIMAL(10,2),
    payment_status ENUM('Paid', 'Unpaid') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- ✅ Trigger: Update last_treatment_date in Patients table when a new bill is added
DELIMITER $$
CREATE TRIGGER update_last_treatment_date
AFTER INSERT ON Billing
FOR EACH ROW
BEGIN
    UPDATE Patients
    SET last_treatment_date = NEW.treatment_date
    WHERE patient_id = NEW.patient_id;
END$$
DELIMITER ;

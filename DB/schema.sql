use sys;
select * from sys_config;
create schema AirportBookingSystem;

use AirportBookingSystem;

create table passengers (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255),
email VARCHAR(255),
passport_number VARCHAR(50) UNIQUE,
frequent_flyer_points INT
);

create table airplanes (
id INT PRIMARY KEY AUTO_INCREMENT,
model VARCHAR(100),
registration VARCHAR(50) UNIQUE,
capacity INT
);

create table flights(
id INT PRIMARY KEY AUTO_INCREMENT,
flight_number VARCHAR(20) UNIQUE,
origin VARCHAR(100),
destination VARCHAR(100),
departure_time DATETIME,
arrival_time DATETIME,
airplane_id INT,
FOREIGN KEY (airplane_id) REFERENCES airplanes(id)
);

create table reservations(
id INT PRIMARY KEY AUTO_INCREMENT,
reservation_code VARCHAR(36) UNIQUE,
passenger_id INT,
flight_id INT,
seat_number VARCHAR(10),
status ENUM('confirmed', 'cancelled'),
booking_time DATETIME,
FOREIGN KEY (passenger_id) REFERENCES passengers(id),
FOREIGN KEY (flight_id) REFERENCES flights(id)
);
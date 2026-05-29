CREATE DATABASE IF NOT EXISTS car_rental_system DEFAULT CHARSET utf8mb4;
USE car_rental_system;

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_requirements (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    use_case VARCHAR(100) NOT NULL,
    duration_days INT DEFAULT 1,
    budget_min INT,
    budget_max INT,
    seat_count INT,
    config_need VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS car_series (
    id INT PRIMARY KEY AUTO_INCREMENT,
    seriesid INT NOT NULL,
    seriesname VARCHAR(100) NOT NULL,
    seriesimg VARCHAR(500),
    seriesminprice INT,
    seriesmaxprice INT,
    average DECIMAL(5, 4),
    specids VARCHAR(255),
    create_time DATETIME
);

CREATE TABLE IF NOT EXISTS rental_orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    car_id INT NOT NULL,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'pending',
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS car_inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    seriesname VARCHAR(100) NOT NULL,
    stock_count INT DEFAULT 0,
    vehicle_status VARCHAR(20) DEFAULT 'available'
);

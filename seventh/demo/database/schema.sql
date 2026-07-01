-- schema.sql for LearningMart ecommerce demo (PHP + MySQL + PDO)
-- Import this in phpMyAdmin (SQL tab) or: mysql -u root < schema.sql
-- Re-runnable: it drops existing tables first, so importing again gives a clean start.

CREATE DATABASE IF NOT EXISTS demo;
USE demo;

-- Drop in reverse dependency order (children before parents)
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

-- Users table
-- NOTE: column names match the PHP code (name, password, role) so login/register work.
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,           -- stores a password_hash(), never plain text
    role ENUM('customer','admin') NOT NULL DEFAULT 'customer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Categories table
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Products table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,             -- price in NPR (Rs.)
    stock INT NOT NULL DEFAULT 0,
    image VARCHAR(255) DEFAULT NULL,          -- filename in /uploads (NULL = show placeholder)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Persistent shopping cart (one row per product per user; survives logout/new sessions)
CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    UNIQUE KEY uniq_user_product (user_id, product_id),   -- one row per product per user
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Orders table
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    status ENUM('pending','paid','processing','completed','cancelled') DEFAULT 'pending',
    total DECIMAL(10,2) NOT NULL,
    shipping_name VARCHAR(100) NOT NULL,
    shipping_address VARCHAR(255) NOT NULL,
    shipping_phone VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Order items table (one row per product in an order)
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price_at_purchase DECIMAL(10,2) NOT NULL, -- copy the price at time of order (prices change later)
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Payments table (one row per payment attempt for an order)
CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    gateway ENUM('khalti','esewa') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status ENUM('initiated','paid','failed') NOT NULL DEFAULT 'initiated',
    transaction_uuid VARCHAR(100) DEFAULT NULL,  -- our reference sent to the gateway (esewa uuid / khalti pidx)
    gateway_ref VARCHAR(100) DEFAULT NULL,        -- gateway's own transaction id (set on success)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- Sample data (5 categories, 15 products) — realistic NPR prices
-- ---------------------------------------------------------------------------
INSERT INTO categories (name, description) VALUES
    ('Phones',      'Smartphones and mobile devices'),
    ('Laptops',     'Laptops and notebooks'),
    ('Audio',       'Earbuds, headphones and speakers'),
    ('Wearables',   'Smart watches and fitness bands'),
    ('Accessories', 'Chargers, keyboards, bags and more');

INSERT INTO products (category_id, title, description, price, stock, image) VALUES
    (1, 'Redmi Note 13',            'Smooth AMOLED display and all-day battery.', 32999, 25, 'phone1.jpg'),
    (1, 'Samsung Galaxy A15',       'Reliable everyday phone with a big screen.', 27999, 18, 'phone2.jpg'),
    (1, 'iPhone 13 (Refurbished)',  'Certified refurbished, like-new condition.', 74999, 6,  'phone3.jpg'),
    (2, 'Acer Aspire 5',            'Slim student laptop for study and work.',    62999, 10, 'laptop1.jpg'),
    (2, 'HP Pavilion 14',           'Lightweight laptop with a crisp display.',   78999, 8,  'laptop2.jpg'),
    (3, 'Wireless Earbuds',         'True-wireless earbuds with clear sound.',    2999, 60,  'earbuds.jpg'),
    (3, 'Bluetooth Speaker',        'Portable speaker with deep bass.',           3499, 40,  'speaker.jpg'),
    (3, 'Over-Ear Headphones',      'Comfortable headphones for long listening.', 5499, 22,  'headphones.jpg'),
    (4, 'Smart Watch',              'Fitness tracking, notifications and calls.', 4999, 35,  'watch.jpg'),
    (4, 'Fitness Band',             'Step, heart-rate and sleep tracking.',       2499, 50,  'band.jpg'),
    (5, 'USB-C Charger 30W',        'Fast, compact charger for phones/laptops.',  1299, 80,  'charger.jpg'),
    (5, 'Power Bank 20000mAh',      'Charge your devices anywhere.',              2199, 45,  'powerbank.jpg'),
    (5, 'Mechanical Keyboard',      'Tactile keys for typing and gaming.',        4599, 20,  'keyboard.jpg'),
    (5, 'Wireless Mouse',           'Ergonomic, silent-click wireless mouse.',    999,  70,  'mouse.jpg'),
    (5, 'Laptop Backpack',          'Padded, water-resistant everyday backpack.', 2799, 33,  'backpack.jpg');

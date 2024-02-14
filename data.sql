CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(255) UNIQUE,
  discord_id BIGINT UNIQUE,
  balance INT DEFAULT 0,
  bank_id INT DEFAULT NULL,
  FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
);

CREATE TABLE banks (
  bank_id INT PRIMARY KEY AUTO_INCREMENT,
  owner_id INT,
  name VARCHAR(255) UNIQUE,
  balance INT DEFAULT 0,
  FOREIGN KEY (owner_id) REFERENCES users(user_id)
);

CREATE TABLE command_logs (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  command VARCHAR(255),
  timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE SCHEMA `my_bank_data_01` ;

CREATE TABLE `my_bank_data_01`.`acct` (
  `acc_no` VARCHAR(45) NOT NULL,
  `fname` VARCHAR(45) NULL,
  `lname` VARCHAR(45) NULL,
  `d_ob` VARCHAR(45) NULL,
  `s_c` VARCHAR(45) NULL,
  `amount` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `phone_no` VARCHAR(45) NULL,
  `m_f_t` VARCHAR(45) NULL,
  PRIMARY KEY (`acc_no`));

CREATE TABLE `my_bank_data_01`.`mgmt` (
  `managerid` VARCHAR(45) NOT NULL,
  `pass` VARCHAR(45) NULL,
  PRIMARY KEY (`managerid`));

CREATE TABLE `my_bank_data_01`.`users` (
  `idusers` VARCHAR(45) NOT NULL,
  `passuser` VARCHAR(45) NULL,
  PRIMARY KEY (`idusers`));
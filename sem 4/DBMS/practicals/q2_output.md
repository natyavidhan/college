## Create Tables

```
mysql> CREATE TABLE EMPLOYEE (
    ->     FNAME TEXT NOT NULL,
    ->     MINIT TEXT,
    ->     LNAME TEXT NOT NULL,
    ->     SSN TEXT PRIMARY KEY,
    ->     BDATE DATE,
    ->     ADDRESS TEXT,
    ->     SEX TEXT,
    ->     SALARY REAL,
    ->     SUPERSSN TEXT,
    ->     DNO INTEGER,
    ->     FOREIGN KEY (SUPERSSN) REFERENCES EMPLOYEE(SSN) ON DELETE SET NULL,
    ->     FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNUMBER) ON DELETE SET NULL
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE DEPARTMENT (
    ->     DNAME TEXT UNIQUE,
    ->     DNUMBER INTEGER PRIMARY KEY,
    ->     MGRSSN TEXT DEFAULT '888665555',
    ->     MGRSTARTDATE DATE,
    ->     FOREIGN KEY (MGRSSN) REFERENCES EMPLOYEE(SSN) ON DELETE SET DEFAULT
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE DEPT_LOCATIONS (
    ->     DNUMBER INTEGER,
    ->     DLOCATION TEXT,
    ->     PRIMARY KEY (DNUMBER, DLOCATION),
    ->     FOREIGN KEY (DNUMBER) REFERENCES DEPARTMENT(DNUMBER) ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE PROJECT (
    ->     PNAME TEXT UNIQUE,
    ->     PNUMBER INTEGER PRIMARY KEY,
    ->     PLOCATION TEXT,
    ->     DNUM INTEGER,
    ->     FOREIGN KEY (DNUM) REFERENCES DEPARTMENT(DNUMBER) ON DELETE SET NULL
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE WORKS_ON (
    ->     ESSN TEXT,
    ->     PNO INTEGER,
    ->     HOURS REAL,
    ->     PRIMARY KEY (ESSN, PNO),
    ->     FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE,
    ->     FOREIGN KEY (PNO) REFERENCES PROJECT(PNUMBER) ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE DEPENDENT (
    ->     ESSN TEXT,
    ->     DEPENDENT_NAME TEXT,
    ->     SEX TEXT,
    ->     BDATE DATE,
    ->     RELATIONSHIP TEXT,
    ->     PRIMARY KEY (ESSN, DEPENDENT_NAME),
    ->     FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES
    ->     ('Research', 5, NULL, '1988-05-22'),
    ->     ('Administration', 4, NULL, '1995-01-01'),
    ->     ('Headquarters', 1, NULL, '1981-06-19'),
    ->     ('Marketing', 7, NULL, '2000-01-01'),
    ->     ('IT', 10, NULL, '2003-03-15'),
    ->     ('Support', 6, NULL, '2018-01-01');
Query OK, 6 rows affected (0.00 sec)

mysql> INSERT INTO EMPLOYEE (FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPERSSN, DNO) VALUES
    -> ('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5),
    -> ('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5),
    -> ('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', 25000, '987654321', 4),
    -> ('Jennifer', 'S', 'Wallace', '987654321', '1941-06-20', '291 Berry, Bellaire, TX', 'F', 43000, '888665555', 4),
    -> ('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5),
    -> ('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5),
    -> ('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000, '987654321', 4),
    -> ('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', 55000, NULL, 1),
    -> ('Maya', 'R', 'Sharma', '777665555', '1978-04-11', '12 IT Park, Houston, TX', 'F', 61000, '888665555', 10),
    -> ('Lina', 'M', 'Das', '222334444', '1980-02-02', '9 Bellaire Ave, Bellaire, TX', 'F', 52000, '777665555', 10),
    -> ('Raj', 'P', 'Mehta', '111223333', '1975-03-03', '88 Staff Road, Stafford, TX', 'M', 58000, '777665555', 10),
    -> ('Temp', 'Q', 'Manager', '12345', '1985-05-05', '44 Support Ln, Houston, TX', 'M', 45000, '888665555', 6),
    -> ('Tina', 'L', 'Ray', '555666777', '1990-01-01', '55 Support Ln, Houston, TX', 'F', 39000, '12345', 6);
Query OK, 13 rows affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '333445555' WHERE DNUMBER = 5;
Query OK, 1 row affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '987654321' WHERE DNUMBER = 4;
Query OK, 1 row affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '888665555' WHERE DNUMBER = 1;
Query OK, 1 row affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '666884444' WHERE DNUMBER = 7;
Query OK, 1 row affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '777665555' WHERE DNUMBER = 10;
Query OK, 1 row affected (0.00 sec)

mysql> UPDATE DEPARTMENT SET MGRSSN = '12345' WHERE DNUMBER = 6;
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO DEPT_LOCATIONS VALUES
    -> (1,'Houston'),
    -> (4,'Stafford'),
    -> (5,'Bellaire'),
    -> (5,'Sugarland'),
    -> (5,'Houston'),
    -> (6,'Houston'),
    -> (7,'Bellaire'),
    -> (10,'Houston');
Query OK, 8 rows affected (0.00 sec)

mysql> INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES
    -> ('ProductX', 1, 'Bellaire', 5),
    -> ('ProductY', 2, 'Sugarland', 5),
    -> ('ProductZ', 3, 'Houston', 5),
    -> ('Computerization', 10, 'Stafford', 4),
    -> ('Reorganization', 20, 'Houston', 1),
    -> ('Newbenefits', 30, 'Stafford', 4),
    -> ('MarketPulse', 40, 'Bellaire', 7),
    -> ('CloudShift', 50, 'Houston', 10);
Query OK, 8 rows affected (0.00 sec)

mysql> INSERT INTO WORKS_ON VALUES
    -> ('123456789',1,32.5),('123456789',2,7.5),('666884444',3,40.0),('453453453',1,20.0),
    -> ('453453453',2,20.0),('333445555',2,10.0),('333445555',3,10.0),('333445555',10,10.0),
    -> ('333445555',20,10.0),('999887777',30,30.0),('999887777',10,10.0),('987987987',10,35.0),
    -> ('987987987',30,5.0),('987654321',30,20.0),('987654321',20,15.0),('888665555',20,NULL),
    -> ('777665555',50,20.0),('222334444',50,25.0),('111223333',50,15.0),('12345',40,22.0),
    -> ('555666777',40,18.0);
Query OK, 21 rows affected (0.00 sec)

mysql> INSERT INTO DEPENDENT VALUES
    -> ('333445555','Alice','F','1986-04-05','Daughter'),
    -> ('333445555','Theodore','M','1983-10-25','Son'),
    -> ('333445555','Joy','F','1958-05-03','Spouse'),
    -> ('987654321','Abner','M','1942-02-28','Spouse'),
    -> ('123456789','Michael','M','1988-01-04','Son'),
    -> ('123456789','Alice','F','1988-12-30','Daughter'),
    -> ('123456789','Elizabeth','F','1967-05-05','Spouse'),
    -> ('12345','Temp','M','2012-08-08','Son');
Query OK, 8 rows affected (0.00 sec)
```

## Initial Table Data

```sql
SELECT * FROM EMPLOYEE;
SELECT * FROM DEPARTMENT;
SELECT * FROM PROJECT;
```

```
mysql> SELECT * FROM EMPLOYEE;
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME   | SSN       | BDATE      | ADDRESS                      | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| John     | B     | Smith   | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX     | M   | 30000.0 | 333445555 | 5   |
| Franklin | T     | Wong    | 333445555 | 1955-12-08 | 638 Voss, Houston, TX        | M   | 40000.0 | 888665555 | 5   |
| Alicia   | J     | Zelaya  | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX      | F   | 25000.0 | 987654321 | 4   |
| Jennifer | S     | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX      | F   | 43000.0 | 888665555 | 4   |
| Ramesh   | K     | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX     | M   | 38000.0 | 333445555 | 5   |
| Joyce    | A     | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX       | F   | 25000.0 | 333445555 | 5   |
| Ahmad    | V     | Jabbar  | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX      | M   | 25000.0 | 987654321 | 4   |
| James    | E     | Borg    | 888665555 | 1937-11-10 | 450 Stone, Houston, TX       | M   | 55000.0 | NULL      | 1   |
| Maya     | R     | Sharma  | 777665555 | 1978-04-11 | 12 IT Park, Houston, TX      | F   | 61000.0 | 888665555 | 10  |
| Lina     | M     | Das     | 222334444 | 1980-02-02 | 9 Bellaire Ave, Bellaire, TX | F   | 52000.0 | 777665555 | 10  |
| Raj      | P     | Mehta   | 111223333 | 1975-03-03 | 88 Staff Road, Stafford, TX  | M   | 58000.0 | 777665555 | 10  |
| Temp     | Q     | Manager | 12345     | 1985-05-05 | 44 Support Ln, Houston, TX   | M   | 45000.0 | 888665555 | 6   |
| Tina     | L     | Ray     | 555666777 | 1990-01-01 | 55 Support Ln, Houston, TX   | F   | 39000.0 | 12345     | 6   |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
13 rows in set (0.00 sec)

mysql> SELECT * FROM DEPARTMENT;
+----------------+---------+-----------+--------------+
| DNAME          | DNUMBER | MGRSSN    | MGRSTARTDATE |
+----------------+---------+-----------+--------------+
| Headquarters   | 1       | 888665555 | 1981-06-19   |
| Administration | 4       | 987654321 | 1995-01-01   |
| Research       | 5       | 333445555 | 1988-05-22   |
| Support        | 6       | 12345     | 2018-01-01   |
| Marketing      | 7       | 666884444 | 2000-01-01   |
| IT             | 10      | 777665555 | 2003-03-15   |
+----------------+---------+-----------+--------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM PROJECT;
+-----------------+---------+-----------+------+
| PNAME           | PNUMBER | PLOCATION | DNUM |
+-----------------+---------+-----------+------+
| ProductX        | 1       | Bellaire  | 5    |
| ProductY        | 2       | Sugarland | 5    |
| ProductZ        | 3       | Houston   | 5    |
| Computerization | 10      | Stafford  | 4    |
| Reorganization  | 20      | Houston   | 1    |
| Newbenefits     | 30      | Stafford  | 4    |
| MarketPulse     | 40      | Bellaire  | 7    |
| CloudShift      | 50      | Houston   | 10   |
+-----------------+---------+-----------+------+
8 rows in set (0.00 sec)
```

## 1: Display all details of all employees working in the company.

```sql
SELECT * FROM EMPLOYEE;
```

```
mysql> SELECT * FROM EMPLOYEE;
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME   | SSN       | BDATE      | ADDRESS                      | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| John     | B     | Smith   | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX     | M   | 30000.0 | 333445555 | 5   |
| Franklin | T     | Wong    | 333445555 | 1955-12-08 | 638 Voss, Houston, TX        | M   | 40000.0 | 888665555 | 5   |
| Alicia   | J     | Zelaya  | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX      | F   | 25000.0 | 987654321 | 4   |
| Jennifer | S     | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX      | F   | 43000.0 | 888665555 | 4   |
| Ramesh   | K     | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX     | M   | 38000.0 | 333445555 | 5   |
| Joyce    | A     | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX       | F   | 25000.0 | 333445555 | 5   |
| Ahmad    | V     | Jabbar  | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX      | M   | 25000.0 | 987654321 | 4   |
| James    | E     | Borg    | 888665555 | 1937-11-10 | 450 Stone, Houston, TX       | M   | 55000.0 | NULL      | 1   |
| Maya     | R     | Sharma  | 777665555 | 1978-04-11 | 12 IT Park, Houston, TX      | F   | 61000.0 | 888665555 | 10  |
| Lina     | M     | Das     | 222334444 | 1980-02-02 | 9 Bellaire Ave, Bellaire, TX | F   | 52000.0 | 777665555 | 10  |
| Raj      | P     | Mehta   | 111223333 | 1975-03-03 | 88 Staff Road, Stafford, TX  | M   | 58000.0 | 777665555 | 10  |
| Temp     | Q     | Manager | 12345     | 1985-05-05 | 44 Support Ln, Houston, TX   | M   | 45000.0 | 888665555 | 6   |
| Tina     | L     | Ray     | 555666777 | 1990-01-01 | 55 Support Ln, Houston, TX   | F   | 39000.0 | 12345     | 6   |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
13 rows in set (0.00 sec)
```

## 2: Display ssn, lname, fname, address of employees who work in department no 7.

```sql
SELECT SSN, LNAME, FNAME, ADDRESS FROM EMPLOYEE WHERE DNO = 7;
```

```
mysql> SELECT SSN, LNAME, FNAME, ADDRESS FROM EMPLOYEE WHERE DNO = 7;
+-----+-------+-------+---------+
| SSN | LNAME | FNAME | ADDRESS |
+-----+-------+-------+---------+
+-----+-------+-------+---------+
Empty set (0.00 sec)
```

## 3: Retrieve the birthdate and address of Franklin T. Wong.

```sql
SELECT BDATE, ADDRESS FROM EMPLOYEE WHERE FNAME='Franklin' AND MINIT='T' AND LNAME='Wong';
```

```
mysql> SELECT BDATE, ADDRESS FROM EMPLOYEE WHERE FNAME='Franklin' AND MINIT='T' AND LNAME='Wong';
+------------+-----------------------+
| BDATE      | ADDRESS               |
+------------+-----------------------+
| 1955-12-08 | 638 Voss, Houston, TX |
+------------+-----------------------+
1 row in set (0.00 sec)
```

## 4: Retrieve the name and salary of every employee.

```sql
SELECT FNAME || ' ' || COALESCE(MINIT || ' ', '') || LNAME AS EMP_NAME, SALARY FROM EMPLOYEE;
```

```
mysql> SELECT FNAME || ' ' || COALESCE(MINIT || ' ', '') || LNAME AS EMP_NAME, SALARY FROM EMPLOYEE;
+--------------------+---------+
| EMP_NAME           | SALARY  |
+--------------------+---------+
| John B Smith       | 30000.0 |
| Franklin T Wong    | 40000.0 |
| Alicia J Zelaya    | 25000.0 |
| Jennifer S Wallace | 43000.0 |
| Ramesh K Narayan   | 38000.0 |
| Joyce A English    | 25000.0 |
| Ahmad V Jabbar     | 25000.0 |
| James E Borg       | 55000.0 |
| Maya R Sharma      | 61000.0 |
| Lina M Das         | 52000.0 |
| Raj P Mehta        | 58000.0 |
| Temp Q Manager     | 45000.0 |
| Tina L Ray         | 39000.0 |
+--------------------+---------+
13 rows in set (0.00 sec)
```

## 5: Retrieve all distinct salary values.

```sql
SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY;
```

```
mysql> SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY;
+---------+
| SALARY  |
+---------+
| 25000.0 |
| 30000.0 |
| 38000.0 |
| 39000.0 |
| 40000.0 |
| 43000.0 |
| 45000.0 |
| 52000.0 |
| 55000.0 |
| 58000.0 |
| 61000.0 |
+---------+
11 rows in set (0.00 sec)
```

## 6: Retrieve all employee names whose address is in Bellaire.

```sql
SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE ADDRESS LIKE '%Bellaire%';
```

```
mysql> SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE ADDRESS LIKE '%Bellaire%';
+----------+-------+---------+
| FNAME    | MINIT | LNAME   |
+----------+-------+---------+
| Jennifer | S     | Wallace |
| Lina     | M     | Das     |
+----------+-------+---------+
2 rows in set (0.00 sec)
```

## 7: Retrieve all employees who were born during the 1950s.

```sql
SELECT * FROM EMPLOYEE WHERE BDATE BETWEEN '1950-01-01' AND '1959-12-31';
```

```
mysql> SELECT * FROM EMPLOYEE WHERE BDATE BETWEEN '1950-01-01' AND '1959-12-31';
+----------+-------+-------+-----------+------------+-----------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME | SSN       | BDATE      | ADDRESS               | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+-------+-----------+------------+-----------------------+-----+---------+-----------+-----+
| Franklin | T     | Wong  | 333445555 | 1955-12-08 | 638 Voss, Houston, TX | M   | 40000.0 | 888665555 | 5   |
+----------+-------+-------+-----------+------------+-----------------------+-----+---------+-----------+-----+
1 row in set (0.00 sec)
```

## 8: Retrieve all employees in department 5 with salary between 50000 and 60000.

```sql
SELECT * FROM EMPLOYEE WHERE DNO = 5 AND SALARY BETWEEN 50000 AND 60000;
```

```
mysql> SELECT * FROM EMPLOYEE WHERE DNO = 5 AND SALARY BETWEEN 50000 AND 60000;
+-------+-------+-------+-----+-------+---------+-----+--------+----------+-----+
| FNAME | MINIT | LNAME | SSN | BDATE | ADDRESS | SEX | SALARY | SUPERSSN | DNO |
+-------+-------+-------+-----+-------+---------+-----+--------+----------+-----+
+-------+-------+-------+-----+-------+---------+-----+--------+----------+-----+
Empty set (0.00 sec)
```

## 9: Retrieve names of all employees who do not have supervisors.

```sql
SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SUPERSSN IS NULL;
```

```
mysql> SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SUPERSSN IS NULL;
+-------+-------+-------+
| FNAME | MINIT | LNAME |
+-------+-------+-------+
| James | E     | Borg  |
+-------+-------+-------+
1 row in set (0.00 sec)
```

## 10: Retrieve SSN and department name for all employees.

```sql
SELECT E.SSN, D.DNAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DNO = D.DNUMBER;
```

```
mysql> SELECT E.SSN, D.DNAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DNO = D.DNUMBER;
+-----------+----------------+
| SSN       | DNAME          |
+-----------+----------------+
| 123456789 | Research       |
| 333445555 | Research       |
| 999887777 | Administration |
| 987654321 | Administration |
| 666884444 | Research       |
| 453453453 | Research       |
| 987987987 | Administration |
| 888665555 | Headquarters   |
| 777665555 | IT             |
| 222334444 | IT             |
| 111223333 | IT             |
| 12345     | Support        |
| 555666777 | Support        |
+-----------+----------------+
13 rows in set (0.00 sec)
```

## 11: Retrieve name and address of employees in Research department.

```sql
SELECT E.FNAME, E.MINIT, E.LNAME, E.ADDRESS FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO = D.DNUMBER WHERE D.DNAME='Research';
```

```
mysql> SELECT E.FNAME, E.MINIT, E.LNAME, E.ADDRESS FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO = D.DNUMBER WHERE D.DNAME='Research';
+----------+-------+---------+--------------------------+
| FNAME    | MINIT | LNAME   | ADDRESS                  |
+----------+-------+---------+--------------------------+
| John     | B     | Smith   | 731 Fondren, Houston, TX |
| Franklin | T     | Wong    | 638 Voss, Houston, TX    |
| Ramesh   | K     | Narayan | 975 Fire Oak, Humble, TX |
| Joyce    | A     | English | 5631 Rice, Houston, TX   |
+----------+-------+---------+--------------------------+
4 rows in set (0.00 sec)
```

## 12: For each Stafford project, list project no, controlling dept no, manager lname, address, birthdate.

```sql
SELECT P.PNUMBER, P.DNUM, M.LNAME, M.ADDRESS, M.BDATE FROM PROJECT P JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE P.PLOCATION='Stafford';
```

```
mysql> SELECT P.PNUMBER, P.DNUM, M.LNAME, M.ADDRESS, M.BDATE FROM PROJECT P JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE P.PLOCATION='Stafford';
+---------+------+---------+-------------------------+------------+
| PNUMBER | DNUM | LNAME   | ADDRESS                 | BDATE      |
+---------+------+---------+-------------------------+------------+
| 10      | 4    | Wallace | 291 Berry, Bellaire, TX | 1941-06-20 |
| 30      | 4    | Wallace | 291 Berry, Bellaire, TX | 1941-06-20 |
+---------+------+---------+-------------------------+------------+
2 rows in set (0.00 sec)
```

## 13: For each employee retrieve employee name and immediate supervisor name.

```sql
SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, S.FNAME || ' ' || S.LNAME AS SUPERVISOR_NAME FROM EMPLOYEE E LEFT JOIN EMPLOYEE S ON E.SUPERSSN=S.SSN;
```

```
mysql> SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, S.FNAME || ' ' || S.LNAME AS SUPERVISOR_NAME FROM EMPLOYEE E LEFT JOIN EMPLOYEE S ON E.SUPERSSN=S.SSN;
+------------------+------------------+
| EMPLOYEE_NAME    | SUPERVISOR_NAME  |
+------------------+------------------+
| John Smith       | Franklin Wong    |
| Franklin Wong    | James Borg       |
| Alicia Zelaya    | Jennifer Wallace |
| Jennifer Wallace | James Borg       |
| Ramesh Narayan   | Franklin Wong    |
| Joyce English    | Franklin Wong    |
| Ahmad Jabbar     | Jennifer Wallace |
| James Borg       | NULL             |
| Maya Sharma      | James Borg       |
| Lina Das         | Maya Sharma      |
| Raj Mehta        | Maya Sharma      |
| Temp Manager     | James Borg       |
| Tina Ray         | Temp Manager     |
+------------------+------------------+
13 rows in set (0.00 sec)
```

## 14: Retrieve all combinations of Employee Name and Department Name.

```sql
SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, D.DNAME FROM EMPLOYEE E CROSS JOIN DEPARTMENT D;
```

```
mysql> SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, D.DNAME FROM EMPLOYEE E CROSS JOIN DEPARTMENT D;
+------------------+----------------+
| EMPLOYEE_NAME    | DNAME          |
+------------------+----------------+
| John Smith       | Administration |
| John Smith       | Headquarters   |
| John Smith       | IT             |
| John Smith       | Marketing      |
| John Smith       | Research       |
| John Smith       | Support        |
| Franklin Wong    | Administration |
| Franklin Wong    | Headquarters   |
| Franklin Wong    | IT             |
| Franklin Wong    | Marketing      |
| Franklin Wong    | Research       |
| Franklin Wong    | Support        |
| Alicia Zelaya    | Administration |
| Alicia Zelaya    | Headquarters   |
| Alicia Zelaya    | IT             |
| Alicia Zelaya    | Marketing      |
| Alicia Zelaya    | Research       |
| Alicia Zelaya    | Support        |
| Jennifer Wallace | Administration |
| Jennifer Wallace | Headquarters   |
| Jennifer Wallace | IT             |
| Jennifer Wallace | Marketing      |
| Jennifer Wallace | Research       |
| Jennifer Wallace | Support        |
| Ramesh Narayan   | Administration |
| Ramesh Narayan   | Headquarters   |
| Ramesh Narayan   | IT             |
| Ramesh Narayan   | Marketing      |
| Ramesh Narayan   | Research       |
| Ramesh Narayan   | Support        |
| Joyce English    | Administration |
| Joyce English    | Headquarters   |
| Joyce English    | IT             |
| Joyce English    | Marketing      |
| Joyce English    | Research       |
| Joyce English    | Support        |
| Ahmad Jabbar     | Administration |
| Ahmad Jabbar     | Headquarters   |
| Ahmad Jabbar     | IT             |
| Ahmad Jabbar     | Marketing      |
| Ahmad Jabbar     | Research       |
| Ahmad Jabbar     | Support        |
| James Borg       | Administration |
| James Borg       | Headquarters   |
| James Borg       | IT             |
| James Borg       | Marketing      |
| James Borg       | Research       |
| James Borg       | Support        |
| Maya Sharma      | Administration |
| Maya Sharma      | Headquarters   |
| Maya Sharma      | IT             |
| Maya Sharma      | Marketing      |
| Maya Sharma      | Research       |
| Maya Sharma      | Support        |
| Lina Das         | Administration |
| Lina Das         | Headquarters   |
| Lina Das         | IT             |
| Lina Das         | Marketing      |
| Lina Das         | Research       |
| Lina Das         | Support        |
| Raj Mehta        | Administration |
| Raj Mehta        | Headquarters   |
| Raj Mehta        | IT             |
| Raj Mehta        | Marketing      |
| Raj Mehta        | Research       |
| Raj Mehta        | Support        |
| Temp Manager     | Administration |
| Temp Manager     | Headquarters   |
| Temp Manager     | IT             |
| Temp Manager     | Marketing      |
| Temp Manager     | Research       |
| Temp Manager     | Support        |
| Tina Ray         | Administration |
| Tina Ray         | Headquarters   |
| Tina Ray         | IT             |
| Tina Ray         | Marketing      |
| Tina Ray         | Research       |
| Tina Ray         | Support        |
+------------------+----------------+
78 rows in set (0.00 sec)
```

## 15: List project numbers that involve Narayan as worker or department manager.

```sql
SELECT DISTINCT P.PNUMBER FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO LEFT JOIN EMPLOYEE E ON W.ESSN=E.SSN LEFT JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER LEFT JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE E.LNAME='Narayan' OR M.LNAME='Narayan';
```

```
mysql> SELECT DISTINCT P.PNUMBER FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO LEFT JOIN EMPLOYEE E ON W.ESSN=E.SSN LEFT JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER LEFT JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE E.LNAME='Narayan' OR M.LNAME='Narayan';
+---------+
| PNUMBER |
+---------+
| 3       |
| 40      |
+---------+
2 rows in set (0.00 sec)
```

## 16: Increase salary by 15% for employees working on ProductX and show name + increased salary.

```sql
SELECT E.FNAME || ' ' || E.LNAME AS EMP_NAME, ROUND(E.SALARY * 1.15, 2) AS INCREASED_SALARY FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PNAME='ProductX';
```

```
mysql> SELECT E.FNAME || ' ' || E.LNAME AS EMP_NAME, ROUND(E.SALARY * 1.15, 2) AS INCREASED_SALARY FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PNAME='ProductX';
+---------------+------------------+
| EMP_NAME      | INCREASED_SALARY |
+---------------+------------------+
| John Smith    | 34500.0          |
| Joyce English | 28750.0          |
+---------------+------------------+
2 rows in set (0.00 sec)
```

## 17: Employees and project name each works in, ordered by department then first name.

```sql
SELECT E.DNO, E.FNAME, E.LNAME, P.PNAME FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER ORDER BY E.DNO, E.FNAME;
```

```
mysql> SELECT E.DNO, E.FNAME, E.LNAME, P.PNAME FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER ORDER BY E.DNO, E.FNAME;
+-----+----------+---------+-----------------+
| DNO | FNAME    | LNAME   | PNAME           |
+-----+----------+---------+-----------------+
| 1   | James    | Borg    | Reorganization  |
| 4   | Ahmad    | Jabbar  | Computerization |
| 4   | Ahmad    | Jabbar  | Newbenefits     |
| 4   | Alicia   | Zelaya  | Computerization |
| 4   | Alicia   | Zelaya  | Newbenefits     |
| 4   | Jennifer | Wallace | Reorganization  |
| 4   | Jennifer | Wallace | Newbenefits     |
| 5   | Franklin | Wong    | ProductY        |
| 5   | Franklin | Wong    | ProductZ        |
| 5   | Franklin | Wong    | Computerization |
| 5   | Franklin | Wong    | Reorganization  |
| 5   | John     | Smith   | ProductX        |
| 5   | John     | Smith   | ProductY        |
| 5   | Joyce    | English | ProductX        |
| 5   | Joyce    | English | ProductY        |
| 5   | Ramesh   | Narayan | ProductZ        |
| 6   | Temp     | Manager | MarketPulse     |
| 6   | Tina     | Ray     | MarketPulse     |
| 10  | Lina     | Das     | CloudShift      |
| 10  | Maya     | Sharma  | CloudShift      |
| 10  | Raj      | Mehta   | CloudShift      |
+-----+----------+---------+-----------------+
21 rows in set (0.00 sec)
```

## 18: Employees whose salary does not match salary of any employee in department 10.

```sql
SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY NOT IN (SELECT SALARY FROM EMPLOYEE WHERE DNO=10);
```

```
mysql> SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY NOT IN (SELECT SALARY FROM EMPLOYEE WHERE DNO=10);
+----------+-------+---------+
| FNAME    | MINIT | LNAME   |
+----------+-------+---------+
| John     | B     | Smith   |
| Franklin | T     | Wong    |
| Alicia   | J     | Zelaya  |
| Jennifer | S     | Wallace |
| Ramesh   | K     | Narayan |
| Joyce    | A     | English |
| Ahmad    | V     | Jabbar  |
| James    | E     | Borg    |
| Temp     | Q     | Manager |
| Tina     | L     | Ray     |
+----------+-------+---------+
10 rows in set (0.00 sec)
```

## 19: Employees with dependent having same first name and same sex as employee.

```sql
SELECT DISTINCT E.FNAME, E.LNAME FROM EMPLOYEE E JOIN DEPENDENT D ON E.SSN=D.ESSN WHERE E.FNAME=D.DEPENDENT_NAME AND E.SEX=D.SEX;
```

```
mysql> SELECT DISTINCT E.FNAME, E.LNAME FROM EMPLOYEE E JOIN DEPENDENT D ON E.SSN=D.ESSN WHERE E.FNAME=D.DEPENDENT_NAME AND E.SEX=D.SEX;
+-------+---------+
| FNAME | LNAME   |
+-------+---------+
| Temp  | Manager |
+-------+---------+
1 row in set (0.00 sec)
```

## 20: Employee numbers of employees who work on project in Bellaire/Houston/Stafford.

```sql
SELECT DISTINCT W.ESSN FROM WORKS_ON W JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PLOCATION IN ('Bellaire','Houston','Stafford');
```

```
mysql> SELECT DISTINCT W.ESSN FROM WORKS_ON W JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PLOCATION IN ('Bellaire','Houston','Stafford');
+-----------+
| ESSN      |
+-----------+
| 111223333 |
| 12345     |
| 123456789 |
| 222334444 |
| 333445555 |
| 453453453 |
| 555666777 |
| 666884444 |
| 777665555 |
| 888665555 |
| 987654321 |
| 987987987 |
| 999887777 |
+-----------+
13 rows in set (0.00 sec)
```

## 21: Sum, max, min, avg salary of all employees.

```sql
SELECT SUM(SALARY) AS TOTAL_SALARY, MAX(SALARY) AS MAX_SALARY, MIN(SALARY) AS MIN_SALARY, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE;
```

```
mysql> SELECT SUM(SALARY) AS TOTAL_SALARY, MAX(SALARY) AS MAX_SALARY, MIN(SALARY) AS MIN_SALARY, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE;
+--------------+------------+------------+------------+
| TOTAL_SALARY | MAX_SALARY | MIN_SALARY | AVG_SALARY |
+--------------+------------+------------+------------+
| 536000.0     | 61000.0    | 25000.0    | 41230.77   |
+--------------+------------+------------+------------+
1 row in set (0.00 sec)
```

## 22: Salary aggregates and employee count for Marketing department.

```sql
SELECT COUNT(*) AS EMP_COUNT, SUM(E.SALARY) AS TOTAL_SALARY, MAX(E.SALARY) AS MAX_SALARY, MIN(E.SALARY) AS MIN_SALARY, ROUND(AVG(E.SALARY),2) AS AVG_SALARY FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO=D.DNUMBER WHERE D.DNAME='Marketing';
```

```
mysql> SELECT COUNT(*) AS EMP_COUNT, SUM(E.SALARY) AS TOTAL_SALARY, MAX(E.SALARY) AS MAX_SALARY, MIN(E.SALARY) AS MIN_SALARY, ROUND(AVG(E.SALARY),2) AS AVG_SALARY FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO=D.DNUMBER WHERE D.DNAME='Marketing';
+-----------+--------------+------------+------------+------------+
| EMP_COUNT | TOTAL_SALARY | MAX_SALARY | MIN_SALARY | AVG_SALARY |
+-----------+--------------+------------+------------+------------+
| 0         | NULL         | NULL       | NULL       | NULL       |
+-----------+--------------+------------+------------+------------+
1 row in set (0.00 sec)
```

## 23: Employees whose salary is greater than average salary of department 10.

```sql
SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE WHERE DNO=10);
```

```
mysql> SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE WHERE DNO=10);
+-------+-------+--------+
| FNAME | MINIT | LNAME  |
+-------+-------+--------+
| Maya  | R     | Sharma |
| Raj   | P     | Mehta  |
+-------+-------+--------+
2 rows in set (0.00 sec)
```

## 24: For each department retrieve dept no, employee count, avg salary.

```sql
SELECT DNO AS DEPT_NO, COUNT(*) AS EMP_COUNT, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE GROUP BY DNO;
```

```
mysql> SELECT DNO AS DEPT_NO, COUNT(*) AS EMP_COUNT, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE GROUP BY DNO;
+---------+-----------+------------+
| DEPT_NO | EMP_COUNT | AVG_SALARY |
+---------+-----------+------------+
| 1       | 1         | 55000.0    |
| 4       | 3         | 31000.0    |
| 5       | 4         | 33250.0    |
| 6       | 2         | 42000.0    |
| 10      | 3         | 57000.0    |
+---------+-----------+------------+
5 rows in set (0.00 sec)
```

## 25: For each project retrieve project no, project name, number of employees.

```sql
SELECT P.PNUMBER, P.PNAME, COUNT(W.ESSN) AS EMP_COUNT FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO GROUP BY P.PNUMBER, P.PNAME;
```

```
mysql> SELECT P.PNUMBER, P.PNAME, COUNT(W.ESSN) AS EMP_COUNT FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO GROUP BY P.PNUMBER, P.PNAME;
+---------+-----------------+-----------+
| PNUMBER | PNAME           | EMP_COUNT |
+---------+-----------------+-----------+
| 50      | CloudShift      | 3         |
| 10      | Computerization | 3         |
| 40      | MarketPulse     | 2         |
| 30      | Newbenefits     | 3         |
| 1       | ProductX        | 2         |
| 2       | ProductY        | 3         |
| 3       | ProductZ        | 2         |
| 20      | Reorganization  | 3         |
+---------+-----------------+-----------+
8 rows in set (0.00 sec)
```

## 26: Change location and department for projects with >5 employees.

```sql
UPDATE PROJECT SET PLOCATION='Bellaire', DNUM=6 WHERE PNUMBER IN (SELECT PNO FROM WORKS_ON GROUP BY PNO HAVING COUNT(ESSN) > 5);
```

```
mysql> UPDATE PROJECT SET PLOCATION='Bellaire', DNUM=6 WHERE PNUMBER IN (SELECT PNO FROM WORKS_ON GROUP BY PNO HAVING COUNT(ESSN) > 5);
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM PROJECT;
+-----------------+---------+-----------+------+
| PNAME           | PNUMBER | PLOCATION | DNUM |
+-----------------+---------+-----------+------+
| ProductX        | 1       | Bellaire  | 5    |
| ProductY        | 2       | Sugarland | 5    |
| ProductZ        | 3       | Houston   | 5    |
| Computerization | 10      | Stafford  | 4    |
| Reorganization  | 20      | Houston   | 1    |
| Newbenefits     | 30      | Stafford  | 4    |
| MarketPulse     | 40      | Bellaire  | 7    |
| CloudShift      | 50      | Houston   | 10   |
+-----------------+---------+-----------+------+
8 rows in set (0.00 sec)
```

## 27: For each department with >10 employees, count employees with salary >40000.

```sql
SELECT DNO AS DEPT_NO, SUM(CASE WHEN SALARY > 40000 THEN 1 ELSE 0 END) AS GT_40000_COUNT FROM EMPLOYEE GROUP BY DNO HAVING COUNT(*) > 10;
```

```
mysql> SELECT DNO AS DEPT_NO, SUM(CASE WHEN SALARY > 40000 THEN 1 ELSE 0 END) AS GT_40000_COUNT FROM EMPLOYEE GROUP BY DNO HAVING COUNT(*) > 10;
+---------+----------------+
| DEPT_NO | GT_40000_COUNT |
+---------+----------------+
+---------+----------------+
Empty set (0.00 sec)
```

## 28: Insert violating PROJECT record.

```sql
INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);
```

```
mysql> INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);
ERROR 1452 (23000): FOREIGN KEY constraint failed

mysql> SELECT * FROM DEPARTMENT;
+----------------+---------+-----------+--------------+
| DNAME          | DNUMBER | MGRSSN    | MGRSTARTDATE |
+----------------+---------+-----------+--------------+
| Headquarters   | 1       | 888665555 | 1981-06-19   |
| Administration | 4       | 987654321 | 1995-01-01   |
| Research       | 5       | 333445555 | 1988-05-22   |
| Support        | 6       | 12345     | 2018-01-01   |
| Marketing      | 7       | 666884444 | 2000-01-01   |
| IT             | 10      | 777665555 | 2003-03-15   |
+----------------+---------+-----------+--------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM PROJECT;
+-----------------+---------+-----------+------+
| PNAME           | PNUMBER | PLOCATION | DNUM |
+-----------------+---------+-----------+------+
| ProductX        | 1       | Bellaire  | 5    |
| ProductY        | 2       | Sugarland | 5    |
| ProductZ        | 3       | Houston   | 5    |
| Computerization | 10      | Stafford  | 4    |
| Reorganization  | 20      | Houston   | 1    |
| Newbenefits     | 30      | Stafford  | 4    |
| MarketPulse     | 40      | Bellaire  | 7    |
| CloudShift      | 50      | Houston   | 10   |
+-----------------+---------+-----------+------+
8 rows in set (0.00 sec)
```

## 28: Fix violation by inserting DEPARTMENT record.

```sql
INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES ('TempDept', 99, '888665555', '2020-01-01');
```

```
mysql> INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES ('TempDept', 99, '888665555', '2020-01-01');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM DEPARTMENT;
+----------------+---------+-----------+--------------+
| DNAME          | DNUMBER | MGRSSN    | MGRSTARTDATE |
+----------------+---------+-----------+--------------+
| Headquarters   | 1       | 888665555 | 1981-06-19   |
| Administration | 4       | 987654321 | 1995-01-01   |
| Research       | 5       | 333445555 | 1988-05-22   |
| Support        | 6       | 12345     | 2018-01-01   |
| Marketing      | 7       | 666884444 | 2000-01-01   |
| IT             | 10      | 777665555 | 2003-03-15   |
| TempDept       | 99      | 888665555 | 2020-01-01   |
+----------------+---------+-----------+--------------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM PROJECT;
+-----------------+---------+-----------+------+
| PNAME           | PNUMBER | PLOCATION | DNUM |
+-----------------+---------+-----------+------+
| ProductX        | 1       | Bellaire  | 5    |
| ProductY        | 2       | Sugarland | 5    |
| ProductZ        | 3       | Houston   | 5    |
| Computerization | 10      | Stafford  | 4    |
| Reorganization  | 20      | Houston   | 1    |
| Newbenefits     | 30      | Stafford  | 4    |
| MarketPulse     | 40      | Bellaire  | 7    |
| CloudShift      | 50      | Houston   | 10   |
+-----------------+---------+-----------+------+
8 rows in set (0.00 sec)
```

## 28: Reinsert previously violating PROJECT record.

```sql
INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);
```

```
mysql> INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM DEPARTMENT;
+----------------+---------+-----------+--------------+
| DNAME          | DNUMBER | MGRSSN    | MGRSTARTDATE |
+----------------+---------+-----------+--------------+
| Headquarters   | 1       | 888665555 | 1981-06-19   |
| Administration | 4       | 987654321 | 1995-01-01   |
| Research       | 5       | 333445555 | 1988-05-22   |
| Support        | 6       | 12345     | 2018-01-01   |
| Marketing      | 7       | 666884444 | 2000-01-01   |
| IT             | 10      | 777665555 | 2003-03-15   |
| TempDept       | 99      | 888665555 | 2020-01-01   |
+----------------+---------+-----------+--------------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM PROJECT;
+-----------------+---------+-----------+------+
| PNAME           | PNUMBER | PLOCATION | DNUM |
+-----------------+---------+-----------+------+
| ProductX        | 1       | Bellaire  | 5    |
| ProductY        | 2       | Sugarland | 5    |
| ProductZ        | 3       | Houston   | 5    |
| Computerization | 10      | Stafford  | 4    |
| Reorganization  | 20      | Houston   | 1    |
| Newbenefits     | 30      | Stafford  | 4    |
| MarketPulse     | 40      | Bellaire  | 7    |
| CloudShift      | 50      | Houston   | 10   |
| BrokenRef       | 99      | Nowhere   | 99   |
+-----------------+---------+-----------+------+
9 rows in set (0.00 sec)
```

## 29: Delete all dependents of employee 123456789.

```sql
DELETE FROM DEPENDENT WHERE ESSN='123456789';
```

```
mysql> DELETE FROM DEPENDENT WHERE ESSN='123456789';
Query OK, 3 rows affected (0.00 sec)

mysql> SELECT * FROM DEPENDENT;
+-----------+----------------+-----+------------+--------------+
| ESSN      | DEPENDENT_NAME | SEX | BDATE      | RELATIONSHIP |
+-----------+----------------+-----+------------+--------------+
| 333445555 | Alice          | F   | 1986-04-05 | Daughter     |
| 333445555 | Theodore       | M   | 1983-10-25 | Son          |
| 333445555 | Joy            | F   | 1958-05-03 | Spouse       |
| 987654321 | Abner          | M   | 1942-02-28 | Spouse       |
| 12345     | Temp           | M   | 2012-08-08 | Son          |
+-----------+----------------+-----+------------+--------------+
5 rows in set (0.00 sec)
```

## 30: Delete employee 12345 to observe cascading/set default/set null behavior.

```sql
DELETE FROM EMPLOYEE WHERE SSN='12345';
```

```
mysql> DELETE FROM EMPLOYEE WHERE SSN='12345';
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM EMPLOYEE;
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME   | SSN       | BDATE      | ADDRESS                      | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| John     | B     | Smith   | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX     | M   | 30000.0 | 333445555 | 5   |
| Franklin | T     | Wong    | 333445555 | 1955-12-08 | 638 Voss, Houston, TX        | M   | 40000.0 | 888665555 | 5   |
| Alicia   | J     | Zelaya  | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX      | F   | 25000.0 | 987654321 | 4   |
| Jennifer | S     | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX      | F   | 43000.0 | 888665555 | 4   |
| Ramesh   | K     | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX     | M   | 38000.0 | 333445555 | 5   |
| Joyce    | A     | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX       | F   | 25000.0 | 333445555 | 5   |
| Ahmad    | V     | Jabbar  | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX      | M   | 25000.0 | 987654321 | 4   |
| James    | E     | Borg    | 888665555 | 1937-11-10 | 450 Stone, Houston, TX       | M   | 55000.0 | NULL      | 1   |
| Maya     | R     | Sharma  | 777665555 | 1978-04-11 | 12 IT Park, Houston, TX      | F   | 61000.0 | 888665555 | 10  |
| Lina     | M     | Das     | 222334444 | 1980-02-02 | 9 Bellaire Ave, Bellaire, TX | F   | 52000.0 | 777665555 | 10  |
| Raj      | P     | Mehta   | 111223333 | 1975-03-03 | 88 Staff Road, Stafford, TX  | M   | 58000.0 | 777665555 | 10  |
| Tina     | L     | Ray     | 555666777 | 1990-01-01 | 55 Support Ln, Houston, TX   | F   | 39000.0 | NULL      | 6   |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
12 rows in set (0.00 sec)

mysql> SELECT * FROM DEPENDENT;
+-----------+----------------+-----+------------+--------------+
| ESSN      | DEPENDENT_NAME | SEX | BDATE      | RELATIONSHIP |
+-----------+----------------+-----+------------+--------------+
| 333445555 | Alice          | F   | 1986-04-05 | Daughter     |
| 333445555 | Theodore       | M   | 1983-10-25 | Son          |
| 333445555 | Joy            | F   | 1958-05-03 | Spouse       |
| 987654321 | Abner          | M   | 1942-02-28 | Spouse       |
+-----------+----------------+-----+------------+--------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM WORKS_ON;
+-----------+-----+-------+
| ESSN      | PNO | HOURS |
+-----------+-----+-------+
| 123456789 | 1   | 32.5  |
| 123456789 | 2   | 7.5   |
| 666884444 | 3   | 40.0  |
| 453453453 | 1   | 20.0  |
| 453453453 | 2   | 20.0  |
| 333445555 | 2   | 10.0  |
| 333445555 | 3   | 10.0  |
| 333445555 | 10  | 10.0  |
| 333445555 | 20  | 10.0  |
| 999887777 | 30  | 30.0  |
| 999887777 | 10  | 10.0  |
| 987987987 | 10  | 35.0  |
| 987987987 | 30  | 5.0   |
| 987654321 | 30  | 20.0  |
| 987654321 | 20  | 15.0  |
| 888665555 | 20  | NULL  |
| 777665555 | 50  | 20.0  |
| 222334444 | 50  | 25.0  |
| 111223333 | 50  | 15.0  |
| 555666777 | 40  | 18.0  |
+-----------+-----+-------+
20 rows in set (0.00 sec)

mysql> SELECT * FROM DEPARTMENT;
+----------------+---------+-----------+--------------+
| DNAME          | DNUMBER | MGRSSN    | MGRSTARTDATE |
+----------------+---------+-----------+--------------+
| Headquarters   | 1       | 888665555 | 1981-06-19   |
| Administration | 4       | 987654321 | 1995-01-01   |
| Research       | 5       | 333445555 | 1988-05-22   |
| Support        | 6       | 888665555 | 2018-01-01   |
| Marketing      | 7       | 666884444 | 2000-01-01   |
| IT             | 10      | 777665555 | 2003-03-15   |
| TempDept       | 99      | 888665555 | 2020-01-01   |
+----------------+---------+-----------+--------------+
7 rows in set (0.00 sec)
```

## 31: Alter Employee table: add EMAIL column with unique constraint.

```sql
ALTER TABLE EMPLOYEE ADD COLUMN EMAIL TEXT UNIQUE;
```

```
mysql> ALTER TABLE EMPLOYEE ADD COLUMN EMAIL TEXT UNIQUE;
ERROR 1452 (23000): Cannot add a UNIQUE column

mysql> SELECT * FROM EMPLOYEE;
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME   | SSN       | BDATE      | ADDRESS                      | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| John     | B     | Smith   | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX     | M   | 30000.0 | 333445555 | 5   |
| Franklin | T     | Wong    | 333445555 | 1955-12-08 | 638 Voss, Houston, TX        | M   | 40000.0 | 888665555 | 5   |
| Alicia   | J     | Zelaya  | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX      | F   | 25000.0 | 987654321 | 4   |
| Jennifer | S     | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX      | F   | 43000.0 | 888665555 | 4   |
| Ramesh   | K     | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX     | M   | 38000.0 | 333445555 | 5   |
| Joyce    | A     | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX       | F   | 25000.0 | 333445555 | 5   |
| Ahmad    | V     | Jabbar  | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX      | M   | 25000.0 | 987654321 | 4   |
| James    | E     | Borg    | 888665555 | 1937-11-10 | 450 Stone, Houston, TX       | M   | 55000.0 | NULL      | 1   |
| Maya     | R     | Sharma  | 777665555 | 1978-04-11 | 12 IT Park, Houston, TX      | F   | 61000.0 | 888665555 | 10  |
| Lina     | M     | Das     | 222334444 | 1980-02-02 | 9 Bellaire Ave, Bellaire, TX | F   | 52000.0 | 777665555 | 10  |
| Raj      | P     | Mehta   | 111223333 | 1975-03-03 | 88 Staff Road, Stafford, TX  | M   | 58000.0 | 777665555 | 10  |
| Tina     | L     | Ray     | 555666777 | 1990-01-01 | 55 Support Ln, Houston, TX   | F   | 39000.0 | NULL      | 6   |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
12 rows in set (0.00 sec)
```

## 31: Alter Employee table: drop EMAIL column.

```sql
ALTER TABLE EMPLOYEE DROP COLUMN EMAIL;
```

```
mysql> ALTER TABLE EMPLOYEE DROP COLUMN EMAIL;
ERROR 1452 (23000): no such column: "EMAIL"

mysql> SELECT * FROM EMPLOYEE;
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| FNAME    | MINIT | LNAME   | SSN       | BDATE      | ADDRESS                      | SEX | SALARY  | SUPERSSN  | DNO |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
| John     | B     | Smith   | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX     | M   | 30000.0 | 333445555 | 5   |
| Franklin | T     | Wong    | 333445555 | 1955-12-08 | 638 Voss, Houston, TX        | M   | 40000.0 | 888665555 | 5   |
| Alicia   | J     | Zelaya  | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX      | F   | 25000.0 | 987654321 | 4   |
| Jennifer | S     | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX      | F   | 43000.0 | 888665555 | 4   |
| Ramesh   | K     | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX     | M   | 38000.0 | 333445555 | 5   |
| Joyce    | A     | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX       | F   | 25000.0 | 333445555 | 5   |
| Ahmad    | V     | Jabbar  | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX      | M   | 25000.0 | 987654321 | 4   |
| James    | E     | Borg    | 888665555 | 1937-11-10 | 450 Stone, Houston, TX       | M   | 55000.0 | NULL      | 1   |
| Maya     | R     | Sharma  | 777665555 | 1978-04-11 | 12 IT Park, Houston, TX      | F   | 61000.0 | 888665555 | 10  |
| Lina     | M     | Das     | 222334444 | 1980-02-02 | 9 Bellaire Ave, Bellaire, TX | F   | 52000.0 | 777665555 | 10  |
| Raj      | P     | Mehta   | 111223333 | 1975-03-03 | 88 Staff Road, Stafford, TX  | M   | 58000.0 | 777665555 | 10  |
| Tina     | L     | Ray     | 555666777 | 1990-01-01 | 55 Support Ln, Houston, TX   | F   | 39000.0 | NULL      | 6   |
+----------+-------+---------+-----------+------------+------------------------------+-----+---------+-----------+-----+
12 rows in set (0.00 sec)
```


## Create Tables

```sql
CREATE TABLE STUDENT (
    Roll_No     CHAR(6) PRIMARY KEY,
    StudentName VARCHAR(20),
    Course      VARCHAR(10),
    DOB         DATE
);
CREATE TABLE SOCIETY (
    SocID      CHAR(6) PRIMARY KEY,
    SocName    VARCHAR(20),
    MentorName VARCHAR(15),
    TotalSeats INT UNSIGNED
);
CREATE TABLE ENROLLMENT (
    Roll_No          CHAR(6),
    SID              CHAR(6),
    DateOfEnrollment DATE,
    PRIMARY KEY (Roll_No, SID),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (SID)     REFERENCES SOCIETY(SocID)
);
```

```
mysql> CREATE TABLE STUDENT (
    ->     Roll_No     CHAR(6) PRIMARY KEY,
    ->     StudentName VARCHAR(20),
    ->     Course      VARCHAR(10),
    ->     DOB         DATE
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE SOCIETY (
    ->     SocID      CHAR(6) PRIMARY KEY,
    ->     SocName    VARCHAR(20),
    ->     MentorName VARCHAR(15),
    ->     TotalSeats INT UNSIGNED
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE ENROLLMENT (
    ->     Roll_No          CHAR(6),
    ->     SID              CHAR(6),
    ->     DateOfEnrollment DATE,
    ->     PRIMARY KEY (Roll_No, SID),
    ->     FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    ->     FOREIGN KEY (SID)     REFERENCES SOCIETY(SocID)
    -> );
Query OK, 0 rows affected (0.00 sec)
```

## Insert Data

```sql
INSERT INTO STUDENT VALUES
('S00001','Aarav Kumar',  'computer s','2001-05-15'),
('S00002','Aditi Sharma', 'chemistry', '2002-08-20'),
('S00003','Rahul Verma',  'physics',   '2000-11-10'),
('X00009','Sneha Gupta',  'computer s','2001-02-25'),
('Z00009','Vikram Singh', 'maths',     '1999-07-30'),
('S00006','Priya Das',    'chemistry', '2003-01-12'),
('S00007','Amit Patel',   'english',   '2001-09-05'),
('S00008','Neha Jain',    'history',   '2002-04-18');

INSERT INTO SOCIETY VALUES
('s1','NSS',      'Mr. A Gupta',  50),
('s2','Debating', 'Ms. R Kaur',   30),
('s3','Dancing',  'Mr. S Sharma', 40),
('s4','Sashakt',  'Dr. V Gupta',  25),
('s5','Music',    'Ms. P Singh',  20),
('s6','Art',      'Mr. K Verma',  15);

INSERT INTO ENROLLMENT VALUES
('S00001','s1','2023-08-01'),
('S00001','s2','2023-08-05'),
('S00002','s3','2023-08-10'),
('S00003','s1','2023-08-12'),
('X00009','s4','2023-08-15'),
('S00006','s1','2023-08-20'),
('S00007','s2','2023-08-22'),
('S00008','s3','2023-08-25');
```

```
mysql> INSERT INTO STUDENT VALUES
    -> ('S00001','Aarav Kumar',  'computer s','2001-05-15'),
    -> ('S00002','Aditi Sharma', 'chemistry', '2002-08-20'),
    -> ('S00003','Rahul Verma',  'physics',   '2000-11-10'),
    -> ('X00009','Sneha Gupta',  'computer s','2001-02-25'),
    -> ('Z00009','Vikram Singh', 'maths',     '1999-07-30'),
    -> ('S00006','Priya Das',    'chemistry', '2003-01-12'),
    -> ('S00007','Amit Patel',   'english',   '2001-09-05'),
    -> ('S00008','Neha Jain',    'history',   '2002-04-18');
Query OK, 8 rows affected (0.00 sec)

mysql> INSERT INTO SOCIETY VALUES
    -> ('s1','NSS',      'Mr. A Gupta',  50),
    -> ('s2','Debating', 'Ms. R Kaur',   30),
    -> ('s3','Dancing',  'Mr. S Sharma', 40),
    -> ('s4','Sashakt',  'Dr. V Gupta',  25),
    -> ('s5','Music',    'Ms. P Singh',  20),
    -> ('s6','Art',      'Mr. K Verma',  15);
Query OK, 6 rows affected (0.00 sec)

mysql> INSERT INTO ENROLLMENT VALUES
    -> ('S00001','s1','2023-08-01'),
    -> ('S00001','s2','2023-08-05'),
    -> ('S00002','s3','2023-08-10'),
    -> ('S00003','s1','2023-08-12'),
    -> ('X00009','s4','2023-08-15'),
    -> ('S00006','s1','2023-08-20'),
    -> ('S00007','s2','2023-08-22'),
    -> ('S00008','s3','2023-08-25');
Query OK, 8 rows affected (0.00 sec)
```

## Initial Table Data

```sql
SELECT * FROM STUDENT;
SELECT * FROM SOCIETY;
SELECT * FROM ENROLLMENT;
```

```
mysql> SELECT * FROM STUDENT;
+---------+--------------+------------+------------+
| Roll_No | StudentName  | Course     | DOB        |
+---------+--------------+------------+------------+
| S00001  | Aarav Kumar  | computer s | 2001-05-15 |
| S00002  | Aditi Sharma | chemistry  | 2002-08-20 |
| S00003  | Rahul Verma  | physics    | 2000-11-10 |
| X00009  | Sneha Gupta  | computer s | 2001-02-25 |
| Z00009  | Vikram Singh | maths      | 1999-07-30 |
| S00006  | Priya Das    | chemistry  | 2003-01-12 |
| S00007  | Amit Patel   | english    | 2001-09-05 |
| S00008  | Neha Jain    | history    | 2002-04-18 |
+---------+--------------+------------+------------+
8 rows in set (0.00 sec)

mysql> SELECT * FROM SOCIETY;
+-------+----------+--------------+------------+
| SocID | SocName  | MentorName   | TotalSeats |
+-------+----------+--------------+------------+
| s1    | NSS      | Mr. A Gupta  | 50         |
| s2    | Debating | Ms. R Kaur   | 30         |
| s3    | Dancing  | Mr. S Sharma | 40         |
| s4    | Sashakt  | Dr. V Gupta  | 25         |
| s5    | Music    | Ms. P Singh  | 20         |
| s6    | Art      | Mr. K Verma  | 15         |
+-------+----------+--------------+------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM ENROLLMENT;
+---------+-----+------------------+
| Roll_No | SID | DateOfEnrollment |
+---------+-----+------------------+
| S00001  | s1  | 2023-08-01       |
| S00001  | s2  | 2023-08-05       |
| S00002  | s3  | 2023-08-10       |
| S00003  | s1  | 2023-08-12       |
| X00009  | s4  | 2023-08-15       |
| S00006  | s1  | 2023-08-20       |
| S00007  | s2  | 2023-08-22       |
| S00008  | s3  | 2023-08-25       |
+---------+-----+------------------+
8 rows in set (0.00 sec)
```

## 1: Retrieve names of students enrolled in any society.

```sql
SELECT DISTINCT s.StudentName
FROM STUDENT s
JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;
```

```
mysql> SELECT DISTINCT s.StudentName
    -> FROM STUDENT s
    -> JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;
+--------------+
| StudentName  |
+--------------+
| Aarav Kumar  |
| Aditi Sharma |
| Rahul Verma  |
| Priya Das    |
| Amit Patel   |
| Neha Jain    |
| Sneha Gupta  |
+--------------+
7 rows in set (0.00 sec)
```

## 2: Retrieve all society names.

```sql
SELECT SocName FROM SOCIETY;
```

```
mysql> SELECT SocName FROM SOCIETY;
+----------+
| SocName  |
+----------+
| NSS      |
| Debating |
| Dancing  |
| Sashakt  |
| Music    |
| Art      |
+----------+
6 rows in set (0.00 sec)
```

## 3: Retrieve students' names starting with the letter 'A'.

```sql
SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';
```

```
mysql> SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';
+--------------+
| StudentName  |
+--------------+
| Aarav Kumar  |
| Aditi Sharma |
| Amit Patel   |
+--------------+
3 rows in set (0.00 sec)
```

## 4: Retrieve students' details studying in 'computer science' or 'chemistry'.

```sql
SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');
```

```
mysql> SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');
+---------+--------------+------------+------------+
| Roll_No | StudentName  | Course     | DOB        |
+---------+--------------+------------+------------+
| S00001  | Aarav Kumar  | computer s | 2001-05-15 |
| S00002  | Aditi Sharma | chemistry  | 2002-08-20 |
| X00009  | Sneha Gupta  | computer s | 2001-02-25 |
| S00006  | Priya Das    | chemistry  | 2003-01-12 |
+---------+--------------+------------+------------+
4 rows in set (0.00 sec)
```

## 5: Retrieve students' names whose roll no starts with 'X' or 'Z' and ends with '9'.

```sql
SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');
```

```
mysql> SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');
+--------------+
| StudentName  |
+--------------+
| Sneha Gupta  |
| Vikram Singh |
+--------------+
2 rows in set (0.00 sec)
```

## 6: Find society details with more than N=25 TotalSeats.

```sql
SELECT * FROM SOCIETY WHERE TotalSeats > 25;  -- N = 25
```

```
mysql> SELECT * FROM SOCIETY WHERE TotalSeats > 25;
+-------+----------+--------------+------------+
| SocID | SocName  | MentorName   | TotalSeats |
+-------+----------+--------------+------------+
| s1    | NSS      | Mr. A Gupta  | 50         |
| s2    | Debating | Ms. R Kaur   | 30         |
| s3    | Dancing  | Mr. S Sharma | 40         |
+-------+----------+--------------+------------+
3 rows in set (0.00 sec)
```

## 7: Update mentor name of society 's5' (Music).

```sql
UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';
```

```
mysql> UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM SOCIETY;
+-------+----------+----------------+------------+
| SocID | SocName  | MentorName     | TotalSeats |
+-------+----------+----------------+------------+
| s1    | NSS      | Mr. A Gupta    | 50         |
| s2    | Debating | Ms. R Kaur     | 30         |
| s3    | Dancing  | Mr. S Sharma   | 40         |
| s4    | Sashakt  | Dr. V Gupta    | 25         |
| s5    | Music    | Dr. New Mentor | 20         |
| s6    | Art      | Mr. K Verma    | 15         |
+-------+----------+----------------+------------+
6 rows in set (0.00 sec)
```

## 8: Find society names in which more than five students have enrolled.

```sql
SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) > 5;
```

```
mysql> SELECT s.SocName
    -> FROM SOCIETY s
    -> JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName
    -> HAVING COUNT(e.Roll_No) > 5;
+---------+
| SocName |
+---------+
+---------+
Empty set (0.00 sec)
```

## 9: Find the name of the youngest student enrolled in society 'NSS'.

```sql
SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName = 'NSS'
ORDER BY st.DOB DESC LIMIT 1;
```

```
mysql> SELECT st.StudentName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> JOIN SOCIETY s ON e.SID = s.SocID
    -> WHERE s.SocName = 'NSS'
    -> ORDER BY st.DOB DESC LIMIT 1;
+-------------+
| StudentName |
+-------------+
| Priya Das   |
+-------------+
1 row in set (0.00 sec)
```

## 10: Find the name of the most popular society (by enrolled students).

```sql
SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;
```

```
mysql> SELECT s.SocName
    -> FROM SOCIETY s
    -> JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName
    -> ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;
+---------+
| SocName |
+---------+
| NSS     |
+---------+
1 row in set (0.00 sec)
```

## 11: Find the names of the two least popular societies (by enrolled students).

```sql
SELECT s.SocName
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;
```

```
mysql> SELECT s.SocName
    -> FROM SOCIETY s
    -> LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName
    -> ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;
+---------+
| SocName |
+---------+
| Music   |
| Art     |
+---------+
2 rows in set (0.00 sec)
```

## 12: Find student names who are NOT enrolled in any society.

```sql
SELECT StudentName
FROM STUDENT
WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);
```

```
mysql> SELECT StudentName
    -> FROM STUDENT
    -> WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);
+--------------+
| StudentName  |
+--------------+
| Vikram Singh |
+--------------+
1 row in set (0.00 sec)
```

## 13: Find student names enrolled in at least two societies.

```sql
SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(e.SID) >= 2;
```

```
mysql> SELECT st.StudentName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> GROUP BY st.Roll_No, st.StudentName
    -> HAVING COUNT(e.SID) >= 2;
+-------------+
| StudentName |
+-------------+
| Aarav Kumar |
+-------------+
1 row in set (0.00 sec)
```

## 14: Find society names in which the maximum number of students are enrolled.

```sql
SELECT SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) = (
    SELECT MAX(cnt) FROM (
        SELECT COUNT(Roll_No) AS cnt FROM ENROLLMENT GROUP BY SID
    )
);
```

```
mysql> SELECT SocName
    -> FROM SOCIETY s
    -> JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName
    -> HAVING COUNT(e.Roll_No) = (
    ->     SELECT MAX(cnt) FROM (
    ->         SELECT COUNT(Roll_No) AS cnt FROM ENROLLMENT GROUP BY SID
    ->     )
    -> );
+---------+
| SocName |
+---------+
| NSS     |
+---------+
1 row in set (0.00 sec)
```

## 15: Find student names enrolled in any society AND society names with ≥ 1 student.

```sql
SELECT st.StudentName, s.SocName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID;
```

```
mysql> SELECT st.StudentName, s.SocName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> JOIN SOCIETY s ON e.SID = s.SocID;
+--------------+----------+
| StudentName  | SocName  |
+--------------+----------+
| Aarav Kumar  | NSS      |
| Aarav Kumar  | Debating |
| Aditi Sharma | Dancing  |
| Rahul Verma  | NSS      |
| Priya Das    | NSS      |
| Amit Patel   | Debating |
| Neha Jain    | Dancing  |
| Sneha Gupta  | Sashakt  |
+--------------+----------+
8 rows in set (0.00 sec)
```

## 16: Find students enrolled in 'Debating', 'Dancing' or 'Sashakt'.

```sql
SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');
```

```
mysql> SELECT DISTINCT st.StudentName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> JOIN SOCIETY s ON e.SID = s.SocID
    -> WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');
+--------------+
| StudentName  |
+--------------+
| Aarav Kumar  |
| Aditi Sharma |
| Amit Patel   |
| Neha Jain    |
| Sneha Gupta  |
+--------------+
5 rows in set (0.00 sec)
```

## 17: Find society names whose mentor name contains 'Gupta'.

```sql
SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';
```

```
mysql> SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';
+---------+
| SocName |
+---------+
| NSS     |
| Sashakt |
+---------+
2 rows in set (0.00 sec)
```

## 18: Find society names where enrolled students = exactly 10% of its capacity.

```sql
SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats
HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;
```

```
mysql> SELECT s.SocName
    -> FROM SOCIETY s
    -> JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName, s.TotalSeats
    -> HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;
+---------+
| SocName |
+---------+
+---------+
Empty set (0.00 sec)
```

## 19: Display the vacant seats for each society.

```sql
SELECT s.SocName, s.TotalSeats - COUNT(e.Roll_No) AS VacantSeats
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats;
```

```
mysql> SELECT s.SocName, s.TotalSeats - COUNT(e.Roll_No) AS VacantSeats
    -> FROM SOCIETY s
    -> LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName, s.TotalSeats;
+----------+-------------+
| SocName  | VacantSeats |
+----------+-------------+
| NSS      | 47          |
| Debating | 28          |
| Dancing  | 38          |
| Sashakt  | 24          |
| Music    | 20          |
| Art      | 15          |
+----------+-------------+
6 rows in set (0.00 sec)
```

## 20: Increment TotalSeats of each society by 10%.

```sql
UPDATE SOCIETY SET TotalSeats = CAST(TotalSeats * 1.10 AS INTEGER);
```

```
mysql> UPDATE SOCIETY SET TotalSeats = CAST(TotalSeats * 1.10 AS INTEGER);
Query OK, 6 rows affected (0.00 sec)

mysql> SELECT * FROM SOCIETY;
+-------+----------+----------------+------------+
| SocID | SocName  | MentorName     | TotalSeats |
+-------+----------+----------------+------------+
| s1    | NSS      | Mr. A Gupta    | 55         |
| s2    | Debating | Ms. R Kaur     | 33         |
| s3    | Dancing  | Mr. S Sharma   | 44         |
| s4    | Sashakt  | Dr. V Gupta    | 27         |
| s5    | Music    | Dr. New Mentor | 22         |
| s6    | Art      | Mr. K Verma    | 16         |
+-------+----------+----------------+------------+
6 rows in set (0.00 sec)
```

## 21: Add FeesPaid ('yes'/'No') field to the ENROLLMENT table.

```sql
ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid TEXT CHECK(FeesPaid IN ('yes','No')) DEFAULT 'No';
```

```
mysql> ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid TEXT CHECK(FeesPaid IN ('yes','No')) DEFAULT 'No';
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM ENROLLMENT;
+---------+-----+------------------+----------+
| Roll_No | SID | DateOfEnrollment | FeesPaid |
+---------+-----+------------------+----------+
| S00001  | s1  | 2023-08-01       | No       |
| S00001  | s2  | 2023-08-05       | No       |
| S00002  | s3  | 2023-08-10       | No       |
| S00003  | s1  | 2023-08-12       | No       |
| X00009  | s4  | 2023-08-15       | No       |
| S00006  | s1  | 2023-08-20       | No       |
| S00007  | s2  | 2023-08-22       | No       |
| S00008  | s3  | 2023-08-25       | No       |
+---------+-----+------------------+----------+
8 rows in set (0.00 sec)
```

## 22: Update DateOfEnrollment: s1→'2018-01-15', s2→today, s3→'2018-01-02'.

```sql
UPDATE ENROLLMENT SET DateOfEnrollment = CASE
    WHEN SID = 's1' THEN '2018-01-15'
    WHEN SID = 's2' THEN DATE('now')
    WHEN SID = 's3' THEN '2018-01-02'
    ELSE DateOfEnrollment
END;
```

```
mysql> UPDATE ENROLLMENT SET DateOfEnrollment = CASE
    ->     WHEN SID = 's1' THEN '2018-01-15'
    ->     WHEN SID = 's2' THEN DATE('now')
    ->     WHEN SID = 's3' THEN '2018-01-02'
    ->     ELSE DateOfEnrollment
    -> END;
Query OK, 8 rows affected (0.00 sec)

mysql> SELECT * FROM ENROLLMENT;
+---------+-----+------------------+----------+
| Roll_No | SID | DateOfEnrollment | FeesPaid |
+---------+-----+------------------+----------+
| S00001  | s1  | 2018-01-15       | No       |
| S00001  | s2  | 2026-03-12       | No       |
| S00002  | s3  | 2018-01-02       | No       |
| S00003  | s1  | 2018-01-15       | No       |
| X00009  | s4  | 2023-08-15       | No       |
| S00006  | s1  | 2018-01-15       | No       |
| S00007  | s2  | 2026-03-12       | No       |
| S00008  | s3  | 2018-01-02       | No       |
+---------+-----+------------------+----------+
8 rows in set (0.00 sec)
```

## 23: Create a view to track society names with total enrolled students.

```sql
CREATE VIEW Society_Enrollment_Count AS
SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName;
```

```
mysql> CREATE VIEW Society_Enrollment_Count AS
    -> SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled
    -> FROM SOCIETY s
    -> LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM Society_Enrollment_Count;
+----------+---------------+
| SocName  | TotalEnrolled |
+----------+---------------+
| NSS      | 3             |
| Debating | 2             |
| Dancing  | 2             |
| Sashakt  | 1             |
| Music    | 0             |
| Art      | 0             |
+----------+---------------+
6 rows in set (0.00 sec)
```

## 24: Find student names enrolled in ALL societies.

```sql
SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);
```

```
mysql> SELECT st.StudentName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> GROUP BY st.Roll_No, st.StudentName
    -> HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);
+-------------+
| StudentName |
+-------------+
+-------------+
Empty set (0.00 sec)
```

## 25: Count the number of societies with more than 5 students enrolled.

```sql
SELECT COUNT(*) AS SocietyCount FROM (
    SELECT SID FROM ENROLLMENT
    GROUP BY SID HAVING COUNT(Roll_No) > 5
);
```

```
mysql> SELECT COUNT(*) AS SocietyCount FROM (
    ->     SELECT SID FROM ENROLLMENT
    ->     GROUP BY SID HAVING COUNT(Roll_No) > 5
    -> );
+--------------+
| SocietyCount |
+--------------+
| 0            |
+--------------+
1 row in set (0.00 sec)
```

## 26: Add Mobile_number column to STUDENT with default '9999999999'.

```sql
ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';
```

```
mysql> ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM STUDENT;
+---------+--------------+------------+------------+---------------+
| Roll_No | StudentName  | Course     | DOB        | Mobile_number |
+---------+--------------+------------+------------+---------------+
| S00001  | Aarav Kumar  | computer s | 2001-05-15 | 9999999999    |
| S00002  | Aditi Sharma | chemistry  | 2002-08-20 | 9999999999    |
| S00003  | Rahul Verma  | physics    | 2000-11-10 | 9999999999    |
| X00009  | Sneha Gupta  | computer s | 2001-02-25 | 9999999999    |
| Z00009  | Vikram Singh | maths      | 1999-07-30 | 9999999999    |
| S00006  | Priya Das    | chemistry  | 2003-01-12 | 9999999999    |
| S00007  | Amit Patel   | english    | 2001-09-05 | 9999999999    |
| S00008  | Neha Jain    | history    | 2002-04-18 | 9999999999    |
+---------+--------------+------------+------------+---------------+
8 rows in set (0.00 sec)
```

## 27: Find the total number of students whose age is > 20 years.

```sql
SELECT COUNT(*) AS TotalStudents
FROM STUDENT
WHERE CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) > 20;
```

```
mysql> SELECT COUNT(*) AS TotalStudents
    -> FROM STUDENT
    -> WHERE CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) > 20;
+---------------+
| TotalStudents |
+---------------+
| 8             |
+---------------+
1 row in set (0.00 sec)
```

## 28: Find names of students born in 2001 and enrolled in at least one society.

```sql
SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
WHERE strftime('%Y', st.DOB) = '2001';
```

```
mysql> SELECT DISTINCT st.StudentName
    -> FROM STUDENT st
    -> JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
    -> WHERE strftime('%Y', st.DOB) = '2001';
+-------------+
| StudentName |
+-------------+
| Aarav Kumar |
| Amit Patel  |
| Sneha Gupta |
+-------------+
3 rows in set (0.00 sec)
```

## 29: Count societies whose name starts with 'S', ends with 't', and >= 5 enrolled.

```sql
SELECT COUNT(*) AS Count FROM (
    SELECT s.SocID
    FROM SOCIETY s
    JOIN ENROLLMENT e ON s.SocID = e.SID
    WHERE s.SocName LIKE 'S%t'
    GROUP BY s.SocID
    HAVING COUNT(e.Roll_No) >= 5
);
```

```
mysql> SELECT COUNT(*) AS Count FROM (
    ->     SELECT s.SocID
    ->     FROM SOCIETY s
    ->     JOIN ENROLLMENT e ON s.SocID = e.SID
    ->     WHERE s.SocName LIKE 'S%t'
    ->     GROUP BY s.SocID
    ->     HAVING COUNT(e.Roll_No) >= 5
    -> );
+-------+
| Count |
+-------+
| 0     |
+-------+
1 row in set (0.00 sec)
```

## 30: Display Society name, Mentor name, Total Capacity, Total Enrolled, Unfilled Seats.

```sql
SELECT
    s.SocName                        AS 'Society name',
    s.MentorName                     AS 'Mentor name',
    s.TotalSeats                     AS 'Total Capacity',
    COUNT(e.Roll_No)                 AS 'Total Enrolled',
    s.TotalSeats - COUNT(e.Roll_No)  AS 'Unfilled Seats'
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.MentorName, s.TotalSeats;
```

```
mysql> SELECT
    ->     s.SocName                        AS 'Society name',
    ->     s.MentorName                     AS 'Mentor name',
    ->     s.TotalSeats                     AS 'Total Capacity',
    ->     COUNT(e.Roll_No)                 AS 'Total Enrolled',
    ->     s.TotalSeats - COUNT(e.Roll_No)  AS 'Unfilled Seats'
    -> FROM SOCIETY s
    -> LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
    -> GROUP BY s.SocID, s.SocName, s.MentorName, s.TotalSeats;
+--------------+---------------+----------------+----------------+----------------+
| Society name | Mentor name   | Total Capacity | Total Enrolled | Unfilled Seats |
+--------------+---------------+----------------+----------------+----------------+
| NSS          | Mr. A Gupta   | 55             | 3              | 52             |
| Debating     | Ms. R Kaur    | 33             | 2              | 31             |
| Dancing      | Mr. S Sharma  | 44             | 2              | 42             |
| Sashakt      | Dr. V Gupta   | 27             | 1              | 26             |
| Music        | Dr. New Mentor| 22             | 0              | 22             |
| Art          | Mr. K Verma   | 16             | 0              | 16             |
+--------------+---------------+----------------+----------------+----------------+
6 rows in set (0.00 sec)
```


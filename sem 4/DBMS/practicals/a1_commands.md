- ```sql
  CREATE TABLE STUDENT (
      Roll_No     CHAR(6) PRIMARY KEY,
      StudentName VARCHAR(20),
      Course      VARCHAR(10),
      DOB         DATE
  );
  ```

- ```sql
  CREATE TABLE SOCIETY (
      SocID      CHAR(6) PRIMARY KEY,
      SocName    VARCHAR(20),
      MentorName VARCHAR(15),
      TotalSeats INT UNSIGNED
  );
  ```

- ```sql
  CREATE TABLE ENROLLMENT (
      Roll_No          CHAR(6),
      SID              CHAR(6),
      DateOfEnrollment DATE,
      PRIMARY KEY (Roll_No, SID),
      FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
      FOREIGN KEY (SID)     REFERENCES SOCIETY(SocID)
  );
  ```

- ```sql
  INSERT INTO STUDENT VALUES
  ('S00001','Aarav Kumar',  'computer s','2001-05-15'),
  ('S00002','Aditi Sharma', 'chemistry', '2002-08-20'),
  ('S00003','Rahul Verma',  'physics',   '2000-11-10'),
  ('X00009','Sneha Gupta',  'computer s','2001-02-25'),
  ('Z00009','Vikram Singh', 'maths',     '1999-07-30'),
  ('S00006','Priya Das',    'chemistry', '2003-01-12'),
  ('S00007','Amit Patel',   'english',   '2001-09-05'),
  ('S00008','Neha Jain',    'history',   '2002-04-18');
  ```

- ```sql
  INSERT INTO SOCIETY VALUES
  ('s1','NSS',      'Mr. A Gupta',  50),
  ('s2','Debating', 'Ms. R Kaur',   30),
  ('s3','Dancing',  'Mr. S Sharma', 40),
  ('s4','Sashakt',  'Dr. V Gupta',  25),
  ('s5','Music',    'Ms. P Singh',  20),
  ('s6','Art',      'Mr. K Verma',  15);
  ```

- ```sql
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

- ```sql
  SELECT * FROM STUDENT;
  ```

- ```sql
  SELECT * FROM SOCIETY;
  ```

- ```sql
  SELECT * FROM ENROLLMENT;
  ```

- ```sql
  SELECT DISTINCT s.StudentName
  FROM STUDENT s
  JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;
  ```

- ```sql
  SELECT SocName FROM SOCIETY;
  ```

- ```sql
  SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';
  ```

- ```sql
  SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');
  ```

- ```sql
  SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');
  ```

- ```sql
  SELECT * FROM SOCIETY WHERE TotalSeats > 25;  -- N = 25;
  ```

- ```sql
  UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';
  ```

- ```sql
  SELECT s.SocName
  FROM SOCIETY s
  JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName
  HAVING COUNT(e.Roll_No) > 5;
  ```

- ```sql
  SELECT st.StudentName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  JOIN SOCIETY s ON e.SID = s.SocID
  WHERE s.SocName = 'NSS'
  ORDER BY st.DOB DESC LIMIT 1;
  ```

- ```sql
  SELECT s.SocName
  FROM SOCIETY s
  JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName
  ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;
  ```

- ```sql
  SELECT s.SocName
  FROM SOCIETY s
  LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName
  ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;
  ```

- ```sql
  SELECT StudentName
  FROM STUDENT
  WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);
  ```

- ```sql
  SELECT st.StudentName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  GROUP BY st.Roll_No, st.StudentName
  HAVING COUNT(e.SID) >= 2;
  ```

- ```sql
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

- ```sql
  SELECT st.StudentName, s.SocName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  JOIN SOCIETY s ON e.SID = s.SocID;
  ```

- ```sql
  SELECT DISTINCT st.StudentName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  JOIN SOCIETY s ON e.SID = s.SocID
  WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');
  ```

- ```sql
  SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';
  ```

- ```sql
  SELECT s.SocName
  FROM SOCIETY s
  JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName, s.TotalSeats
  HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;
  ```

- ```sql
  SELECT s.SocName, s.TotalSeats - COUNT(e.Roll_No) AS VacantSeats
  FROM SOCIETY s
  LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName, s.TotalSeats;
  ```

- ```sql
  UPDATE SOCIETY SET TotalSeats = CAST(TotalSeats * 1.10 AS INTEGER);
  ```

- ```sql
  ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid TEXT CHECK(FeesPaid IN ('yes','No')) DEFAULT 'No';
  ```

- ```sql
  UPDATE ENROLLMENT SET DateOfEnrollment = CASE
      WHEN SID = 's1' THEN '2018-01-15'
      WHEN SID = 's2' THEN DATE('now')
      WHEN SID = 's3' THEN '2018-01-02'
      ELSE DateOfEnrollment
  END;
  ```

- ```sql
  CREATE VIEW Society_Enrollment_Count AS
  SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled
  FROM SOCIETY s
  LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
  GROUP BY s.SocID, s.SocName;
  ```

- ```sql
  SELECT st.StudentName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  GROUP BY st.Roll_No, st.StudentName
  HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);
  ```

- ```sql
  SELECT COUNT(*) AS SocietyCount FROM (
      SELECT SID FROM ENROLLMENT
      GROUP BY SID HAVING COUNT(Roll_No) > 5
  );
  ```

- ```sql
  ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';
  ```

- ```sql
  SELECT COUNT(*) AS TotalStudents
  FROM STUDENT
  WHERE CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) > 20;
  ```

- ```sql
  SELECT DISTINCT st.StudentName
  FROM STUDENT st
  JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
  WHERE strftime('%Y', st.DOB) = '2001';
  ```

- ```sql
  SELECT COUNT(*) AS Count FROM (
      SELECT s.SocID
      FROM SOCIETY s
      JOIN ENROLLMENT e ON s.SocID = e.SID
      WHERE s.SocName LIKE 'S%t'
      GROUP BY s.SocID
      HAVING COUNT(e.Roll_No) >= 5
  );
  ```

- ```sql
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


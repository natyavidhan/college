-- Create database and use it
CREATE DATABASE student_society;
USE student_society;

-- Create tables
CREATE TABLE STUDENT (
    Roll_No CHAR(6) PRIMARY KEY,
    StudentName VARCHAR(20),
    Course VARCHAR(10),
    DOB DATE
);

CREATE TABLE SOCIETY (
    SocID CHAR(6) PRIMARY KEY,
    SocName VARCHAR(20),
    MentorName VARCHAR(15),
    TotalSeats INT UNSIGNED
);

CREATE TABLE ENROLLMENT (
    Roll_No CHAR(6),
    SID CHAR(6),
    DateOfEnrollment DATE,
    PRIMARY KEY (Roll_No, SID),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (SID) REFERENCES SOCIETY(SocID)
);

-- Insert sample data
INSERT INTO STUDENT (Roll_No, StudentName, Course, DOB) VALUES
('S00001', 'Aarav Kumar', 'computer s', '2001-05-15'),
('S00002', 'Aditi Sharma', 'chemistry', '2002-08-20'),
('S00003', 'Rahul Verma', 'physics', '2000-11-10'),
('X00009', 'Sneha Gupta', 'computer s', '2001-02-25'),
('Z00009', 'Vikram Singh', 'maths', '1999-07-30'),
('S00006', 'Priya Das', 'chemistry', '2003-01-12'),
('S00007', 'Amit Patel', 'english', '2001-09-05'),
('S00008', 'Neha Jain', 'history', '2002-04-18');

INSERT INTO SOCIETY (SocID, SocName, MentorName, TotalSeats) VALUES
('s1', 'NSS', 'Mr. A Gupta', 50),
('s2', 'Debating', 'Ms. R Kaur', 30),
('s3', 'Dancing', 'Mr. S Sharma', 40),
('s4', 'Sashakt', 'Dr. V Gupta', 25),
('s5', 'Music', 'Ms. P Singh', 20),
('s6', 'Art', 'Mr. K Verma', 15);

INSERT INTO ENROLLMENT (Roll_No, SID, DateOfEnrollment) VALUES
('S00001', 's1', '2023-08-01'),
('S00001', 's2', '2023-08-05'),
('S00002', 's3', '2023-08-10'),
('S00003', 's1', '2023-08-12'),
('X00009', 's4', '2023-08-15'),
('S00006', 's1', '2023-08-20'),
('S00007', 's2', '2023-08-22'),
('S00008', 's3', '2023-08-25');

-- Show all tables data
SELECT * FROM STUDENT;
SELECT * FROM SOCIETY;
SELECT * FROM ENROLLMENT;

-- Queries

-- 1. Retrieve names of students enrolled in any society.
SELECT DISTINCT s.StudentName 
FROM STUDENT s 
JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;

-- 2. Retrieve all society names.
SELECT SocName FROM SOCIETY;

-- 3. Retrieve students' names starting with the letter 'A'.
SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';

-- 4. Retrieve students' details studying in courses 'computer science' or 'chemistry'.
SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');

-- 5. Retrieve students' names whose roll no either starts with 'X' or 'Z' and ends with '9'
SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');

-- 6. Find society details with more than N TotalSeats where N is to be input by the user.
-- Assuming N = 25 for this example
SET @N = 25;
SELECT * FROM SOCIETY WHERE TotalSeats > @N;

-- 7. Update society table for the mentor name of a specific society.
UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';

-- 8. Find society names in which more than five students have enrolled.
SELECT s.SocName 
FROM SOCIETY s 
JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName 
HAVING COUNT(e.Roll_No) > 5;

-- 9. Find the name of the youngest student enrolled in society 'NSS'.
SELECT st.StudentName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
JOIN SOCIETY s ON e.SID = s.SocID 
WHERE s.SocName = 'NSS' 
ORDER BY st.DOB DESC LIMIT 1;

-- 10. Find the name of the most popular society (on the basis of enrolled students).
SELECT s.SocName 
FROM SOCIETY s 
JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName 
ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;

-- 11. Find the name of two least popular societies (on the basis of enrolled students).
SELECT s.SocName 
FROM SOCIETY s 
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName 
ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;

-- 12. Find the students names who are not enrolled in any society.
SELECT StudentName 
FROM STUDENT 
WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);

-- 13. Find the students names enrolled in at least two societies.
SELECT st.StudentName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
GROUP BY st.Roll_No, st.StudentName 
HAVING COUNT(e.SID) >= 2;

-- 14. Find society names in which maximum students are enrolled.
SELECT SocName FROM SOCIETY s JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY s.SocID, s.SocName HAVING COUNT(e.Roll_No) = (SELECT MAX(cnt) FROM (SELECT COUNT(Roll_No) as cnt FROM ENROLLMENT GROUP BY SID) as temp);

-- 15. Find names of all students who have enrolled in any society and society names in which at least one student has enrolled.
-- Using UNION for the logical "and" of the two sets if needed, but the query likely means pairs of Student and Society.
SELECT st.StudentName, s.SocName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
JOIN SOCIETY s ON e.SID = s.SocID;

-- 16. Find names of students who are enrolled in any of the three societies 'Debating', 'Dancing' and 'Sashakt'.
SELECT DISTINCT st.StudentName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
JOIN SOCIETY s ON e.SID = s.SocID 
WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');

-- 17. Find society names such that its mentor has a name with 'Gupta' in it.
SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';

-- 18. Find the society names in which the number of enrolled students is only 10% of its capacity.
SELECT s.SocName 
FROM SOCIETY s 
JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName, s.TotalSeats 
HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;

-- 19. Display the vacant seats for each society.
SELECT s.SocName, s.TotalSeats - COALESCE(COUNT(e.Roll_No), 0) AS VacantSeats 
FROM SOCIETY s 
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName, s.TotalSeats;

-- 20. Increment Total Seats of each society by 10%.
UPDATE SOCIETY SET TotalSeats = TotalSeats + (TotalSeats * 0.10);

-- 21. Add the enrollment fees paid ('yes'/'No') field in the enrollment table.
ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid ENUM('yes', 'No') DEFAULT 'No';

-- 22. Update date of enrollment of society id 's1' to '2018-01-15', 's2' to the current date and 's3' to '2018-01-02'.
UPDATE ENROLLMENT SET DateOfEnrollment = CASE 
    WHEN SID = 's1' THEN '2018-01-15'
    WHEN SID = 's2' THEN CURRENT_DATE()
    WHEN SID = 's3' THEN '2018-01-02'
    ELSE DateOfEnrollment
END;

-- 23. Create a view to keep track of society names with the total number of students enrolled in it.
CREATE VIEW Society_Enrollment_Count AS 
SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled 
FROM SOCIETY s 
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName;

-- 24. Find student names enrolled in all the societies.
SELECT st.StudentName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
GROUP BY st.Roll_No, st.StudentName 
HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);

-- 25. Count the number of societies with more than 5 students enrolled in it.
SELECT COUNT(*) FROM (
    SELECT SID FROM ENROLLMENT GROUP BY SID HAVING COUNT(Roll_No) > 5
) AS subquery;

-- 26. Add column Mobile number in student table with default value '9999999999'.
ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';

-- 27. Find the total number of students whose age is > 20 years.
SELECT COUNT(*) FROM STUDENT WHERE TIMESTAMPDIFF(YEAR, DOB, CURDATE()) > 20;

-- 28. Find names of students who were born in 2001 and are enrolled in at least one society.
SELECT DISTINCT st.StudentName 
FROM STUDENT st 
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No 
WHERE YEAR(st.DOB) = 2001;

-- 29. Count all societies whose name starts with 'S' and ends with 't' and at least 5 students are enrolled in the society.
SELECT COUNT(*) FROM (
    SELECT s.SocID 
    FROM SOCIETY s 
    JOIN ENROLLMENT e ON s.SocID = e.SID 
    WHERE s.SocName LIKE 'S%t' 
    GROUP BY s.SocID 
    HAVING COUNT(e.Roll_No) >= 5
) AS subquery;

-- 30. Display the following information: Society name, Mentor name, Total Capacity, Total Enrolled, Unfilled Seats
SELECT 
    s.SocName AS 'Society name', 
    s.MentorName AS 'Mentor name', 
    s.TotalSeats AS 'Total Capacity', 
    COUNT(e.Roll_No) AS 'Total Enrolled', 
    s.TotalSeats - COUNT(e.Roll_No) AS 'Unfilled Seats' 
FROM SOCIETY s 
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID 
GROUP BY s.SocID, s.SocName, s.MentorName, s.TotalSeats;

#!/usr/bin/env python3
"""
Student Society Database - Interactive SQL Runner (SQLite)
Press ENTER after each screenshot to advance to the next query.
Output is formatted to match the MySQL shell exactly.
"""

import sqlite3
import time


# ─────────────────────────────────────────────────────────────────────────────
# MySQL-style output helpers
# ─────────────────────────────────────────────────────────────────────────────

def mysql_table(rows, headers):
    """Print a result set exactly like the MySQL CLI."""
    str_rows = [[("NULL" if v is None else str(v)) for v in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in str_rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(val))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt    = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"

    print(border)
    print(fmt.format(*headers))
    print(border)
    for row in str_rows:
        print(fmt.format(*row))
    print(border)

    n = len(rows)
    if n == 0:
        print("Empty set (0.00 sec)")
    elif n == 1:
        print("1 row in set (0.00 sec)")
    else:
        print(f"{n} rows in set (0.00 sec)")


def mysql_ok(rowcount=0, extra=""):
    suffix = f"  {extra}" if extra else ""
    print(f"Query OK, {rowcount} row{'s' if rowcount != 1 else ''} affected (0.00 sec){suffix}")


def show_table(conn, name):
    """Print a full table in MySQL style (used after DML statements)."""
    print()
    try:
        cur = conn.execute(f"SELECT * FROM {name}")
        headers = [d[0] for d in cur.description]
        rows = cur.fetchall()
        mysql_table(rows, headers)
    except Exception as e:
        print(f"ERROR 1064: {e}")


def mysql_prompt(sql):
    """Print the SQL the way the MySQL shell echoes it (multiline aware)."""
    lines = sql.strip().splitlines()
    print(f"mysql> {lines[0]}")
    for line in lines[1:]:
        print(f"    -> {line}")


def pause(msg=""):
    input("\nPress ENTER to continue...\n")


def run_query(conn, number, description, sql, show_tables=None):
    print(f"\n-- Query {number}: {description}")
    mysql_prompt(sql)
    try:
        cur = conn.execute(sql)
        if cur.description:
            headers = [d[0] for d in cur.description]
            rows = cur.fetchall()
            mysql_table(rows, headers)
        else:
            conn.commit()
            mysql_ok(cur.rowcount if cur.rowcount >= 0 else 0)
        if show_tables:
            for t in show_tables:
                print(f"\nmysql> SELECT * FROM {t};")
                show_table(conn, t)
    except Exception as e:
        print(f"ERROR 1064 (42000): {e}")
    pause()


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")

    # ── PHASE 1: Schema + Data ─────────────────────────────────────────────
    print("-- Student Society Database Setup\n")

    setup = [
        ("CREATE TABLE STUDENT",
         """CREATE TABLE STUDENT (
    Roll_No     CHAR(6) PRIMARY KEY,
    StudentName VARCHAR(20),
    Course      VARCHAR(10),
    DOB         DATE
)"""),
        ("CREATE TABLE SOCIETY",
         """CREATE TABLE SOCIETY (
    SocID      CHAR(6) PRIMARY KEY,
    SocName    VARCHAR(20),
    MentorName VARCHAR(15),
    TotalSeats INT UNSIGNED
)"""),
        ("CREATE TABLE ENROLLMENT",
         """CREATE TABLE ENROLLMENT (
    Roll_No          CHAR(6),
    SID              CHAR(6),
    DateOfEnrollment DATE,
    PRIMARY KEY (Roll_No, SID),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (SID)     REFERENCES SOCIETY(SocID)
)"""),
        ("INSERT INTO STUDENT",
         """INSERT INTO STUDENT VALUES
('S00001','Aarav Kumar',  'computer s','2001-05-15'),
('S00002','Aditi Sharma', 'chemistry', '2002-08-20'),
('S00003','Rahul Verma',  'physics',   '2000-11-10'),
('X00009','Sneha Gupta',  'computer s','2001-02-25'),
('Z00009','Vikram Singh', 'maths',     '1999-07-30'),
('S00006','Priya Das',    'chemistry', '2003-01-12'),
('S00007','Amit Patel',   'english',   '2001-09-05'),
('S00008','Neha Jain',    'history',   '2002-04-18')"""),
        ("INSERT INTO SOCIETY",
         """INSERT INTO SOCIETY VALUES
('s1','NSS',      'Mr. A Gupta',  50),
('s2','Debating', 'Ms. R Kaur',   30),
('s3','Dancing',  'Mr. S Sharma', 40),
('s4','Sashakt',  'Dr. V Gupta',  25),
('s5','Music',    'Ms. P Singh',  20),
('s6','Art',      'Mr. K Verma',  15)"""),
        ("INSERT INTO ENROLLMENT",
         """INSERT INTO ENROLLMENT VALUES
('S00001','s1','2023-08-01'),
('S00001','s2','2023-08-05'),
('S00002','s3','2023-08-10'),
('S00003','s1','2023-08-12'),
('X00009','s4','2023-08-15'),
('S00006','s1','2023-08-20'),
('S00007','s2','2023-08-22'),
('S00008','s3','2023-08-25')"""),
    ]

    for label, sql in setup:
        mysql_prompt(sql + ";")
        try:
            conn.execute(sql)
            conn.commit()
            mysql_ok(0)
        except Exception as e:
            print(f"ERROR 1064 (42000): {e}")
        print()

    # Show initial table data
    for tbl in ("STUDENT", "SOCIETY", "ENROLLMENT"):
        print(f"mysql> SELECT * FROM {tbl};")
        show_table(conn, tbl)
        print()

    pause()

    # ── PHASE 2: Queries 1-30 ──────────────────────────────────────────────

    # Q1
    run_query(conn, 1,
        "Retrieve names of students enrolled in any society.",
        """SELECT DISTINCT s.StudentName
FROM STUDENT s
JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;""")

    # Q2
    run_query(conn, 2,
        "Retrieve all society names.",
        "SELECT SocName FROM SOCIETY;")

    # Q3
    run_query(conn, 3,
        "Retrieve students' names starting with the letter 'A'.",
        "SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';")

    # Q4
    run_query(conn, 4,
        "Retrieve students' details studying in 'computer science' or 'chemistry'.",
        "SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');")

    # Q5
    run_query(conn, 5,
        "Retrieve students' names whose roll no starts with 'X' or 'Z' and ends with '9'.",
        "SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');")

    # Q6 — user input for N
    print("\n-- Query 6: Society details with more than N TotalSeats (user input)")
    try:
        n_val = int(input("mysql> SET @N = "))
    except ValueError:
        n_val = 25
        print(f"-- Invalid input, using N = {n_val}")
    sql6 = f"SELECT * FROM SOCIETY WHERE TotalSeats > {n_val};"
    mysql_prompt(sql6)
    try:
        cur = conn.execute(sql6.rstrip(";"))
        rows = cur.fetchall()
        mysql_table(rows, [d[0] for d in cur.description])
    except Exception as e:
        print(f"ERROR 1064 (42000): {e}")
    pause()

    # Q7
    run_query(conn, 7,
        "Update mentor name of society 's5' (Music).",
        "UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';",
        show_tables=["SOCIETY"])

    # Q8
    run_query(conn, 8,
        "Find society names in which more than five students have enrolled.",
        """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) > 5;""")

    # Q9
    run_query(conn, 9,
        "Find name of the youngest student enrolled in society 'NSS'.",
        """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName = 'NSS'
ORDER BY st.DOB DESC LIMIT 1;""")

    # Q10
    run_query(conn, 10,
        "Find name of the most popular society (by enrolled students).",
        """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;""")

    # Q11
    run_query(conn, 11,
        "Find names of two least popular societies (by enrolled students).",
        """SELECT s.SocName
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;""")

    # Q12
    run_query(conn, 12,
        "Find student names who are NOT enrolled in any society.",
        """SELECT StudentName
FROM STUDENT
WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);""")

    # Q13
    run_query(conn, 13,
        "Find student names enrolled in at least two societies.",
        """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(e.SID) >= 2;""")

    # Q14
    run_query(conn, 14,
        "Find society names in which the maximum number of students are enrolled.",
        """SELECT SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) = (
    SELECT MAX(cnt) FROM (
        SELECT COUNT(Roll_No) AS cnt FROM ENROLLMENT GROUP BY SID
    )
);""")

    # Q15
    run_query(conn, 15,
        "Student names enrolled in any society AND society names with >= 1 student.",
        """SELECT st.StudentName, s.SocName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID;""")

    # Q16
    run_query(conn, 16,
        "Find students enrolled in 'Debating', 'Dancing' or 'Sashakt'.",
        """SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');""")

    # Q17
    run_query(conn, 17,
        "Find society names whose mentor name contains 'Gupta'.",
        "SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';")

    # Q18
    run_query(conn, 18,
        "Find society names where enrolled students = exactly 10% of capacity.",
        """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats
HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;""")

    # Q19
    run_query(conn, 19,
        "Display vacant seats for each society.",
        """SELECT s.SocName, s.TotalSeats - COUNT(e.Roll_No) AS VacantSeats
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats;""")

    # Q20
    run_query(conn, 20,
        "Increment TotalSeats of each society by 10%.",
        "UPDATE SOCIETY SET TotalSeats = CAST(TotalSeats * 1.10 AS INTEGER);",
        show_tables=["SOCIETY"])

    # Q21
    run_query(conn, 21,
        "Add FeesPaid ('yes'/'No') column to ENROLLMENT table.",
        "ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid TEXT CHECK(FeesPaid IN ('yes','No')) DEFAULT 'No';",
        show_tables=["ENROLLMENT"])

    # Q22
    run_query(conn, 22,
        "Update DateOfEnrollment: s1->'2018-01-15', s2->today, s3->'2018-01-02'.",
        """UPDATE ENROLLMENT SET DateOfEnrollment = CASE
    WHEN SID = 's1' THEN '2018-01-15'
    WHEN SID = 's2' THEN DATE('now')
    WHEN SID = 's3' THEN '2018-01-02'
    ELSE DateOfEnrollment
END;""",
        show_tables=["ENROLLMENT"])

    # Q23 — CREATE VIEW
    print("\n-- Query 23: Create a view — Society name with total enrolled students.")
    view_sql = """CREATE VIEW Society_Enrollment_Count AS
SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName;"""
    mysql_prompt(view_sql)
    try:
        conn.execute(view_sql.rstrip(";"))
        conn.commit()
        mysql_ok(0)
        print("\nmysql> SELECT * FROM Society_Enrollment_Count;")
        cur = conn.execute("SELECT * FROM Society_Enrollment_Count")
        mysql_table(cur.fetchall(), [d[0] for d in cur.description])
    except Exception as e:
        print(f"ERROR 1064 (42000): {e}")
    pause()

    # Q24
    run_query(conn, 24,
        "Find student names enrolled in ALL societies.",
        """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);""")

    # Q25
    run_query(conn, 25,
        "Count societies with more than 5 students enrolled.",
        """SELECT COUNT(*) AS SocietyCount FROM (
    SELECT SID FROM ENROLLMENT
    GROUP BY SID HAVING COUNT(Roll_No) > 5
);""")

    # Q26
    run_query(conn, 26,
        "Add Mobile_number column to STUDENT with default '9999999999'.",
        "ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';",
        show_tables=["STUDENT"])

    # Q27
    run_query(conn, 27,
        "Find total number of students whose age is > 20 years.",
        """SELECT COUNT(*) AS TotalStudents
FROM STUDENT
WHERE CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) > 20;""")

    # Q28
    run_query(conn, 28,
        "Find names of students born in 2001 enrolled in at least one society.",
        """SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
WHERE strftime('%Y', st.DOB) = '2001';""")

    # Q29
    run_query(conn, 29,
        "Count societies: name starts with 'S', ends with 't', >= 5 enrolled.",
        """SELECT COUNT(*) AS Count FROM (
    SELECT s.SocID
    FROM SOCIETY s
    JOIN ENROLLMENT e ON s.SocID = e.SID
    WHERE s.SocName LIKE 'S%t'
    GROUP BY s.SocID
    HAVING COUNT(e.Roll_No) >= 5
);""")

    # Q30
    run_query(conn, 30,
        "Society name | Mentor name | Total Capacity | Total Enrolled | Unfilled Seats",
        """SELECT
    s.SocName                               AS 'Society name',
    s.MentorName                            AS 'Mentor name',
    s.TotalSeats                            AS 'Total Capacity',
    COUNT(e.Roll_No)                        AS 'Total Enrolled',
    s.TotalSeats - COUNT(e.Roll_No)         AS 'Unfilled Seats'
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.MentorName, s.TotalSeats;""")

    print("-- All 30 queries complete!")
    conn.close()


if __name__ == "__main__":
    main()

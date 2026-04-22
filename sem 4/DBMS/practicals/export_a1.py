#!/usr/bin/env python3
"""
Student Society Database — Markdown Exporter
Runs all SQL against an in-memory SQLite DB and writes a .md file with
  ## Query N headers, SQL in ```sql blocks, output in ```text blocks.
"""

import sqlite3
import io
import os

OUT_FILE = os.path.join(os.path.dirname(__file__), "a1_output.md")

# ─────────────────────────────────────────────────────────────────────────────
# MySQL-style table renderer (returns string)
# ─────────────────────────────────────────────────────────────────────────────

def render_table(rows, headers):
    buf = io.StringIO()
    str_rows = [[("NULL" if v is None else str(v)) for v in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in str_rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(val))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt    = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"

    buf.write(border + "\n")
    buf.write(fmt.format(*headers) + "\n")
    buf.write(border + "\n")
    for row in str_rows:
        buf.write(fmt.format(*row) + "\n")
    buf.write(border + "\n")

    n = len(rows)
    if n == 0:
        buf.write("Empty set (0.00 sec)\n")
    elif n == 1:
        buf.write("1 row in set (0.00 sec)\n")
    else:
        buf.write(f"{n} rows in set (0.00 sec)\n")

    return buf.getvalue()


def render_ok(rowcount=0):
    return f"Query OK, {rowcount} row{'s' if rowcount != 1 else ''} affected (0.00 sec)\n"


def render_table_from_conn(conn, name):
    cur = conn.execute(f"SELECT * FROM {name}")
    headers = [d[0] for d in cur.description]
    return "mysql> SELECT * FROM " + name + ";\n" + render_table(cur.fetchall(), headers)


def render_prompt(sql):
    lines = sql.strip().splitlines()
    out = f"mysql> {lines[0]}\n"
    for line in lines[1:]:
        out += f"    -> {line}\n"
    return out


# ─────────────────────────────────────────────────────────────────────────────
# MD section builder
# ─────────────────────────────────────────────────────────────────────────────

sections = []  # list of (heading, sql_text, output_text)


def add(heading, sql, output):
    sections.append((heading, sql.strip(), output.strip()))


def run_select(conn, sql):
    cur = conn.execute(sql)
    headers = [d[0] for d in cur.description]
    return render_prompt(sql + ";") + render_table(cur.fetchall(), headers)


def run_dml(conn, sql, show_tables=None):
    cur = conn.execute(sql)
    conn.commit()
    out = render_prompt(sql + ";") + render_ok(cur.rowcount if cur.rowcount >= 0 else 0)
    if show_tables:
        for t in show_tables:
            out += "\n" + render_table_from_conn(conn, t)
    return out


def run_ddl(conn, sql, show_tables=None):
    conn.execute(sql)
    conn.commit()
    out = render_prompt(sql + ";") + render_ok(0)
    if show_tables:
        for t in show_tables:
            out += "\n" + render_table_from_conn(conn, t)
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")

    md = io.StringIO()
    md.write("# Student Society Database — Practical 1\n\n")

    # ── Setup ────────────────────────────────────────────────────────────────
    md.write("## Setup — Create Tables\n\n")

    setup_sqls = [
        """CREATE TABLE STUDENT (
    Roll_No     CHAR(6) PRIMARY KEY,
    StudentName VARCHAR(20),
    Course      VARCHAR(10),
    DOB         DATE
)""",
        """CREATE TABLE SOCIETY (
    SocID      CHAR(6) PRIMARY KEY,
    SocName    VARCHAR(20),
    MentorName VARCHAR(15),
    TotalSeats INT UNSIGNED
)""",
        """CREATE TABLE ENROLLMENT (
    Roll_No          CHAR(6),
    SID              CHAR(6),
    DateOfEnrollment DATE,
    PRIMARY KEY (Roll_No, SID),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (SID)     REFERENCES SOCIETY(SocID)
)""",
    ]

    setup_out = ""
    for sql in setup_sqls:
        conn.execute(sql)
        conn.commit()
        setup_out += render_prompt(sql + ";") + render_ok(0) + "\n"

    md.write("```sql\n" + "\n".join(s + ";" for s in setup_sqls) + "\n```\n\n")
    md.write("```\n" + setup_out.rstrip() + "\n```\n\n")

    # ── Insert Data ──────────────────────────────────────────────────────────
    md.write("## Setup — Insert Data\n\n")

    insert_sqls = [
        """INSERT INTO STUDENT VALUES
('S00001','Aarav Kumar',  'computer s','2001-05-15'),
('S00002','Aditi Sharma', 'chemistry', '2002-08-20'),
('S00003','Rahul Verma',  'physics',   '2000-11-10'),
('X00009','Sneha Gupta',  'computer s','2001-02-25'),
('Z00009','Vikram Singh', 'maths',     '1999-07-30'),
('S00006','Priya Das',    'chemistry', '2003-01-12'),
('S00007','Amit Patel',   'english',   '2001-09-05'),
('S00008','Neha Jain',    'history',   '2002-04-18')""",
        """INSERT INTO SOCIETY VALUES
('s1','NSS',      'Mr. A Gupta',  50),
('s2','Debating', 'Ms. R Kaur',   30),
('s3','Dancing',  'Mr. S Sharma', 40),
('s4','Sashakt',  'Dr. V Gupta',  25),
('s5','Music',    'Ms. P Singh',  20),
('s6','Art',      'Mr. K Verma',  15)""",
        """INSERT INTO ENROLLMENT VALUES
('S00001','s1','2023-08-01'),
('S00001','s2','2023-08-05'),
('S00002','s3','2023-08-10'),
('S00003','s1','2023-08-12'),
('X00009','s4','2023-08-15'),
('S00006','s1','2023-08-20'),
('S00007','s2','2023-08-22'),
('S00008','s3','2023-08-25')""",
    ]

    ins_out = ""
    for sql in insert_sqls:
        cur = conn.execute(sql)
        conn.commit()
        ins_out += render_prompt(sql + ";") + render_ok(cur.rowcount) + "\n"

    md.write("```sql\n" + "\n\n".join(s + ";" for s in insert_sqls) + "\n```\n\n")
    md.write("```\n" + ins_out.rstrip() + "\n```\n\n")

    # ── Initial table dump ───────────────────────────────────────────────────
    md.write("## Initial Table Data\n\n")
    dump_out = ""
    for t in ("STUDENT", "SOCIETY", "ENROLLMENT"):
        dump_out += render_table_from_conn(conn, t) + "\n"
    md.write("```sql\nSELECT * FROM STUDENT;\nSELECT * FROM SOCIETY;\nSELECT * FROM ENROLLMENT;\n```\n\n")
    md.write("```\n" + dump_out.rstrip() + "\n```\n\n")

    # ── Queries 1–30 ─────────────────────────────────────────────────────────

    def section(num, desc, sql, output):
        md.write(f"## {num}: {desc}\n\n")
        md.write(f"```sql\n{sql.strip()}\n```\n\n")
        md.write(f"```\n{output.strip()}\n```\n\n")

    # Q1
    sql = """SELECT DISTINCT s.StudentName
FROM STUDENT s
JOIN ENROLLMENT e ON s.Roll_No = e.Roll_No;"""
    section(1, "Retrieve names of students enrolled in any society.", sql, run_select(conn, sql.rstrip(";")))

    # Q2
    sql = "SELECT SocName FROM SOCIETY;"
    section(2, "Retrieve all society names.", sql, run_select(conn, sql.rstrip(";")))

    # Q3
    sql = "SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%';"
    section(3, "Retrieve students' names starting with the letter 'A'.", sql, run_select(conn, sql.rstrip(";")))

    # Q4
    sql = "SELECT * FROM STUDENT WHERE Course IN ('computer s', 'chemistry');"
    section(4, "Retrieve students' details studying in 'computer science' or 'chemistry'.", sql, run_select(conn, sql.rstrip(";")))

    # Q5
    sql = "SELECT StudentName FROM STUDENT WHERE (Roll_No LIKE 'X%9' OR Roll_No LIKE 'Z%9');"
    section(5, "Retrieve students' names whose roll no starts with 'X' or 'Z' and ends with '9'.", sql, run_select(conn, sql.rstrip(";")))

    # Q6
    N = 25
    sql = f"SELECT * FROM SOCIETY WHERE TotalSeats > {N};  -- N = {N}"
    section(6, f"Find society details with more than N={N} TotalSeats.", sql, run_select(conn, f"SELECT * FROM SOCIETY WHERE TotalSeats > {N}"))

    # Q7
    sql = "UPDATE SOCIETY SET MentorName = 'Dr. New Mentor' WHERE SocID = 's5';"
    section(7, "Update mentor name of society 's5' (Music).", sql, run_dml(conn, sql.rstrip(";"), show_tables=["SOCIETY"]))

    # Q8
    sql = """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) > 5;"""
    section(8, "Find society names in which more than five students have enrolled.", sql, run_select(conn, sql.rstrip(";")))

    # Q9
    sql = """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName = 'NSS'
ORDER BY st.DOB DESC LIMIT 1;"""
    section(9, "Find the name of the youngest student enrolled in society 'NSS'.", sql, run_select(conn, sql.rstrip(";")))

    # Q10
    sql = """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) DESC LIMIT 1;"""
    section(10, "Find the name of the most popular society (by enrolled students).", sql, run_select(conn, sql.rstrip(";")))

    # Q11
    sql = """SELECT s.SocName
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
ORDER BY COUNT(e.Roll_No) ASC LIMIT 2;"""
    section(11, "Find the names of the two least popular societies (by enrolled students).", sql, run_select(conn, sql.rstrip(";")))

    # Q12
    sql = """SELECT StudentName
FROM STUDENT
WHERE Roll_No NOT IN (SELECT Roll_No FROM ENROLLMENT);"""
    section(12, "Find student names who are NOT enrolled in any society.", sql, run_select(conn, sql.rstrip(";")))

    # Q13
    sql = """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(e.SID) >= 2;"""
    section(13, "Find student names enrolled in at least two societies.", sql, run_select(conn, sql.rstrip(";")))

    # Q14
    sql = """SELECT SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName
HAVING COUNT(e.Roll_No) = (
    SELECT MAX(cnt) FROM (
        SELECT COUNT(Roll_No) AS cnt FROM ENROLLMENT GROUP BY SID
    )
);"""
    section(14, "Find society names in which the maximum number of students are enrolled.", sql, run_select(conn, sql.rstrip(";")))

    # Q15
    sql = """SELECT st.StudentName, s.SocName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID;"""
    section(15, "Find student names enrolled in any society AND society names with ≥ 1 student.", sql, run_select(conn, sql.rstrip(";")))

    # Q16
    sql = """SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
JOIN SOCIETY s ON e.SID = s.SocID
WHERE s.SocName IN ('Debating', 'Dancing', 'Sashakt');"""
    section(16, "Find students enrolled in 'Debating', 'Dancing' or 'Sashakt'.", sql, run_select(conn, sql.rstrip(";")))

    # Q17
    sql = "SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';"
    section(17, "Find society names whose mentor name contains 'Gupta'.", sql, run_select(conn, sql.rstrip(";")))

    # Q18
    sql = """SELECT s.SocName
FROM SOCIETY s
JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats
HAVING COUNT(e.Roll_No) = 0.10 * s.TotalSeats;"""
    section(18, "Find society names where enrolled students = exactly 10% of its capacity.", sql, run_select(conn, sql.rstrip(";")))

    # Q19
    sql = """SELECT s.SocName, s.TotalSeats - COUNT(e.Roll_No) AS VacantSeats
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.TotalSeats;"""
    section(19, "Display the vacant seats for each society.", sql, run_select(conn, sql.rstrip(";")))

    # Q20
    sql = "UPDATE SOCIETY SET TotalSeats = CAST(TotalSeats * 1.10 AS INTEGER);"
    section(20, "Increment TotalSeats of each society by 10%.", sql, run_dml(conn, sql.rstrip(";"), show_tables=["SOCIETY"]))

    # Q21
    sql = "ALTER TABLE ENROLLMENT ADD COLUMN FeesPaid TEXT CHECK(FeesPaid IN ('yes','No')) DEFAULT 'No';"
    section(21, "Add FeesPaid ('yes'/'No') field to the ENROLLMENT table.", sql, run_ddl(conn, sql.rstrip(";"), show_tables=["ENROLLMENT"]))

    # Q22
    sql = """UPDATE ENROLLMENT SET DateOfEnrollment = CASE
    WHEN SID = 's1' THEN '2018-01-15'
    WHEN SID = 's2' THEN DATE('now')
    WHEN SID = 's3' THEN '2018-01-02'
    ELSE DateOfEnrollment
END;"""
    section(22, "Update DateOfEnrollment: s1→'2018-01-15', s2→today, s3→'2018-01-02'.", sql, run_dml(conn, sql.rstrip(";"), show_tables=["ENROLLMENT"]))

    # Q23
    view_sql = """CREATE VIEW Society_Enrollment_Count AS
SELECT s.SocName, COUNT(e.Roll_No) AS TotalEnrolled
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName;"""
    conn.execute(view_sql.rstrip(";"))
    conn.commit()
    view_out = render_prompt(view_sql) + render_ok(0)
    view_out += "\n" + render_table_from_conn(conn, "Society_Enrollment_Count")
    section(23, "Create a view to track society names with total enrolled students.", view_sql, view_out)

    # Q24
    sql = """SELECT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
GROUP BY st.Roll_No, st.StudentName
HAVING COUNT(DISTINCT e.SID) = (SELECT COUNT(*) FROM SOCIETY);"""
    section(24, "Find student names enrolled in ALL societies.", sql, run_select(conn, sql.rstrip(";")))

    # Q25
    sql = """SELECT COUNT(*) AS SocietyCount FROM (
    SELECT SID FROM ENROLLMENT
    GROUP BY SID HAVING COUNT(Roll_No) > 5
);"""
    section(25, "Count the number of societies with more than 5 students enrolled.", sql, run_select(conn, sql.rstrip(";")))

    # Q26
    sql = "ALTER TABLE STUDENT ADD COLUMN Mobile_number VARCHAR(10) DEFAULT '9999999999';"
    section(26, "Add Mobile_number column to STUDENT with default '9999999999'.", sql, run_ddl(conn, sql.rstrip(";"), show_tables=["STUDENT"]))

    # Q27
    sql = """SELECT COUNT(*) AS TotalStudents
FROM STUDENT
WHERE CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) > 20;"""
    section(27, "Find the total number of students whose age is > 20 years.", sql, run_select(conn, sql.rstrip(";")))

    # Q28
    sql = """SELECT DISTINCT st.StudentName
FROM STUDENT st
JOIN ENROLLMENT e ON st.Roll_No = e.Roll_No
WHERE strftime('%Y', st.DOB) = '2001';"""
    section(28, "Find names of students born in 2001 and enrolled in at least one society.", sql, run_select(conn, sql.rstrip(";")))

    # Q29
    sql = """SELECT COUNT(*) AS Count FROM (
    SELECT s.SocID
    FROM SOCIETY s
    JOIN ENROLLMENT e ON s.SocID = e.SID
    WHERE s.SocName LIKE 'S%t'
    GROUP BY s.SocID
    HAVING COUNT(e.Roll_No) >= 5
);"""
    section(29, "Count societies whose name starts with 'S', ends with 't', and >= 5 enrolled.", sql, run_select(conn, sql.rstrip(";")))

    # Q30
    sql = """SELECT
    s.SocName                        AS 'Society name',
    s.MentorName                     AS 'Mentor name',
    s.TotalSeats                     AS 'Total Capacity',
    COUNT(e.Roll_No)                 AS 'Total Enrolled',
    s.TotalSeats - COUNT(e.Roll_No)  AS 'Unfilled Seats'
FROM SOCIETY s
LEFT JOIN ENROLLMENT e ON s.SocID = e.SID
GROUP BY s.SocID, s.SocName, s.MentorName, s.TotalSeats;"""
    section(30, "Display Society name, Mentor name, Total Capacity, Total Enrolled, Unfilled Seats.", sql, run_select(conn, sql.rstrip(";")))

    conn.close()

    # ── Write MD file ────────────────────────────────────────────────────────
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(md.getvalue())

    print(f"Done! Written to: {OUT_FILE}")


if __name__ == "__main__":
    main()

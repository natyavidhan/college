#!/usr/bin/env python3
"""
COMPANY schema - Interactive SQL Runner (SQLite)
MySQL-shell-like output, press ENTER to move query-by-query.
"""

import sqlite3


def mysql_table(rows, headers):
    str_rows = [[("NULL" if v is None else str(v)) for v in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in str_rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(val))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"

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


def mysql_ok(rowcount=0):
    print(f"Query OK, {rowcount} row{'s' if rowcount != 1 else ''} affected (0.00 sec)")


def mysql_prompt(sql):
    lines = sql.strip().splitlines()
    print(f"mysql> {lines[0]}")
    for line in lines[1:]:
        print(f"    -> {line}")


def pause():
    input("\nPress ENTER to continue...\n")


def show_table(conn, table_name):
    print(f"mysql> SELECT * FROM {table_name};")
    cur = conn.execute(f"SELECT * FROM {table_name}")
    headers = [d[0] for d in cur.description]
    mysql_table(cur.fetchall(), headers)


def run_sql(conn, sql, show_tables=None):
    mysql_prompt(sql)
    try:
        cur = conn.execute(sql.rstrip(";"))
        if cur.description:
            headers = [d[0] for d in cur.description]
            mysql_table(cur.fetchall(), headers)
        else:
            conn.commit()
            mysql_ok(cur.rowcount if cur.rowcount >= 0 else 0)
        if show_tables:
            for t in show_tables:
                print()
                show_table(conn, t)
    except Exception as e:
        print(f"ERROR 1064 (42000): {e}")


def seed_database(conn):
    ddl = [
        """CREATE TABLE EMPLOYEE (
    FNAME TEXT NOT NULL,
    MINIT TEXT,
    LNAME TEXT NOT NULL,
    SSN TEXT PRIMARY KEY,
    BDATE DATE,
    ADDRESS TEXT,
    SEX TEXT,
    SALARY REAL,
    SUPERSSN TEXT,
    DNO INTEGER,
    FOREIGN KEY (SUPERSSN) REFERENCES EMPLOYEE(SSN) ON DELETE SET NULL,
    FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNUMBER) ON DELETE SET NULL
);""",
        """CREATE TABLE DEPARTMENT (
    DNAME TEXT UNIQUE,
    DNUMBER INTEGER PRIMARY KEY,
    MGRSSN TEXT DEFAULT '888665555',
    MGRSTARTDATE DATE,
    FOREIGN KEY (MGRSSN) REFERENCES EMPLOYEE(SSN) ON DELETE SET DEFAULT
);""",
        """CREATE TABLE DEPT_LOCATIONS (
    DNUMBER INTEGER,
    DLOCATION TEXT,
    PRIMARY KEY (DNUMBER, DLOCATION),
    FOREIGN KEY (DNUMBER) REFERENCES DEPARTMENT(DNUMBER) ON DELETE CASCADE
);""",
        """CREATE TABLE PROJECT (
    PNAME TEXT UNIQUE,
    PNUMBER INTEGER PRIMARY KEY,
    PLOCATION TEXT,
    DNUM INTEGER,
    FOREIGN KEY (DNUM) REFERENCES DEPARTMENT(DNUMBER) ON DELETE SET NULL
);""",
        """CREATE TABLE WORKS_ON (
    ESSN TEXT,
    PNO INTEGER,
    HOURS REAL,
    PRIMARY KEY (ESSN, PNO),
    FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE,
    FOREIGN KEY (PNO) REFERENCES PROJECT(PNUMBER) ON DELETE CASCADE
);""",
        """CREATE TABLE DEPENDENT (
    ESSN TEXT,
    DEPENDENT_NAME TEXT,
    SEX TEXT,
    BDATE DATE,
    RELATIONSHIP TEXT,
    PRIMARY KEY (ESSN, DEPENDENT_NAME),
    FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE
);""",
    ]

    # Create tables first
    for s in ddl:
        run_sql(conn, s)
        print()

    # Seed departments early for FK DNO
    run_sql(conn, """INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES
('Research', 5, NULL, '1988-05-22'),
('Administration', 4, NULL, '1995-01-01'),
('Headquarters', 1, NULL, '1981-06-19'),
('Marketing', 7, NULL, '2000-01-01'),
('IT', 10, NULL, '2003-03-15'),
('Support', 6, NULL, '2018-01-01');""")
    print()

    run_sql(conn, """INSERT INTO EMPLOYEE (FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPERSSN, DNO) VALUES
('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5),
('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5),
('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', 25000, '987654321', 4),
('Jennifer', 'S', 'Wallace', '987654321', '1941-06-20', '291 Berry, Bellaire, TX', 'F', 43000, '888665555', 4),
('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5),
('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5),
('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000, '987654321', 4),
('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', 55000, NULL, 1),
('Maya', 'R', 'Sharma', '777665555', '1978-04-11', '12 IT Park, Houston, TX', 'F', 61000, '888665555', 10),
('Lina', 'M', 'Das', '222334444', '1980-02-02', '9 Bellaire Ave, Bellaire, TX', 'F', 52000, '777665555', 10),
('Raj', 'P', 'Mehta', '111223333', '1975-03-03', '88 Staff Road, Stafford, TX', 'M', 58000, '777665555', 10),
('Temp', 'Q', 'Manager', '12345', '1985-05-05', '44 Support Ln, Houston, TX', 'M', 45000, '888665555', 6),
('Tina', 'L', 'Ray', '555666777', '1990-01-01', '55 Support Ln, Houston, TX', 'F', 39000, '12345', 6);""")
    print()

    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '333445555' WHERE DNUMBER = 5;")
    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '987654321' WHERE DNUMBER = 4;")
    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '888665555' WHERE DNUMBER = 1;")
    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '666884444' WHERE DNUMBER = 7;")
    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '777665555' WHERE DNUMBER = 10;")
    run_sql(conn, "UPDATE DEPARTMENT SET MGRSSN = '12345' WHERE DNUMBER = 6;")
    print()

    run_sql(conn, """INSERT INTO DEPT_LOCATIONS VALUES
(1,'Houston'),
(4,'Stafford'),
(5,'Bellaire'),
(5,'Sugarland'),
(5,'Houston'),
(6,'Houston'),
(7,'Bellaire'),
(10,'Houston');""")
    print()

    run_sql(conn, """INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4),
('MarketPulse', 40, 'Bellaire', 7),
('CloudShift', 50, 'Houston', 10);""")
    print()

    run_sql(conn, """INSERT INTO WORKS_ON VALUES
('123456789',1,32.5),
('123456789',2,7.5),
('666884444',3,40.0),
('453453453',1,20.0),
('453453453',2,20.0),
('333445555',2,10.0),
('333445555',3,10.0),
('333445555',10,10.0),
('333445555',20,10.0),
('999887777',30,30.0),
('999887777',10,10.0),
('987987987',10,35.0),
('987987987',30,5.0),
('987654321',30,20.0),
('987654321',20,15.0),
('888665555',20,NULL),
('777665555',50,20.0),
('222334444',50,25.0),
('111223333',50,15.0),
('12345',40,22.0),
('555666777',40,18.0);""")
    print()

    run_sql(conn, """INSERT INTO DEPENDENT VALUES
('333445555','Alice','F','1986-04-05','Daughter'),
('333445555','Theodore','M','1983-10-25','Son'),
('333445555','Joy','F','1958-05-03','Spouse'),
('987654321','Abner','M','1942-02-28','Spouse'),
('123456789','Michael','M','1988-01-04','Son'),
('123456789','Alice','F','1988-12-30','Daughter'),
('123456789','Elizabeth','F','1967-05-05','Spouse'),
('12345','Temp','M','2012-08-08','Son');""")
    print()


def run_query(conn, idx, title, sql, show_tables=None):
    print(f"-- Query {idx}: {title}")
    run_sql(conn, sql, show_tables=show_tables)
    pause()


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")

    print("-- COMPANY schema setup and data load")
    seed_database(conn)

    print("mysql> SELECT * FROM EMPLOYEE;")
    show_table(conn, "EMPLOYEE")
    print()
    print("mysql> SELECT * FROM DEPARTMENT;")
    show_table(conn, "DEPARTMENT")
    print()
    print("mysql> SELECT * FROM PROJECT;")
    show_table(conn, "PROJECT")
    print()
    pause()

    run_query(conn, 1, "Display all details of all employees.", "SELECT * FROM EMPLOYEE;")

    run_query(conn, 2, "Display ssn, lname, fname, address of employees in department 7.",
              "SELECT SSN, LNAME, FNAME, ADDRESS FROM EMPLOYEE WHERE DNO = 7;")

    run_query(conn, 3, "Birthdate and address of employee 'Franklin T. Wong'.",
              "SELECT BDATE, ADDRESS FROM EMPLOYEE WHERE FNAME='Franklin' AND MINIT='T' AND LNAME='Wong';")

    run_query(conn, 4, "Name and salary of every employee.",
              "SELECT FNAME || ' ' || COALESCE(MINIT || ' ', '') || LNAME AS EMP_NAME, SALARY FROM EMPLOYEE;")

    run_query(conn, 5, "All distinct salary values.",
              "SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY;")

    run_query(conn, 6, "Employees whose address is in Bellaire.",
              "SELECT * FROM EMPLOYEE WHERE ADDRESS LIKE '%Bellaire%';")

    run_query(conn, 7, "Employees born during the 1950s.",
              "SELECT * FROM EMPLOYEE WHERE BDATE BETWEEN '1950-01-01' AND '1959-12-31';")

    run_query(conn, 8, "Employees in department 5 with salary between 50,000 and 60,000.",
              "SELECT * FROM EMPLOYEE WHERE DNO = 5 AND SALARY BETWEEN 50000 AND 60000;")

    run_query(conn, 9, "Employees who do not have supervisors.",
              "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SUPERSSN IS NULL;")

    run_query(conn, 10, "SSN and department name for all employees.",
              "SELECT E.SSN, D.DNAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DNO = D.DNUMBER;")

    run_query(conn, 11, "Name and address of employees who work for Research department.",
              "SELECT E.FNAME, E.MINIT, E.LNAME, E.ADDRESS FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO = D.DNUMBER WHERE D.DNAME = 'Research';")

    run_query(conn, 12, "For each project in Stafford, list project number, dept number, manager lname, address, birthdate.",
              """SELECT P.PNUMBER, P.DNUM, M.LNAME, M.ADDRESS, M.BDATE
FROM PROJECT P
JOIN DEPARTMENT D ON P.DNUM = D.DNUMBER
JOIN EMPLOYEE M ON D.MGRSSN = M.SSN
WHERE P.PLOCATION = 'Stafford';""")

    run_query(conn, 13, "For each employee, retrieve employee name and immediate supervisor name.",
              """SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME,
       S.FNAME || ' ' || S.LNAME AS SUPERVISOR_NAME
FROM EMPLOYEE E
LEFT JOIN EMPLOYEE S ON E.SUPERSSN = S.SSN;""")

    run_query(conn, 14, "All combinations of Employee Name and Department Name.",
              "SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, D.DNAME FROM EMPLOYEE E CROSS JOIN DEPARTMENT D;")

    run_query(conn, 15, "Project numbers involving employee with lname Narayan as worker or manager.",
              """SELECT DISTINCT P.PNUMBER
FROM PROJECT P
LEFT JOIN WORKS_ON W ON P.PNUMBER = W.PNO
LEFT JOIN EMPLOYEE E ON W.ESSN = E.SSN
LEFT JOIN DEPARTMENT D ON P.DNUM = D.DNUMBER
LEFT JOIN EMPLOYEE M ON D.MGRSSN = M.SSN
WHERE E.LNAME = 'Narayan' OR M.LNAME = 'Narayan';""")

    run_query(conn, 16, "Increase salary by 15% for employees working on ProductX; show names and increased salary.",
              """SELECT E.FNAME || ' ' || E.LNAME AS EMP_NAME,
       ROUND(E.SALARY * 1.15, 2) AS INCREASED_SALARY
FROM EMPLOYEE E
JOIN WORKS_ON W ON E.SSN = W.ESSN
JOIN PROJECT P ON W.PNO = P.PNUMBER
WHERE P.PNAME = 'ProductX';""")

    run_query(conn, 17, "Employees and project names they work on, ordered by dept then employee first name.",
              """SELECT E.DNO, E.FNAME, E.LNAME, P.PNAME
FROM EMPLOYEE E
JOIN WORKS_ON W ON E.SSN = W.ESSN
JOIN PROJECT P ON W.PNO = P.PNUMBER
ORDER BY E.DNO, E.FNAME;""")

    run_query(conn, 18, "Employees whose salary does not match any salary in department 10.",
              "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY NOT IN (SELECT SALARY FROM EMPLOYEE WHERE DNO = 10);")

    run_query(conn, 19, "Employees who have dependent with same first name and sex.",
              """SELECT DISTINCT E.FNAME, E.LNAME
FROM EMPLOYEE E
JOIN DEPENDENT D ON E.SSN = D.ESSN
WHERE E.FNAME = D.DEPENDENT_NAME AND E.SEX = D.SEX;""")

    run_query(conn, 20, "Employee numbers who work on projects in Bellaire, Houston, or Stafford.",
              """SELECT DISTINCT W.ESSN
FROM WORKS_ON W
JOIN PROJECT P ON W.PNO = P.PNUMBER
WHERE P.PLOCATION IN ('Bellaire', 'Houston', 'Stafford');""")

    run_query(conn, 21, "Sum, max, min, avg salary for all employees.",
              "SELECT SUM(SALARY) AS TOTAL_SALARY, MAX(SALARY) AS MAX_SALARY, MIN(SALARY) AS MIN_SALARY, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE;")

    run_query(conn, 22, "Salary aggregates and employee count for Marketing department.",
              """SELECT COUNT(*) AS EMP_COUNT, SUM(E.SALARY) AS TOTAL_SALARY,
       MAX(E.SALARY) AS MAX_SALARY, MIN(E.SALARY) AS MIN_SALARY, ROUND(AVG(E.SALARY),2) AS AVG_SALARY
FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO = D.DNUMBER
WHERE D.DNAME = 'Marketing';""")

    run_query(conn, 23, "Employees with salary greater than average salary of department 10.",
              "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE WHERE DNO = 10);")

    run_query(conn, 24, "For each department: dept no, number of employees, average salary.",
              "SELECT DNO AS DEPT_NO, COUNT(*) AS EMP_COUNT, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE GROUP BY DNO;")

    run_query(conn, 25, "For each project: project number, name, and number of employees working.",
              """SELECT P.PNUMBER, P.PNAME, COUNT(W.ESSN) AS EMP_COUNT
FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER = W.PNO
GROUP BY P.PNUMBER, P.PNAME;""")

    run_query(conn, 26, "Set location='Bellaire' and dept=6 for projects with >5 employees.",
              """UPDATE PROJECT
SET PLOCATION = 'Bellaire', DNUM = 6
WHERE PNUMBER IN (
    SELECT PNO FROM WORKS_ON GROUP BY PNO HAVING COUNT(ESSN) > 5
);""", show_tables=["PROJECT"])

    run_query(conn, 27, "For each department with >10 employees, count employees earning >40000.",
              """SELECT DNO AS DEPT_NO,
       SUM(CASE WHEN SALARY > 40000 THEN 1 ELSE 0 END) AS GT_40000_COUNT
FROM EMPLOYEE
GROUP BY DNO
HAVING COUNT(*) > 10;""")

    run_query(conn, 28, "Attempt invalid PROJECT insert then remove violation by inserting DEPARTMENT.",
              "INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);")
    run_query(conn, 28, "Fix referential integrity by inserting DEPARTMENT 99, then reinsert project.",
              """INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE)
VALUES ('TempDept', 99, '888665555', '2020-01-01');""", show_tables=["DEPARTMENT"])
    run_query(conn, 28, "Re-insert previously violating project record.",
              "INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);", show_tables=["PROJECT"])

    run_query(conn, 29, "Delete dependents of employee with ssn 123456789.",
              "DELETE FROM DEPENDENT WHERE ESSN = '123456789';", show_tables=["DEPENDENT"])

    run_query(conn, 30, "Delete employee ssn=12345 and show cascading effects.",
              "DELETE FROM EMPLOYEE WHERE SSN = '12345';",
              show_tables=["EMPLOYEE", "DEPENDENT", "WORKS_ON", "DEPARTMENT"])

    run_query(conn, 31, "Alter EMPLOYEE: add EMAIL with unique constraint, then drop the column.",
              "ALTER TABLE EMPLOYEE ADD COLUMN EMAIL TEXT UNIQUE;", show_tables=["EMPLOYEE"])
    run_query(conn, 31, "Drop EMAIL column from EMPLOYEE.",
              "ALTER TABLE EMPLOYEE DROP COLUMN EMAIL;", show_tables=["EMPLOYEE"])

    print("-- All queries complete.")
    conn.close()


if __name__ == "__main__":
    main()

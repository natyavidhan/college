#!/usr/bin/env python3
"""
COMPANY schema - Markdown exporter.
Generates a file with H2 query headers, SQL blocks, and output blocks.
"""

import io
import os
import sqlite3

OUT_FILE = os.path.join(os.path.dirname(__file__), "q2_output.md")


def render_table(rows, headers):
    buf = io.StringIO()
    str_rows = [[("NULL" if v is None else str(v)) for v in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in str_rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(val))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"

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


def render_prompt(sql):
    lines = sql.strip().splitlines()
    out = f"mysql> {lines[0]}\n"
    for line in lines[1:]:
        out += f"    -> {line}\n"
    return out


def render_ok(rowcount=0):
    return f"Query OK, {rowcount} row{'s' if rowcount != 1 else ''} affected (0.00 sec)\n"


def select_output(conn, sql):
    cur = conn.execute(sql.rstrip(";"))
    headers = [d[0] for d in cur.description]
    return render_prompt(sql) + render_table(cur.fetchall(), headers)


def exec_output(conn, sql):
    cur = conn.execute(sql.rstrip(";"))
    conn.commit()
    return render_prompt(sql) + render_ok(cur.rowcount if cur.rowcount >= 0 else 0)


def table_dump(conn, table_name):
    cur = conn.execute(f"SELECT * FROM {table_name}")
    headers = [d[0] for d in cur.description]
    return f"mysql> SELECT * FROM {table_name};\n" + render_table(cur.fetchall(), headers)


def seed(conn):
    statements = [
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
        """INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES
    ('Research', 5, NULL, '1988-05-22'),
    ('Administration', 4, NULL, '1995-01-01'),
    ('Headquarters', 1, NULL, '1981-06-19'),
    ('Marketing', 7, NULL, '2000-01-01'),
    ('IT', 10, NULL, '2003-03-15'),
    ('Support', 6, NULL, '2018-01-01');""",
        """INSERT INTO EMPLOYEE (FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPERSSN, DNO) VALUES
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
('Tina', 'L', 'Ray', '555666777', '1990-01-01', '55 Support Ln, Houston, TX', 'F', 39000, '12345', 6);""",
        "UPDATE DEPARTMENT SET MGRSSN = '333445555' WHERE DNUMBER = 5;",
        "UPDATE DEPARTMENT SET MGRSSN = '987654321' WHERE DNUMBER = 4;",
        "UPDATE DEPARTMENT SET MGRSSN = '888665555' WHERE DNUMBER = 1;",
        "UPDATE DEPARTMENT SET MGRSSN = '666884444' WHERE DNUMBER = 7;",
        "UPDATE DEPARTMENT SET MGRSSN = '777665555' WHERE DNUMBER = 10;",
        "UPDATE DEPARTMENT SET MGRSSN = '12345' WHERE DNUMBER = 6;",
        """INSERT INTO DEPT_LOCATIONS VALUES
(1,'Houston'),
(4,'Stafford'),
(5,'Bellaire'),
(5,'Sugarland'),
(5,'Houston'),
(6,'Houston'),
(7,'Bellaire'),
(10,'Houston');""",
        """INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4),
('MarketPulse', 40, 'Bellaire', 7),
('CloudShift', 50, 'Houston', 10);""",
        """INSERT INTO WORKS_ON VALUES
('123456789',1,32.5),('123456789',2,7.5),('666884444',3,40.0),('453453453',1,20.0),
('453453453',2,20.0),('333445555',2,10.0),('333445555',3,10.0),('333445555',10,10.0),
('333445555',20,10.0),('999887777',30,30.0),('999887777',10,10.0),('987987987',10,35.0),
('987987987',30,5.0),('987654321',30,20.0),('987654321',20,15.0),('888665555',20,NULL),
('777665555',50,20.0),('222334444',50,25.0),('111223333',50,15.0),('12345',40,22.0),
('555666777',40,18.0);""",
        """INSERT INTO DEPENDENT VALUES
('333445555','Alice','F','1986-04-05','Daughter'),
('333445555','Theodore','M','1983-10-25','Son'),
('333445555','Joy','F','1958-05-03','Spouse'),
('987654321','Abner','M','1942-02-28','Spouse'),
('123456789','Michael','M','1988-01-04','Son'),
('123456789','Alice','F','1988-12-30','Daughter'),
('123456789','Elizabeth','F','1967-05-05','Spouse'),
('12345','Temp','M','2012-08-08','Son');""",
    ]

    out = io.StringIO()
    for s in statements:
        cur = conn.execute(s.rstrip(";"))
        conn.commit()
        if cur.description:
            headers = [d[0] for d in cur.description]
            out.write(render_prompt(s if s.strip().endswith(";") else s + ";"))
            out.write(render_table(cur.fetchall(), headers))
        else:
            out.write(render_prompt(s if s.strip().endswith(";") else s + ";"))
            out.write(render_ok(cur.rowcount if cur.rowcount >= 0 else 0))
        out.write("\n")
    return out.getvalue()


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")

    md = io.StringIO()
    md.write("## Create Tables\n\n")
    setup_output = seed(conn)
    md.write("```\n" + setup_output.strip() + "\n```\n\n")

    md.write("## Initial Table Data\n\n")
    init_sql = "SELECT * FROM EMPLOYEE;\nSELECT * FROM DEPARTMENT;\nSELECT * FROM PROJECT;"
    init_out = table_dump(conn, "EMPLOYEE") + "\n" + table_dump(conn, "DEPARTMENT") + "\n" + table_dump(conn, "PROJECT")
    md.write("```sql\n" + init_sql + "\n```\n\n")
    md.write("```\n" + init_out.strip() + "\n```\n\n")

    def add_query(qno, desc, sql, out):
        md.write(f"## {qno}: {desc}\n\n")
        md.write(f"```sql\n{sql.strip()}\n```\n\n")
        md.write(f"```\n{out.strip()}\n```\n\n")

    q = []
    q.append((1, "Display all details of all employees working in the company.", "SELECT * FROM EMPLOYEE;", "select"))
    q.append((2, "Display ssn, lname, fname, address of employees who work in department no 7.", "SELECT SSN, LNAME, FNAME, ADDRESS FROM EMPLOYEE WHERE DNO = 7;", "select"))
    q.append((3, "Retrieve the birthdate and address of Franklin T. Wong.", "SELECT BDATE, ADDRESS FROM EMPLOYEE WHERE FNAME='Franklin' AND MINIT='T' AND LNAME='Wong';", "select"))
    q.append((4, "Retrieve the name and salary of every employee.", "SELECT FNAME || ' ' || COALESCE(MINIT || ' ', '') || LNAME AS EMP_NAME, SALARY FROM EMPLOYEE;", "select"))
    q.append((5, "Retrieve all distinct salary values.", "SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY;", "select"))
    q.append((6, "Retrieve all employee names whose address is in Bellaire.", "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE ADDRESS LIKE '%Bellaire%';", "select"))
    q.append((7, "Retrieve all employees who were born during the 1950s.", "SELECT * FROM EMPLOYEE WHERE BDATE BETWEEN '1950-01-01' AND '1959-12-31';", "select"))
    q.append((8, "Retrieve all employees in department 5 with salary between 50000 and 60000.", "SELECT * FROM EMPLOYEE WHERE DNO = 5 AND SALARY BETWEEN 50000 AND 60000;", "select"))
    q.append((9, "Retrieve names of all employees who do not have supervisors.", "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SUPERSSN IS NULL;", "select"))
    q.append((10, "Retrieve SSN and department name for all employees.", "SELECT E.SSN, D.DNAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DNO = D.DNUMBER;", "select"))
    q.append((11, "Retrieve name and address of employees in Research department.", "SELECT E.FNAME, E.MINIT, E.LNAME, E.ADDRESS FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO = D.DNUMBER WHERE D.DNAME='Research';", "select"))
    q.append((12, "For each Stafford project, list project no, controlling dept no, manager lname, address, birthdate.", "SELECT P.PNUMBER, P.DNUM, M.LNAME, M.ADDRESS, M.BDATE FROM PROJECT P JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE P.PLOCATION='Stafford';", "select"))
    q.append((13, "For each employee retrieve employee name and immediate supervisor name.", "SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, S.FNAME || ' ' || S.LNAME AS SUPERVISOR_NAME FROM EMPLOYEE E LEFT JOIN EMPLOYEE S ON E.SUPERSSN=S.SSN;", "select"))
    q.append((14, "Retrieve all combinations of Employee Name and Department Name.", "SELECT E.FNAME || ' ' || E.LNAME AS EMPLOYEE_NAME, D.DNAME FROM EMPLOYEE E CROSS JOIN DEPARTMENT D;", "select"))
    q.append((15, "List project numbers that involve Narayan as worker or department manager.", "SELECT DISTINCT P.PNUMBER FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO LEFT JOIN EMPLOYEE E ON W.ESSN=E.SSN LEFT JOIN DEPARTMENT D ON P.DNUM=D.DNUMBER LEFT JOIN EMPLOYEE M ON D.MGRSSN=M.SSN WHERE E.LNAME='Narayan' OR M.LNAME='Narayan';", "select"))
    q.append((16, "Increase salary by 15% for employees working on ProductX and show name + increased salary.", "SELECT E.FNAME || ' ' || E.LNAME AS EMP_NAME, ROUND(E.SALARY * 1.15, 2) AS INCREASED_SALARY FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PNAME='ProductX';", "select"))
    q.append((17, "Employees and project name each works in, ordered by department then first name.", "SELECT E.DNO, E.FNAME, E.LNAME, P.PNAME FROM EMPLOYEE E JOIN WORKS_ON W ON E.SSN=W.ESSN JOIN PROJECT P ON W.PNO=P.PNUMBER ORDER BY E.DNO, E.FNAME;", "select"))
    q.append((18, "Employees whose salary does not match salary of any employee in department 10.", "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY NOT IN (SELECT SALARY FROM EMPLOYEE WHERE DNO=10);", "select"))
    q.append((19, "Employees with dependent having same first name and same sex as employee.", "SELECT DISTINCT E.FNAME, E.LNAME FROM EMPLOYEE E JOIN DEPENDENT D ON E.SSN=D.ESSN WHERE E.FNAME=D.DEPENDENT_NAME AND E.SEX=D.SEX;", "select"))
    q.append((20, "Employee numbers of employees who work on project in Bellaire/Houston/Stafford.", "SELECT DISTINCT W.ESSN FROM WORKS_ON W JOIN PROJECT P ON W.PNO=P.PNUMBER WHERE P.PLOCATION IN ('Bellaire','Houston','Stafford');", "select"))
    q.append((21, "Sum, max, min, avg salary of all employees.", "SELECT SUM(SALARY) AS TOTAL_SALARY, MAX(SALARY) AS MAX_SALARY, MIN(SALARY) AS MIN_SALARY, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE;", "select"))
    q.append((22, "Salary aggregates and employee count for Marketing department.", "SELECT COUNT(*) AS EMP_COUNT, SUM(E.SALARY) AS TOTAL_SALARY, MAX(E.SALARY) AS MAX_SALARY, MIN(E.SALARY) AS MIN_SALARY, ROUND(AVG(E.SALARY),2) AS AVG_SALARY FROM EMPLOYEE E JOIN DEPARTMENT D ON E.DNO=D.DNUMBER WHERE D.DNAME='Marketing';", "select"))
    q.append((23, "Employees whose salary is greater than average salary of department 10.", "SELECT FNAME, MINIT, LNAME FROM EMPLOYEE WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE WHERE DNO=10);", "select"))
    q.append((24, "For each department retrieve dept no, employee count, avg salary.", "SELECT DNO AS DEPT_NO, COUNT(*) AS EMP_COUNT, ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE GROUP BY DNO;", "select"))
    q.append((25, "For each project retrieve project no, project name, number of employees.", "SELECT P.PNUMBER, P.PNAME, COUNT(W.ESSN) AS EMP_COUNT FROM PROJECT P LEFT JOIN WORKS_ON W ON P.PNUMBER=W.PNO GROUP BY P.PNUMBER, P.PNAME;", "select"))
    q.append((26, "Change location and department for projects with >5 employees.", "UPDATE PROJECT SET PLOCATION='Bellaire', DNUM=6 WHERE PNUMBER IN (SELECT PNO FROM WORKS_ON GROUP BY PNO HAVING COUNT(ESSN) > 5);", "exec"))
    q.append((27, "For each department with >10 employees, count employees with salary >40000.", "SELECT DNO AS DEPT_NO, SUM(CASE WHEN SALARY > 40000 THEN 1 ELSE 0 END) AS GT_40000_COUNT FROM EMPLOYEE GROUP BY DNO HAVING COUNT(*) > 10;", "select"))
    q.append((28, "Insert violating PROJECT record.", "INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);", "exec"))
    q.append((28, "Fix violation by inserting DEPARTMENT record.", "INSERT INTO DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE) VALUES ('TempDept', 99, '888665555', '2020-01-01');", "exec"))
    q.append((28, "Reinsert previously violating PROJECT record.", "INSERT INTO PROJECT (PNAME, PNUMBER, PLOCATION, DNUM) VALUES ('BrokenRef', 99, 'Nowhere', 99);", "exec"))
    q.append((29, "Delete all dependents of employee 123456789.", "DELETE FROM DEPENDENT WHERE ESSN='123456789';", "exec"))
    q.append((30, "Delete employee 12345 to observe cascading/set default/set null behavior.", "DELETE FROM EMPLOYEE WHERE SSN='12345';", "exec"))
    q.append((31, "Alter Employee table: add EMAIL column with unique constraint.", "ALTER TABLE EMPLOYEE ADD COLUMN EMAIL TEXT UNIQUE;", "exec"))
    q.append((31, "Alter Employee table: drop EMAIL column.", "ALTER TABLE EMPLOYEE DROP COLUMN EMAIL;", "exec"))

    for num, desc, sql, kind in q:
        if kind == "select":
            out = select_output(conn, sql)
        else:
            try:
                out = exec_output(conn, sql)
            except Exception as e:
                out = render_prompt(sql) + f"ERROR 1452 (23000): {e}\n"

            if num in (26, 28, 29, 30, 31):
                if num == 26:
                    out += "\n" + table_dump(conn, "PROJECT")
                elif num == 28:
                    out += "\n" + table_dump(conn, "DEPARTMENT") + "\n" + table_dump(conn, "PROJECT")
                elif num == 29:
                    out += "\n" + table_dump(conn, "DEPENDENT")
                elif num == 30:
                    out += "\n" + table_dump(conn, "EMPLOYEE") + "\n" + table_dump(conn, "DEPENDENT") + "\n" + table_dump(conn, "WORKS_ON") + "\n" + table_dump(conn, "DEPARTMENT")
                elif num == 31:
                    out += "\n" + table_dump(conn, "EMPLOYEE")

        add_query(num, desc, sql, out)

    conn.close()

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(md.getvalue())

    print(f"Done! Written: {OUT_FILE}")


if __name__ == "__main__":
    main()

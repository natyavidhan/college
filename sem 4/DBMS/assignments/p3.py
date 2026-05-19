"""
                Users
+------------------------------------+
| id | name       | age | city       |
+----+------------+-----+------------+
| 1  | John Doe   | 30  | New York   |
| 2  | Jane Smith | 25  | Los Angeles|
| 3  | Bob Johnson| 40  | Chicago    |
+----+------------+-----+------------+

-- Create user
CREATE USER 'natya'@'localhost' IDENTIFIED BY 'password';

-- Create role
CREATE ROLE 'admin';

-- Grant privileges to role
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'admin';

-- Revoke privileges from role
REVOKE DELETE ON *.* FROM 'admin';

-- Create index
CREATE INDEX idx ON users (name);
"""


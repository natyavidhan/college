# Unit 1: Introduction to Database

## Characteristics, Architecture, and Data Independence

1. What are the four different types of database users. Specify their roles. **Source:**

- 2210 / 2019 / IV
- Question 1(b)

2. Differentiate between the logical and physical data independence with the help of an example. **Source:**

- 2798 / 2017 / IV
- Question 1(e)

3. How does DDL support the implementation of the three-schema architecture? **Source:**

- 32341403 / 2021 / IV
- Question 6

4. Describe the three-schema architecture with the help of a suitable diagram. In this context, give a suitable example of data independence. **Source:**

- 4095 / 2024 / IV
- Question 3(b)

5. Compare and contrast the traditional file processing approach with the database approach in the context of the self-describing nature of the database system. **Source:**

- 4095 / 2024 / IV
- Question 6(a)

6. Differentiate between the following: (i) Database Definition language and Database Manipulation language (ii) Logical data independence and Physical data independence (iii) Database Intension and Database Extension **Source:**

- 4803 / 2023 / IV
- Question 1(h)

7. What is data independence? Illustrate the concepts of logical data independence and physical data independence with examples. **Source:**

- 6514 / 2018 / IV
- Question 1(e)

8. Give four advantages of the DBMS approach over the conventional file system approach. **Source:**

- 6514 / 2018 / IV
- Question 6(b)

## Frequency Analysis

- **Most repeated questions:** The difference between logical and physical data independence is highly tested, appearing in almost every paper (2017, 2018, 2023, 2024). The three-schema architecture is also a recurring concept.
- **Frequently asked concepts:** Data independence, DBMS vs. traditional file system, database users, and three-schema architecture.
- **Trend analysis across years:** The focus consistently remains on foundational concepts, particularly demonstrating an understanding of how data independence works within the three-schema architecture.

---

# Unit 2: Entity Relationship (ER) Modeling

## ER Diagrams and Conceptual Modeling

1. Why is it necessary to give role names in a recursive relationship? **Source:**

- 2210 / 2019 / IV
- Question 1(g)
- 4803 / 2023 / IV
- Question 1(c)

2. Give EER diagram illustrating each of the following : (i) total-disjoint specialization and (ii) partial-disjoint specialization **Source:**

- 2210 / 2019 / IV
- Question 1(i)

3. A university registrar's office maintains data about the following entities : (i) Courses, including number, title, credits, syllabus, and prerequisites; (ii) Course offerings, including course number, year, semester, section number, instructor(s), timings, and classroom; (iii) Students, including student-id, name, and program; (iv) Instructors, including identification number, name, department, and title. Design an ER schema for this application. Specify key attribute of each entity type and structural constraints on each relationship type. **Source:**

- 2210 / 2019 / IV
- Question 2(a)

4. For the given binary relationship, suggest the cardinality ratio of the relationship based on the general context of entity types and state the context clearly : Entity1 Entity2 College Principal Student Course Course Book Book Author **Source:**

- 2210 / 2019 / IV
- Question 4(b)

5. Suppose you are given the following requirements for a database for the National Hockey League (NHL). The NHL has many teams.

- each team has a name, a city, a coach, a captain, and a set of players,
- each player belongs to only one team,
- each player has a name, a position (such as left wing or goalie), a skill level, and a set of injury records,
- every team has a team captain, a team captain is also a player.
- injury record of each player is kept with its description (injury_date, injury_type).
- a game is played between two teams (referred to as host_team and guest_team) and has a date (such as April 11th, 2017) and a score (such as 2 to 1). Identify: (i) Entities of interest (ii) Attributes of interest for each entity (iii) Draw the ER diagram for the above mentioned scenario. Also specify clearly, all constraints on the relationships in the diagram. State any assumptions that you make. **Source:**
- 2798 / 2017 / IV
- Question 2

6. What is cardinality ratio? For the binary relationships below, suggest cardinality ratios based on the meaning of the entity types. State any assumptions you make. ENTITY 1 Cardinality Ratio ENTITY 2 STUDENT _______ TEACHER COUNTRY _______ CURRENT_PRESIDENT LIBRARY _______ BOOK ITEM (that can be found in an order) _______ ORDER **Source:**

- 2798 / 2017 / IV
- Question 3(b)

7. Illustrate each of the following concepts with the help of an example: (i) Total and disjoint specializations/generalizations (ii) Recursive Relationship (iii) Weak Entity **Source:**

- 2798 / 2017 / IV
- Question 7(a)

8. The XYZ Co. deals with several pharmaceutical companies. Its data requirements include the following specifications:

- Patients are identified by SSN, and their names, addresses, and also age.
- Doctors are identified by SSN. For each doctor, the name, specialty and years of experience must be recorded.
- Each pharmaceutical company is identified by name and has a phone number.
- For each medicine, the trade name and formula must be recorded. Each medicine is sold by a given pharmaceutical company, and the trade name identifies a medicine uniquely from among the products of that company. If a pharmaceutical company is deleted, you need not keep track of its products any longer.
- Each pharmacy has a name, address, and phone number.
- Each pharmacy sells several drugs and has a price for each. A medicine could be sold at several pharmacies, and the price could vary from one pharmacy to another.
- Doctors prescribe medicine for patients. A doctor would prescribe one or more medicine for several patients, and a patient could obtain prescriptions from several doctors. Each prescription has a date and a quantity associated with it. Draw an ER diagram that captures the above information. Clearly state any constraints that you assume. Also, extend the above ER diagram to EER using one specialization. **Source:**
- 32341403 / 2021 / IV
- Question 1

9. Also, describe the role of recursive relationships in the context of the above diagram. (Note: refers to airplane diagram mapped in Unit 5) **Source:**

- 32341403 / 2021 / IV
- Question 3 (Subpart)

10. Identify multivalued and composite attributes from the following complex attribute : {Hobby_stats (Name (First_name, Last_name), {Phone (Area_code, Phone_number)}, {Hobbies})} **Source:**

- 4095 / 2024 / IV
- Question 1(g)

11. Consider the following ER diagram and answer the questions that follow : (i) Specify the role names for the given relationship. (ii) Determine the cardinality ratio. Justify your answer. (iii) Determine the participation constraint. Justify your answer. **Source:**

- 4095 / 2024 / IV
- Question 2(b)

12. ABC shipping company prides itself on having up-to-date information on the processing and current location of each shipped item. To do this, the company relies on its database management system. Shipped items can be characterized by item number (unique), weight, dimensions, insurance amount, destination, and final delivery date. Shipped items are received into the system at a single retail center. Retail centers are characterized by their type, unique ID, and address. Shipped items arrive at their destination via one or more standard transportation events (i.e., flights, truck deliveries). These transportation events are characterized by a unique schedule number, a type (e.g., flight, truck), and a deliveryRoute. Create an Entity Relationship diagram that captures this information about the company. Also, indicate the primary key, cardinality, and participation constraints. **Source:**

- 4095 / 2024 / IV
- Question 7(c)

13. Give an example of the following with its proper notation used in ER Model (i) Identifying Relationship (ii) Complex attribute **Source:**

- 4803 / 2023 / IV
- Question 1(g)

14. Consider a database PROJECT_EXAMINATION that maintains data about the project reports submitted for consideration by the examiners. Comments by the examiners are recorded for use in the project selection process. The database system caters primarily to examiners who record answers to pre-decided questions for each report they evaluate. The examiners make recommendations regarding whether to accept or reject the project. The data requirements are summarized as follows :

- Students write the project reports.
- Students are uniquely identified by e-mail id. first and last names are also recorded.
- Each project is assigned a unique identifier by the system and is described by a title, abstract, and the name of the electronic file containing the project report.
- Multiple students may be involved in the same project, but one of the students is designated as the coordinator.
- Examiners of project reports are uniquely identified by e-mail address. Each examiner's first name, last name, phone number, areas of interest are also recorded.
- Each project report is assigned to two and four reviewers. An examiner rates each report assigned to him or her on a scale of 1 to 10 in four categories: technical merit, readability, originality, and presentation. Finally, each examiner provides an overall recommendation regarding each report. Design an Entity-Relationship Diagram (ER) for the above database and identify existing composite attributes (if any). **Source:**
- 4803 / 2023 / IV
- Question 2(a)

15. For the given binary relationship, suggest the cardinality ratio of the relationship based on the general context of entity types and state the context clearly : Entity Set1 Entity Set2 I. Country President II. Teacher Course III. Players Team IV. Book Author **Source:**

- 4803 / 2023 / IV
- Question 2(b)

16. Differentiate between a Specialization Hierarchy and a Specialization Lattice using appropriate examples. **Source:**

- 4803 / 2023 / IV
- Question 4(b)

17. Consider a movie database in which data is recorded about the movie industry. The data requirements are summarized as follows:

- Each movie is identified by title and year of release. Each movie has a length in minutes. Each movie has a production company and is classified into one or more genres (such as horror, action, drama, and so forth). Each movie has one or more directors and one or more actors that appear in it. Each movie also has a plot outline. Finally, each movie has zero or more quotable quotes, each of which is spoken by a particular actor appearing in the movie.
- Actors are identified by name and date of birth and appear in one or more movies. Each actor in the movie has a role in it.
- Directors are identified by name and date of birth and direct one or more movies. It is possible for a director to act in a movie that he directed.
- Production companies are identified by name and each has an address. A production company produces one or more movies. Identify : (i) Entities of interest. (ii) Attributes of interest for each entity. (iii) Draw an ER diagram for the above scenario. Also specify clearly all constraints on the relationships in the diagram. State any assumptions that you make. **Source:**
- 6514 / 2018 / IV
- Question 2

18. Illustrate the use of each of the following constraints that can be applied to specializations/generalizations with the help of an example : (i) Disjoint Total (ii) Disjoint Partial (iii) Overlapping Partial. **Source:**

- 6514 / 2018 / IV
- Question 7(a)

## Frequency Analysis

- **Most repeated questions:** Drawing a complete ER diagram from a given case study is asked in every single paper (10+ marks). Asking to suggest cardinality ratios for given real-world entity pairs is also highly recurrent. Recursive relationship concepts are commonly asked.
- **Frequently asked concepts:** Cardinality ratios, participation constraints, recursive relationships, weak entities, identifying relationships, and specialization/generalization constraints.
- **Trend analysis across years:** The paper structure always tests the application of ER concepts via a long scenario-based design question. In recent years, EER concepts like specialization/generalization constraints (total, partial, disjoint, overlapping) and hierarchy vs lattice have gained prominence.

---

# Unit 3: Relational Data Model

## Relational Constraints and Relational Algebra

1. Justify that primary key cannot be null. **Source:**

- 2210 / 2019 / IV
- Question 1(c)

2. Consider the tables T1 and T2 given below : T1 A B C 1 3 1 3 2 1 T2 X Y Z 1 3 1 2 5 4 Show the results of the following operations : (i) T1 bowtie_{T1.X=T2.C} T2 (ii) T1 intersect T2 (iii) pi_{T1.2, T2.C} (sigma_{T1.Y=T2.B} (T1 x T2)) **Source:**

- 2210 / 2019 / IV
- Question 1(f)

3. Consider the following relation STUDENT : STUDENT ID NAME COURSE PHONENO. PROJECTNO PROJECTNAME Assume that ID is primary key and the following dependency holds in the above relation: PROJECTNO -> PROJECTNAME Give an instance of the STUDENT table and in the context of that instance illustrate the following concepts : (i) updation anomaly (ii) insertion anomaly (iii) deletion anomaly **Source:**

- 2210 / 2019 / IV
- Question 4(a)

4. Consider the given relations : WORKER (ID, Name, Salary, JoiningDate, Department#) DEPARTMENT (DepID, DName, Location, Mgr#) Write following queries in relational algebra for the relations given above :- (i) Display name of all the workers along with their department name and manager name of that department. (ii) Count number of workers working in finance department. (iii) Show number of workers working in each department along with department name. (iv) Find Average salary of each department. (v) Retrieve the names of workers who have joined after the year 2010. **Source:**

- 2210 / 2019 / IV
- Question 5

5. Consider the database schema given below :- Book (Book_Id, Title, Publisher) Book_copies (Book_Id, Branch_Id, No_of_Copies) Library_branch (Branch_Id, BranchName, Address) Book_Authors (Book_Id, AuthorName) Depict the referential integrity constraints diagrammatically using schema diagram. **Source:**

- 2210 / 2019 / IV
- Question 7(b)

6. Consider the following tables A and B: (Note: Labels inside question refer to R and S) R X Y Z 10 a 7 25 b 8 30 a 9 S A B C 25 c 9 30 d 8 25 c 7 The attributes X, Y, Z are domain compatible with the attributes A, B, C respectively. Show the results of the following operations: (i) R U S (ii) R bowtie_{A=Z AND B=C} S (iii) R bowtie_{R.X=S.A} S **Source:**

- 2798 / 2017 / IV
- Question 1(d)

7. Consider the tables given below and answer the following queries in relational algebra: item (ItemCode, ItemName, ItemPrice, ItemQty) customer (CustCode, CustName, CustAddress, CustPhone) issue(IssueCode, ItemCode, IssueDate, IssueQty, CustCode) (i) Find the names of distinct customers who have got issued any item with price above 1000/-. (ii) Give the details of the costliest item. (iii) Give the details of all those customers who bought an item with item code '1005'. **Source:**

- 2798 / 2017 / IV
- Question 6(a)
- 6514 / 2018 / IV
- Question 6(a)

8. Consider the following relations: Employee (Eno, Ename, Dno) Department (Dnum, Dname, Dloc) Here, Eno is a Primary Key and Dno is a Foreign Key in EMPLOYEE relation. For each of the following operations, indicate whether it results in constraint violation and if so, why? (i) Insert <5, 'Pooja', 10> in Employee (ii) Insert <5, 'Reeta', 7> in Employee (iii) Delete <7, 'XX', 'Delhi'> from Department (iv) Insert <10, 'AA', 'Delhi'> in Department **Source:**

- 2798 / 2017 / IV
- Question 6(b)

9. Consider the relations given below: Doctor (SSN, Firstname, Lastname, Speciality, YearsOfExp, PhoneNum) Patient (SSN, Firstname, Lastname, Address, DOB, PrimaryDoc_SSN) Medicine (TradeName, UnitPrice, GenericFlag) Prescription (ID, Date, Doctor_SSN, Patient_SSN) Prescription_Medicine (PrescriptionID, TradeName, Quantity) where Medicine.GenericFlag represents whether or not the medicine is generic (True or False). Patient.PrimaryDoc_SSN is a foreign key to Doctor.SSN PrescriptionID of Prescription_Medicine relation is a foreign key to ID attribute of Prescription relation. Prescription_Medicine.TradeName refers to Medicine.TradeName Precription.Doctor_SSN and Prescription.Patient_SSN are foreign keys to Doctor.SSN and Patient.SSN respectively. Write the following queries in SQL and Relational Algebra.

- List the TradeName of generic medicine with unit price less than Rs 150.
- List the names of patients whose primary doctor is 'Rakesh Sharma'
- List the names of doctors who are not primary doctors to any patient
- For medicines written in more than 20 prescriptions, report the trade name and the total quantity prescribed.
- List the SSN of patients who have 'Paracetamol' and 'Vitamin' trade names in one prescription
- List the SSN of distinct patients who have 'Paracetamol' prescribed to them by a doctor named 'Rakesh Sharma'.
- List the first and last name of patients who have no prescriptions written by doctors other than their primary doctors. _(Note: Relational Algebra translations for these queries fall under Unit 3)_ **Source:**
- 32341403 / 2021 / IV
- Question 2

10. Consider the following two relations R1 and R2: R1 P Q S 10 a 5 15 b 8 5 a 6 R2 A B C 10 b 6 25 c 1 10 b 5 Show the result of the following relational queries:

- R1 bowtie_{R1.P=R2.A} R2
- R1 bowtie_{R1.Q=R2.B} R2
- R1 * R2
- R1 bowtie_{(R1.P=R2.A AND R1.R=R2.C)} R2 **Source:**
- 32341403 / 2021 / IV
- Question 6 (Subpart 1)

11. Consider a relational schema comprising three relations as follows: S represents Sailors(sid, name, rating, age) B represents Boats (bid, name, color) R represents Reserves (sid, bid, day, rname) Draw a query tree to show a possible order of execution for the following relational expression: pi_{sid, sname, age} (sigma_{age<30} (sigma_{color='red'} (sigma_{bid=bid} (B x sigma_{sid=sid} (S x R))))) **Source:**

- 32341403 / 2021 / IV
- Question 6 (Subpart 2)

12. Consider the following relations for a database that keeps track of business trips of salespersons working in a sales office : SALESPERSON (SSN, name, joiningDate, supervisorSSN) TRIP (tripID, SSN, fromCity, toCity, departureDate, returnDate) EXPENSE (tripID, accountNo, amount) The sales office maintains multiple bank accounts. A trip can be charged to one or more accounts. Specify the foreign keys for the above relations. **Source:**

- 4095 / 2024 / IV
- Question 1(d)

13. Consider the following relations R and S : R A B C D 15 1 15 a 20 2 25 a 25 4 20 b 15 1 25 a 30 2 20 b S B D E 1 a 15 3 a 20 1 a 25 2 b 30 3 b null Show the output for the following relational statements : (i) R bowtie_{R.B = S.B} S (ii) R bowtie_{R.C = S.E} S **Source:**

- 4095 / 2024 / IV
- Question 1(e)

14. Consider the following relational schema : Suppliers(sID: integer, sName: string, address: string) Parts(pID: integer, pName: string, color: string) Catalog(sID: integer, pID: integer, cost: real) Write relational algebra expressions to perform the following : (i) Find the names of suppliers who supply a red part. (ii) List the IDs and names of parts with an entry in the table Catalog. **Source:**

- 4095 / 2024 / IV
- Question 1(f)

15. Consider the following relation StudentCourse. studentID studentName CGPA courseID courseName credits 123 Shyam 9 C118 C++ 4 132 Shyam 8.5 C121 Java 4 131 Mohan 7.5 C118 C++ 4 135 Vijay 8 C118 C++ 4 Which of the following commands result in an update anomaly? Justify your answer. (i) DELETE FROM StudentCourse WHERE studentID = 132 (ii) UPDATE StudentCourse SET credits = 3 WHERE courseID = 118 **Source:**

- 4095 / 2024 / IV
- Question 1(i)

16. Consider the following relation schema : Student(SSN, Name, Major, Birthdate) Course(CourseId, CourseName) Enroll(SSN, CourseId, Duration) Which of the relational model constraints may be violated by the following operations? Justify your answer in each case. (i) Insert a record in the Enroll table. (ii) Delete a record from the Student table. **Source:**

- 4095 / 2024 / IV
- Question 3(a)

17. Consider the following two tables, T1 and T2 : T1 P Q R 10 a 5 15 b 8 25 a 6 T2 A B C 10 b 6 15 c 3 10 b 5 Show the results of the following operations : (i) pi_T (T1 X T2) (ii) T1 - T2 (iii) T1 intersect T2 **Source:**

- 4095 / 2024 / IV
- Question 6(c)

18. Consider the following Medical Database relations to keep track of Patients and Physicians : Patient (PP#, PName) Physician (Dname, Specialization) Test (PP#, Test_name, Date, Time, Dname) Identify the primary and foreign keys for the relations given above (State any assumptions made). **Source:**

- 4803 / 2023 / IV
- Question 1(f)

19. Find the output of the following expressions in relational algebra on the tables A, B1, B2, B3 as given below : A1 S.No. P.No. S1 P1 S1 P2 S1 P3 S1 P4 S2 P1 S2 P2 S3 P2 S4 P2 S4 P4 B1 P.No. P2 P4 B2 P.No. P2 B3 P.No. P1 P2 P4 (i) B1-B2 (ii) A/B3, where '/' is a division operator. **Source:**

- 4803 / 2023 / IV
- Question 1(i)

20. Consider the Relation given below : STUDENT_COURSE Name Course Grade Ph_no Major Department Does this given relation STUDENT_COURSE suffer from any of the following anomalies? Justify your answers using appropriate example. (i) Insertion (ii) Deletion (iii) Modification **Source:**

- 4803 / 2023 / IV
- Question 1(j)

21. Consider the following relations for the EMP_PROJ database with the following relations : Employee (Emp#, Name, Age, Salary, City, Mobile) Allotted (Project#, Emp#) Project (Project#, Project_Name, Project_Manager) Write the following queries in Relational Algebra for the relations given above:- (i) Display the project details of projects managed by "James". (ii) Count the number of employees working on the "Artificial Intelligence" Project. **Source:**

- 4803 / 2023 / IV
- Question 6(b)

22. Consider the following tables A and B : A X Y Z 15 a 7 25 b 8 35 d 6 B U V W 25 a 9 35 d 6 25 c 7 The attributes X, Y, Z are domain compatible with the attributes U, V, W respectively. Show the results of the following operations : (i) A U B (ii) A bowtie_{A.X=B.U} B (iii) pi_{A.Z, B.W} (sigma_{A.Y=B.V} (A x B)). **Source:**

- 6514 / 2018 / IV
- Question 1(d)

23. Consider the following relations : Student SId Sname CNum 1 Anu 6 2 Shyam 8 3 Rakesh 6 Course CNo Cname Dept 6 XX Maths 7 YY CompSc 8 ZZ English Here, SId is a Primary Key and CNum is a Foreign Key in Student relation. CNo is primary in Course relation. For each of the following operations, indicate whether it results in constraint violation and if so, why ? (i) Insert < 4, 'Preeti', 10 > in Student (ii) Insert < 5, 'Reena', 7 > in Student (iii) Delete < 6, 'XX', 'Maths' > from Dept (iv) Insert < 10, 'AA', 'Electronics' > in Course **Source:**

- 6514 / 2018 / IV
- Question 7(b)

## Frequency Analysis

- **Most repeated questions:** Showing the step-by-step output of Relational Algebra operations (like Union, Join, Cartesian Product, Projection) on small given sample tables is asked very frequently (2017, 2018, 2019, 2021, 2023, 2024). Identifying anomalies in a given table is also very common. Evaluating constraint violations for specific INSERT/DELETE operations on related tables appears multiple times.
- **Frequently asked concepts:** Relational Algebra (Joins, Selection, Projection, Set operations), Update anomalies (Insertion, Deletion, Modification), Relational constraints (Entity integrity, Referential integrity).
- **Trend analysis across years:** Consistently tests the mechanical execution of Relational Algebra operators. The skill to identify foreign keys and assess referential integrity violations is standard. There is a slight shift towards more complex algebra expressions and query trees in recent years.

---

# Unit 4: Structured Query Language (SQL)

## SQL DDL, DML, and Queries

1. Give SQL command to create a relational table T having attributes A, B, C, D where :

- A is a number (maximum 10 digits in length) and cannot contain null values.
- B is a character string (50 maximum characters in length)
- (A, B) form the primary key
- C and D are integer values.
- Default value of C is 6
- D is a foreign key referring to E from another table S of the database (assuming S is already created). **Source:**
- 2210 / 2019 / IV
- Question 1(h)
- 2798 / 2017 / IV
- Question 1(c) (Identical phrasing but different attribute names T1,T2,T3,T4)

2. Consider the following relations : CUSTOMER(Customer#, Customer_Name, City, Product#) PRODUCT(Prod#, Prod_Name, Prod_Details) (i) Write a command to insert a new attribute Price in PRODUCT relation. (ii) Write a command to delete rows from PRODUCT table for Prod_Name = 'P2'. (iii) Retrieve the list of customers who have purchased product with Prod_Name as 'P3' and 'P4'. (iv) Retrieve the total number of products bought by each customer. **Source:**

- 2210 / 2019 / IV
- Question 3(a)

3. Differentiate between Alter table and Update table command in SQL with the help of suitable example. **Source:**

- 2798 / 2017 / IV
- Question 1(g)

4. Consider the following database giving information of various branches of a library: Book (BookId, title, PublisherName) Library_Branch (BranchId, BranchName, address) Book_Copies(BookId, BranchId, NoOfCopies) Book_Loans (BookId, BranchId, CardNo, DateOut, DueDate) Answer the following queries in SQL: (i) For each library branch, list the number of copies of each title. (ii) How many copies of the book titled, 'Fundamentals of Database Systems' are owned by each library branch? (iii) For each book that is loaned out from 'CP' branch, for which the due date is today, retrieve the book title and publisher name. **Source:**

- 2798 / 2017 / IV
- Question 3(a)

5. Consider the relations given below: Doctor (SSN, Firstname, Lastname, Speciality, YearsOfExp, PhoneNum) Patient (SSN, Firstname, Lastname, Address, DOB, PrimaryDoc_SSN) Medicine (TradeName, UnitPrice, GenericFlag) Prescription (ID, Date, Doctor_SSN, Patient_SSN) Prescription_Medicine (PrescriptionID, TradeName, Quantity) where Medicine.GenericFlag represents whether or not the medicine is generic (True or False). Patient.PrimaryDoc_SSN is a foreign key to Doctor.SSN PrescriptionID of Prescription_Medicine relation is a foreign key to ID attribute of Prescription relation. Prescription_Medicine.TradeName refers to Medicine.TradeName Precription.Doctor_SSN and Prescription.Patient_SSN are foreign keys to Doctor.SSN and Patient.SSN respectively. Write the following queries in SQL.

- List the TradeName of generic medicine with unit price less than Rs 150.
- List the names of patients whose primary doctor is 'Rakesh Sharma'
- List the names of doctors who are not primary doctors to any patient
- For medicines written in more than 20 prescriptions, report the trade name and the total quantity prescribed.
- List the SSN of patients who have 'Paracetamol' and 'Vitamin' trade names in one prescription
- List the SSN of distinct patients who have 'Paracetamol' prescribed to them by a doctor named 'Rakesh Sharma'.
- List the first and last name of patients who have no prescriptions written by doctors other than their primary doctors. **Source:**
- 32341403 / 2021 / IV
- Question 2

6. Map the following E-R Diagram to relational schema... Now, write the CREATE TABLE command for all of the above tables in SQL ensuring that the following concepts are used at least once: integer, string, and date data, NOT NULL constraint, CHECK constraint, PRIMARY KEY constraint, FOREIGN KEY constraints (with ON DELETE SET NULL and ON UPDATE CASCADE constraints, if applicable). _(Note: Requires mapping E-R diagram from source first)_ **Source:**

- 32341403 / 2021 / IV
- Question 3

7. Consider the following SQL statements : (i) CREATE TABLE (ii) SELECT (iii) INSERT (iv) CREATE VIEW (v) DELETE (vi) ALTER TABLE For each of the above commands, indicate whether it is a Data Manipulation Language (DML) command, Data Definition Language (DDL) command, or View Definition Language (VDL) command. **Source:**

- 4095 / 2024 / IV
- Question 1(b)

8. Consider the following relations : Employee(empID: integer, deptID: integer, empSalary: integer, empHobby: char (20)) Department(deptID: integer, deptName: char (20), deptFloor: integer) Which attributes will appear in the output on executing the following SQL queries? (i) SELECT * FROM Employee E NATURAL JOIN Department D; (ii) SELECT * FROM Employee E, Department D WHERE E.deptID = D.deptID; **Source:**

- 4095 / 2024 / IV
- Question 1(c)

9. Consider the following SQL statement : Create table Student (Rollno INT, Name VARCHAR(15), Marks DECIMAL(3,2), Age INT CHECK(Age>=17 and Age <=25), DOB DATE); Which of the following values entered for the columns holds valid? Justify your answer for each case. (i) '14-12-2002' for DOB (ii) 34.75 for Marks (iii) 16 for Age (iv) '21' for RollNo **Source:**

- 4095 / 2024 / IV
- Question 4(b)

10. Consider the following relation schema : Student (sNum: integer, sName: string, major: string, level: string, age: integer) Class (cName: string, room: string, fID: integer) Enrolled (sNum: integer, cName: string) Write SQL statements to perform the following : (i) Find the names of all classes that either meet in room 'R12' or have five or more students enrolled. (ii) For all levels except 'JR', display the level and the average age of students for that level. (iii) Find the names of students not enrolled in any class. **Source:**

- 4095 / 2024 / IV
- Question 4(c)

11. Consider the following relational schema : retiredEmployee (empID, empName, basicSalary, deptName, payGrade) pensionGrade (payGrade, Amount) Show the result for each of the following on the tables : (i) SELECT deptName, COUNT (*), SUM (basicSalary) FROM retiredEmployee GROUP BY deptName; (ii) SELECT empID, empName, deptName FROM retiredEmployee WHERE empName LIKE '_a%'; **Source:**

- 4095 / 2024 / IV
- Question 5(a)

12. Explain the usage of the following clauses in the SQL Query "ON UPDATE CASCADE" and "ON DELETE NULL". **Source:**

- 4803 / 2023 / IV
- Question 1(d)

13. Given the following relations for an EMP_PROJ database : (a) Employee (Emp#, Name, Age, Salary, City, Mobile) Allotted (Project#, Emp#) Project (Project#, Project_Name, Project_Manager) Solve the following Queries on the above-mentioned database using SQL : (i) Get Emp# of employees working on both Project# 353 and Project# 354. (ii) Get details of employees working on all "database" project. (iii) Get Emp# of employees who work on all the projects that Emp # 107 works on. (iv) Insert a tuple <555, "Operation Research", "Jim"> in the Project table. (v) Change the city of an employee from "Delhi" to "Chennai" whose name is "James". **Source:**

- 4803 / 2023 / IV
- Question 5(a)

14. Consider the following database giving information of various branches of a company and staff at each branch : Branch (branchNo, street, city, postcode) Staff (staffNo, fname, lname, position, sex, DOB, salary, branchNo) (a) Give SQL Create Table commands to create the above tables. (b) Answer the following queries in SQL : (i) List the address of all branch offices in London or Bristol. (ii) Find the minimum, maximum and average staff salary. (iii) For each branch office with more than one staff member, find the number of staff working and the sum of their salaries. (iv) Find all staff whose salary is larger than the salary of every staff member at the branch with branchNo 'B003'. **Source:**

- 6514 / 2018 / IV
- Question 3

## Frequency Analysis

- **Most repeated questions:** Writing SQL DML queries (SELECT, INSERT, UPDATE, DELETE) for a provided relational schema is a standard question present in every paper. CREATE TABLE with constraints is also frequently asked.
- **Frequently asked concepts:** SQL JOINs, GROUP BY and HAVING clauses, Aggregate functions, DDL commands (CREATE, ALTER), ON DELETE/UPDATE clauses.
- **Trend analysis across years:** Writing queries to fetch aggregated statistics (using COUNT, SUM, AVG) combined with GROUP BY remains a focal point. Recent questions increasingly test the syntactical correctness and implications of SQL constraints.

---

# Unit 5: Database Design

## Mapping ER to Relational, Functional Dependencies and Normalization

1. In the Restaurant relation given below: Find out which of the following dependencies are violated? Justify your answer. (i) Dish_Desc -> Price (ii) Bill_No -> Qty **Source:**

- 2210 / 2019 / IV
- Question 1(a)

2. Map the following ER diagram to their corresponding relational tables. **Source:**

- 2210 / 2019 / IV
- Question 1(e)

3. Two sets of FDs for a relation R (A, B, C, D, E) are given as follows : F = {A -> B, AB -> C, D -> AC, D -> E} and G = {A -> BC, D -> AE} Find out whether F and G are equivalent. Justify your answer. **Source:**

- 2210 / 2019 / IV
- Question 3(b)

4. Consider the following relation : BOOK (BookID, GenreID, GenreType, Price) Following dependencies hold in the relation : BookID -> GenreID, Price GenreID -> GenreType (i) Find Primary key of the above relation. (ii) Apply normalization to convert it into 3NF stating the reasons behind each decomposition. **Source:**

- 2210 / 2019 / IV
- Question 6(a)

5. Choose suitable attributes for various entities and convert the following ER diagram to relational tables. **Source:**

- 2798 / 2017 / IV
- Question 1(b)

6. Two sets of FDs for a relation R(A, B, C) are given as follows: F = {A -> B, A -> C, C -> A} G = {A -> B, B -> C, A -> C, C -> A} Are F and G equivalent? Justify your answer. **Source:**

- 2798 / 2017 / IV
- Question 1(f)

7. Consider the universal relation R = {A, B, C, D, E, F, G, H, I, J} and the set of functional dependencies F = {{A, B} -> {C}, {B, D} -> {E, F}, {A, D} -> {G, H}, {A} -> {I}, {H} -> {J}}. Find the key of R. Decompose R into 2NF and then 3NF relations. **Source:**

- 2798 / 2017 / IV
- Question 5(a)

8. You are given the following state of the relational scheme R(A, B, C): A B C a1 b1 c1 a2 b1 c2 a3 b2 c3 a4 b3 c2 Indicate which of the following functional dependencies are satisfied by the current state? Justify your answer. (i) B -> C (ii) A -> B **Source:**

- 2798 / 2017 / IV
- Question 5(b)

9. Let F = {A -> B, A -> C, C -> A} for a given relational schema R. Find (BC)+ and (C)+. **Source:**

- 2798 / 2017 / IV
- Question 7(b)

10. Map the following E-R Diagram to relational schema: _(Note: Requires mapping E-R diagram from source)_ **Source:**

- 32341403 / 2021 / IV
- Question 3

11. Given below are two sets of FDs for a relation R (A,B,C,D,E) : F : A -> B, AB -> C, D -> AC, D -> E G : A -> BC, D -> AE Are F and G equivalent? Find the minimal cover for the set of dependencies F. Now, Consider another relation R = {A,B,C,D,E,F,G,H,I,J} with the following set of FDs F = { AB -> C, A -> DE, B -> F, F -> GH, D -> IJ } Find the key. Which highest normal form is this relation in? Why? Decompose it into 2NF and 3NF relations. Is this decomposition dependency preserving? Justify your answer. **Source:**

- 32341403 / 2021 / IV
- Question 4

12. Consider the following Entity Relationship diagram (ERD) for a ternary relationship ProjGuide. Map the given ER diagram to a relation schema. **Source:**

- 4095 / 2024 / IV
- Question 1(a)

13. Consider the relation R = {A, B, C, D, E, F, G, H, I, J} and the set of functional dependencies F ={{A, B} -> {C}, {A} -> {D, E}, {B} -> {F}, {F} -> {G, H}, {D} -> {I, J}}. (i) Find the closure of {A, B}. (ii) Assuming {A, B} as the primary key, does the relation R exhibit partial dependency? Justify your answer. **Source:**

- 4095 / 2024 / IV
- Question 1(j)

14. Consider a relation R(A, B). Is the given relation in BCNF? Why or why not? **Source:**

- 4095 / 2024 / IV
- Question 2(a)

15. Consider the following relation for which {Car#, Salesperson#} is the primary key. Assume that all attributes are simple and atomic. Also, assume that a car may be sold by multiple salespersons. CarSale(Car#, dateSold, Salesperson#, Commission%, DiscountAmt) Additional functional dependencies are : {dateSold -> DiscountAmt}, {Salesperson# -> Commission%} (i) Based on the given primary key, check whether the above schema is in 2NF. Justify your answer. (ii) If required, normalize the given relation up to 3NF. Show all the intermediate steps. **Source:**

- 4095 / 2024 / IV
- Question 2(c)

16. State and prove the Pseudotransitive inference rule. Apply the above rule to infer ONE additional functional dependency for the given set F = {M -> P, MY -> P, YP -> C} **Source:**

- 4095 / 2024 / IV
- Question 3(c)

17. Consider a relation R(A, B, C, D, E) with the following dependencies : {AB -> C, CD -> E, DE -> B} Is AB a candidate key of this relation? Justify your answer. **Source:**

- 4095 / 2024 / IV
- Question 4(a)

18. Consider the following ER diagram to conceptualize a database that can be used to keep track of transport ships and their locations. (i) Map the given ER diagram into a relational schema. (ii) Specify the primary key and foreign keys for each relation. **Source:**

- 4095 / 2024 / IV
- Question 5(b)

19. Consider a relation R with three attributes {A, B, C}. It is decomposed into relations R1 with attributes {A, B} and R2 with attributes {B, C}. State the condition (using relational algebra notation) that should be met for this decomposition to satisfy lossless-join property. **Source:**

- 4095 / 2024 / IV
- Question 6(c)

20. Considering the below given state of R(A, B, C, D) : Which of these FDs may hold on R? Justify your answer. (i) D -> A (ii) BC -> D (iii) BC -> A **Source:**

- 4095 / 2024 / IV
- Question 6(d)

21. When is it necessary to have a surrogate key while mapping EER to a relational database? Justify with an example. **Source:**

- 4803 / 2023 / IV
- Question 1(a)

22. In the relation R (A, B, C, D, E) given below: Which amongst the following dependencies are violated? Justify your answer. (i) B -> C (ii) D -> E **Source:**

- 4803 / 2023 / IV
- Question 1(b)

23. Find out the closure of CD in the following relation R (A, B, C, D, E, F, G) for the given set of functional dependencies F = {A -> BC, E -> C, CD -> AEG, ABG -> BD, DG -> BC} Show the steps to compute the closure for CD. Using the closure, can we say that CD is a candidate key, if yes, Justify. **Source:**

- 4803 / 2023 / IV
- Question 1(e)

24. Consider the relation R, which has attributes to store timetable of courses and sections at a university; R = {Course_no, Sec_no, Offering_dept, Credit_hours, Course_level, Instructor_ssn, Semester, Year, Days_hours, Room_no, No_of_students}. Suppose that the following functional dependencies hold on R : {Course_no} -> {Offering_dept, Credit_hours, Course_level} {Course_no, Sec_no, Semester, Year} -> {Days_hours, Room_no, No_of_students, Instructor_ssn} {Room_no, Days_hours, Semester, Year} -> {Instructor_ssn, Course_no, Sec_no} (i) Identify the Primary key in relation R? (ii) Apply normalization to convert it into 3NF stating the reasons behind each decomposition (assume R is already in 1NF). **Source:**

- 4803 / 2023 / IV
- Question 3(a)

25. Find the minimal cover of Functional dependency set F : {B -> A, D -> A, AB -> D}. **Source:**

- 4803 / 2023 / IV
- Question 3(b)

26. Map the following ER-diagram into a Relational database (Assume appropriate cardinality ratios for each of the given relationships). Here CCI denotes a ternary relationship between candidate, company and interview. **Source:**

- 4803 / 2023 / IV
- Question 4(a)

27. List all the FDs satisfied by the following table **Source:**

- 4803 / 2023 / IV
- Question 5(b)

28. Two sets of FDs for a relation R (A,B,C,D,F) are given as follows : F = { A -> B, AB -> C, D -> AC, D -> E } G = { A -> BC, D -> AE } Are F and G equivalent ? Justify your answer. **Source:**

- 6514 / 2018 / IV
- Question 1(a)

29. Consider the following EER diagram for a vehicle dealer database. Vin (Vehicle Identification) is primary key for the entity VEHICLE and Sid (Salesperson Id) is the primary key for the entity SALESPERSON : Convert the following components of the above EER diagram to relational tables : (i) 1 : N relationship (ii) Specialization. **Source:**

- 6514 / 2018 / IV
- Question 1(b)

30. Consider the universal relation R = {A, B, C, D, E, F, G, H, I, J} and the set of functional dependencies F = {{A, B} -> {C}, {A} -> {D, E}, {B} -> {F}, {F} -> {G, H}, {D} -> {I, J}}. Find the key of R? Decompose R into 2NF and then 3NF relations. **Source:**

- 6514 / 2018 / IV
- Question 5(a)

31. Differentiate between functional dependency and full functional dependency. Give an example of a relation that is in 3NF but not in BCNF giving reasons. **Source:**

- 6514 / 2018 / IV
- Question 5(b)

## Frequency Analysis

- **Most repeated questions:** Equivalence of two sets of FDs (checking if F is equivalent to G) and converting a universal relation R with given FDs to 2NF, 3NF and BCNF are extremely common. Translating an ER diagram to a relational schema is asked in nearly all papers.
- **Frequently asked concepts:** ER to Relational schema mapping, Closure of an attribute set, Finding Candidate Keys, Minimal Cover, 1NF, 2NF, 3NF, BCNF, Dependency Preserving and Lossless join decomposition.
- **Trend analysis across years:** The mechanical process of normalization remains a staple. Recent tests increasingly look at minimal covers, testing for lossless join property, and evaluating whether states of a table violate given functional dependencies.

---

# Unit 6: Data Storage and Indexes

## File Indexing, B+ Trees, Transactions and Concurrency

1. Two transactions T1 and T2 are executing concurrently (assuming concurrency control is not in place) with initial value of X=50 and Y=5 T1 read_item(X) X = X+10 write_item(X) read_item(Y) T2 read item(X) X = X+Y write_item(X) After the completion of the transactions T1 and T2 what will be the value of X. Is this the correct value, if not specify the problem. **Source:**

- 2210 / 2019 / IV
- Question 1(d)

2. Consider an ordered file with number of records r = 30000 stored on a disk with block size B = 1024 bytes and record size = 100 bytes. (i) Find the blocking factor for the file. (ii) The number of blocks needed for the file and (iii) Number of block accesses needed by a binary search on this data file. (iv) How many block accesses would be required if you create a primary index on a key field of size 9 bytes and size of block pointer 6 bytes. **Source:**

- 2210 / 2019 / IV
- Question 6(b)

3. Consider a file with the following key values: 19, 5, 12, 7, 40, 3, 15. Suppose these search key values are inserted in the given order in a B+ tree of order p = 3. Show the tree at each step. **Source:**

- 2210 / 2019 / IV
- Question 7(a)

4. Consider a data file STUDENT (Sid, Sname, CourseNo, Dob, Address). Create the primary index (on Sid) and the secondary index (on CourseNo) on the above file diagrammatically. Which index will take more space and why? **Source:**

- 2798 / 2017 / IV
- Question 1(a)

5. What is the system log used for? **Source:**

- 2798 / 2017 / IV
- Question 1(e)

6. Consider a file with the following key values: 8, 5, 2, 6, 4, 25. Insert these search key values in the given order in a B+ tree of order p = 3 and pleaf = 2. Show the tree at each step. **Source:**

- 2798 / 2017 / IV
- Question 4(a)

7. Consider an ordered file with number of records r = 30000 stored on a disk with block size B = 1024 bytes. A primary index is created on this file where the key is 9 bytes long and the block pointer is 6 bytes long. Find the blocking factor and the number of blocks needed for the primary index. **Source:**

- 2798 / 2017 / IV
- Question 4(b)

8. A file comprising employee records has emp_ID as the primary key. It is searched with the help of B+ tree index with order p = 3 for internal nodes and order pleaf = 2 for leaf nodes.

- If the values of emp_ID are inserted in the following order, show how the tree will expand and how many times the leaf node will split up. 216, 182, 333, 115, 160, 235, 218, 332
- Show the tree after deleting the employees with emp_ID numbers 216, 182 and 333. Show each step.
- What will be the number of block accesses in the above indexing scheme? **Source:**
- 32341403 / 2021 / IV
- Question 5

9. In the given schedule, what is the problem encountered due to concurrent execution of transactions T1 and T2? Assuming the initial value X=5, what will be the value of X after the schedule is executed? Timestamp T1 T2 1 read (X) 2 X=X+10 3 Read (X) 4 X=X+20 5 Write (X) 6 Write (X) 7 Commit 8 Commit **Source:**

- 4095 / 2024 / IV
- Question 1(h)

10. Why can a database allow at most one primary index on a file but several secondary indexes? **Source:**

- 4095 / 2024 / IV
- Question 6(b)

11. How does multilevel indexing improve the efficiency of searching an index file? **Source:**

- 4095 / 2024 / IV
- Question 7(a)

12. Suppose that we have an ordered file with r = 10,000 records stored on a disk. The records are of fixed size and are unspanned. The search key field in each record is V = 9 bytes long. The remaining attributes of the record are 91 bytes in total. The block size for the disk is B = 1024 bytes. Compute the following : (i) record length (R) (ii) blocking factor (bfr) (iii) number of file blocks (b) (iv) number of block accesses required during binary search on the data **Source:**

- 4095 / 2024 / IV
- Question 7(b)

13. Two transactions T1 and T2 are executing concurrently (assuming concurrency control is not in place) with initial value of X=15 and Y=5. T1
14. Read_item(X)
15. X = X+10
16. write_item (X)
17. Read_item(X) T2
18. Read_item(X)
19. X = X+Y
20. write_ item (X) Transaction T1 fails during the execution of statement number 7. After the completion of the transaction T2 what will be the value of X. Is this the correct value, if not, identify the name of the concurrency control problem. **Source:**

- 4803 / 2023 / IV
- Question 1(k)

14. Create a B-tree of order 4 inserting following values in the given order (in steps) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 **Source:**

- 4803 / 2023 / IV
- Question 6(a)

15. Compute the number of blocks of access required to get records from an ordered file with r = 20,000 records stored on a disk with Block size B = 1024 bytes with or without primary index. Also, calculate blocking factor. Assume that file records are of fixed size with record length R = 100 bytes, ordering key field is 9 bytes long and block pointer is 6 bytes long. **Source:**

- 4803 / 2023 / IV
- Question 7(a)

16. What are the four desirable properties of a Transaction that should be enforced by the concurrency control? **Source:**

- 4803 / 2023 / IV
- Question 7(b)

17. Consider a data file EMPLOYEE (EmpId, Ename Salary, DeptNo, Dob, Designation). Create the primary index (on EmpId) and the secondary index (on DeptNo) on the above file diagrammatically. Which index will take more space and why ? **Source:**

- 6514 / 2018 / IV
- Question 1(f)

18. State the ACID properties of transactions. What is the use of system log ? **Source:**

- 6514 / 2018 / IV
- Question 1(g)

19. Consider a file with the following key values : 9, 5, 2, 7, 4, 15. Insert these search key values in the given order in a B+ tree of order p = 3 and pleaf = 2. Show the tree at each step. **Source:**

- 6514 / 2018 / IV
- Question 4(a)

20. Consider an ordered file with number of records r = 30000 stored on a disk with block size B = 1024 bytes. Find the blocking factor for the file, the number of blocks needed for the file and number of block accesses needed by a binary search on this data file. **Source:**

- 6514 / 2018 / IV
- Question 4(b)

## Frequency Analysis

- **Most repeated questions:** Showing step-by-step insertions into a B+ tree of a given order is asked in almost every paper (2017, 2018, 2019, 2021, 2023). Numerical problems calculating record length, blocking factor, total blocks, and number of accesses using binary search and index search is also highly recurrent.
- **Frequently asked concepts:** B+ Trees (insertion, leaf splitting), Indexing computations (Blocking factor, Multi-level indexing logic), Primary vs. Secondary indexing properties, ACID properties, Transaction schedules and concurrency problems (Lost update, Dirty read).
- **Trend analysis across years:** The B+ tree insertion logic and block-factor numericals form the core computational portion of the exam. In recent years, recognizing exact concurrency problems from small transaction schedules has become a persistent testing pattern.
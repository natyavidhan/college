# Unit 1: Introduction to Basic Statistics and Analysis

## Fundamentals of Data Analysis and Types of Data

1. Explain unimodal, bimodal and multimodal distribution with the help of examples.

**Source:**

- 1673 / 2024 / Sem III / Q4(a)
- 2012 / 2023 / Sem II / Q1(a)

2. List and describe different types of sampling of data.

**Source:**

- 6060 / 2024 / Sem II / Q1(b)

3. Define categorical and interval data. Give example of each.

**Source:**

- 6060 / 2024 / Sem II / Q5(a)

4. Classify each field as either qualitative or quantitative, and identify the type of data (Nominal, Ordinal, Interval or Ratio) associated with each. A data analyst is working with a survey dataset that includes fields like gender, age, income, education level, and satisfaction rating.

**Source:**

- 5325 / 2025 / Sem II / Q1(c)

5. Describe the key stages in the data analysis process. For each step, explain its purpose and significance using relevant examples.

**Source:**

- 5325 / 2025 / Sem II / Q2(a)

6. List and describe the steps involved in process of Data Analysis.

**Source:**

- 2012 / 2023 / Sem II / Q3(d)

7. State differences between following by giving appropriate examples: (i) Simple random sampling and Stratified sampling

**Source:**

- 5325 / 2025 / Sem II / Q1(b)(i)

## Correlation and Covariance

1. Define correlation and covariance. Outline the difference between the two.

**Source:**

- 6060 / 2024 / Sem II / Q4(e)

2. What is correlation? How does it help in understanding relationships between two variables? Based on the scatter plots shown below, estimate the type and strength of correlation for each plot (e.g., strong positive, weak negative, no correlation, etc.). Justify your answer.

**Source:**

- 5325 / 2025 / Sem II / Q1(e)

## Python Basics and Built-in Structures

1. Python is a strongly "typed" language. Comment.

**Source:**

- 4432 / 2024 / Sem V / Q1(d)

2. Differentiate between mutable and immutable objects.

**Source:**

- 4432 / 2024 / Sem V / Q1(f)

3. What is the use of generator function? Write a generator function to print square of first n natural numbers where n is user input.

**Source:**

- 1095 / 2022 / Sem V / Q4(a)

4. Write a generator function to print Fibonacci numbers.

**Source:**

- 4432 / 2024 / Sem V / Q4(b)(i)

5. What is the output of the following code :

```
def simpleGeneratorFunc():
    yield 1
    yield 2
x = simpleGeneratorFunc()
print(next(x))
print(next(x))
```

**Source:**

- 4432 / 2024 / Sem V / Q4(b)(ii)

6. Give output of the following code. Justify. (i)

```
val=['foo', 2,]
val = (5, 4)
print(val)
```

(ii)

```
var=(3, 5, (4,5))
var = 'two'
print(var)
```

**Source:**

- 1095 / 2022 / Sem V / Q2(b)

7. Give output of the following code. Justify your answer.

```
var=(1, 2, (3,4))
var='geet'
print(var)
```

**Source:**

- 4432 / 2024 / Sem V / Q5(a)

8. Provide the output of following codes. Given the value of string object `s=3.1456` and `c="""This is a long string that spans multiple lines"""` (i) `fval= float(s); type(fval)` (ii) `bool(s)` (iii) `c.count('\n')`

**Source:**

- 1095 / 2022 / Sem V / Q1(c)

9. Consider a list `seq=`. Write a code to find the sum of elements of the value till element 5.

**Source:**

- 1095 / 2022 / Sem V / Q1(d)

10. What will be the output of the following codes? (ii)

```
List = [str[::-1] for str in ('happy','go','lucky')]
print(List)
```

**Source:**

- 4432 / 2024 / Sem V / Q1(b)(ii)

11. Given the following list of strings `List1 = ['Amazon', 'Amazing Amazon', 'Apple', 'Microsoft', 'Apple is good for health', 'I like Microsoft']` Using 'List1', generate the following dictionary 'Anydict' where key is the count of words in a string and value is the list of strings having that count. `Anydict={1:['Amazon', 'Apple', 'Microsoft'], 2: ['Amazing Amazon'], 3: ['I like Microsoft'], 4: ['Apple is good for health']}`.

**Source:**

- 1095 / 2022 / Sem V / Q3(a)

## Frequency Analysis

- **Most repeated questions:** Definitions and differences between categorical/interval data, correlation vs. covariance, and data distributions (unimodal, bimodal, multimodal).
- **Frequently asked concepts:** Generator functions, mutable vs. immutable objects, and outputs involving basic Python tuple/list assignment restrictions.
- **Trend analysis across years:** There is a distinct shift from asking basic Python programming questions (2022, 2024 Sem V) towards asking conceptual statistics and data lifecycle definitions in the GE papers (2024, 2025 Sem II).

---

# Unit 2: Array manipulation using Numpy

## Creating NumPy arrays and Data Types

1. What is a NumPy ndarray? How does it differ from a Python list? Consider the following code snippet. Predict the output and explain the reason behind the result:

```
import numpy as np
arr = np.arange(10)
sliced = arr[2:6]
sliced[:] = 99
print(arr)
```

**Source:**

- 5325 / 2025 / Sem II / Q1(d)

2. State differences between following by giving appropriate examples: (ii) rand( ), randint( ) functions in NumPy. (iii) Deep and shallow copy in NumPy array.

**Source:**

- 5325 / 2025 / Sem II / Q1(b)(ii-iii)

3. Write Numpy commands to perform the following operations on array num : (i) Create an array num containing values from 31 to 46. (ii) Convert datatype of array num to floating type data. (iii) Reshape array num to an array of size 4x4. (iv) Replace the diagonal elements of array num to 0. (v) To create an array of 1's with the same shape and type as the given array num.

**Source:**

- 6060 / 2024 / Sem II / Q7(a)

4. Create an array `num` of size 2x3 filled with all zeros then insert `[,]` into array. Identify the shape of the array `num`.

**Source:**

- 1095 / 2022 / Sem V / Q1(g)

5. Consider the given numpy array mat: `mat = np.array([[[-1,2],], [[-5,6],]])` Write numpy commands to perform the following operations: (i) Create an array of zeros with the same shape as mat. (ii) Print the shape of the mat. (iii) Print the datatype of the elements in mat. (iv) Print the elements which are greater than 6 in mat. (v) Convert all the elements in mat as float type. (vi) Multiply each element in mat with 25.

**Source:**

- 2012 / 2023 / Sem II / Q3(c)

6. Construct a NumPy array, `markSheet`, to store marks obtained by 2 students in 3 subjects, where marks are between 60 and 100. Write Python statements to display the data type, shape and dimension of `markSheet`.

**Source:**

- 1673 / 2024 / Sem III / Q3(b)

## Indexing, Slicing, and Array Operations

1. Consider the following numpy arrays : `arr1 = np.array([,])` `arr2 = np.array([,,])` Give the output of the following commands : (i) arr2 (ii) arr1 [: 2, -1] (iii) arr1 * 3 (iv) arr1 > 5 (v) arr2 = 4

**Source:**

- 6060 / 2024 / Sem II / Q1(a)

2. Give the output of the following code segment:

```
arr = np.array()
arr1 = arr[5:9]
arr2 = arr[5:9].copy()
arr1 = 36
arr2 = 7
print(arr)
print(arr1)
print(arr2)
```

**Source:**

- 2012 / 2023 / Sem II / Q1(b)

3. Write numpy commands to retrieve following elements from `arr`:

```
arr = [,
       ,
       ,
       ,
       ,
        ]
```

(i) (1, 4), (3, 1), (5, 0), and (2, 3) (ii) Retrieve 0, 2, 4 rows (use positive index) (iii) Retrieve 1, 3, 5 rows (use negative index) (iv) Retrieve values greater than 10 (v) Retrieve rows 1 to 4.

**Source:**

- 6060 / 2024 / Sem II / Q6(c)

4. Write a Python program using NumPy to perform the following tasks: (i) Create a 3x4 NumPy array containing random integers between 10 and 50. (ii) Slice and display the first two rows of the array. (iii) Replace the last column of the array with zeros. (iv) Transpose the modified array and display its shape. (v) Compute and display the mean and standard deviation along each column of the original (modified) array. (vi) Explain the use of the following ndarray attributes with suitable Python code examples: `.shape`, `.ndim` and `.dtype`

**Source:**

- 5325 / 2025 / Sem II / Q4

5. Consider the following numpy array matrix :

```
[,
,
,
]
```

Give the output of the following numpy commands : (i) matrix.T (ii) matrix[:1,1:] (iii) matrix[,] (iv) matrix[[-2,-4]] (v) matrix[[True, False, False, True]] (vi) matrix [:2] (vii) matrix[::-1] (viii) matrix.ndim (ix) np.swapaxes(matrix, 1, 0) (x) matrix+10

**Source:**

- 2012 / 2023 / Sem II / Q3(a)

6. Give the output of the following code snippets: (i)

```
y=np.arange(12).reshape(4,3)
print(y)
y[(y > 5)] = -1
print(y)
```

(ii)

```
x = np.array ([,])
z=np.ones_like(x)
print(z)
w=np.eye(2) * x
print(w)
```

**Source:**

- 2012 / 2023 / Sem II / Q3(e)

7. Find the output that will be produced on the execution of the following code snippet :

```
c1 = np.arange(0, 24, 2)
c2 = c1.reshape((2, 6))
print(c1, c2, sep = '\n')
print(c2.reshape((3,4)))
arr2[3, 3:] = 0
print(c2)
print(c1 * 2)
```

**Source:**

- 1673 / 2024 / Sem III / Q1(d)

8. Consider a NumPy array, `empSalary`, containing salary of 10 employees. Write Python statements to do the following : (i) Find total number of employees earning salary > 5000. (ii) Create a new array, `incentive`, to store incentives given to each employee where incentive is 10% of the salary.

**Source:**

- 1673 / 2024 / Sem III / Q1(e)

9. Find the output on the execution of the following code snippet :

```
b1 = np.arange(6)
b2 = np.array([,])
print('i.\n', b1)
print('ii.\n', b2)
print('iii.\n', 2/b2)
print('iv.\n', b1, b2)
print('v.\n', b1[:1], b2[::2])
```

**Source:**

- 1673 / 2024 / Sem III / Q3(b) _(note: explicitly labeled b inside paper but directly follows a question 3a)_

10. What will be the output of the following codes? (i)

```
import numpy as np
arr = np.array([,])
print(arr[1,-1], arr[-1:])
```

**Source:**

- 4432 / 2024 / Sem V / Q1(b)(i)

11. Reshape the following array to dimension (2,6) `[,,]`

**Source:**

- 4432 / 2024 / Sem V / Q1(c)

12. Give output of the following code.

```
matrix =[[j for j in range(3)]for i in range(3)]
print(matrix)
```

**Source:**

- 1095 / 2022 / Sem V / Q1(a)(ii)

13. Consider the given `arr =`. What will be the resulting array if these operations are performed `arr[2:5]`, `arr[-5: -1]` and `arr[::-2]`.

**Source:**

- 1095 / 2022 / Sem V / Q1(e)

14. Write a numpy code to create a 3D array a3 of size 4 x 5 x 3 of random numbers in range 1 to 60 and swap axis 1 with axis 2. Identify the number of matrices in the array a3, dimension of a matrix in array a3 and the datatype of array a3.

**Source:**

- 6060 / 2024 / Sem II / Q3(b)

## Frequency Analysis

- **Most repeated questions:** Predicting outputs for complex array indexing (boolean masks, multi-dimensional slicing, negative indexing). Reshaping an array and transposing.
- **Frequently asked concepts:** Array views vs copies (especially what happens when modifying a slice), `arange`, `reshape`, `ones_like`, `eye`, broadcasting, and dimensional attributes (`.shape`, `.ndim`, `.dtype`).
- **Trend analysis across years:** Over the years, creating large matrices and fetching highly specific overlapping subsets (`matrix[,]`) has become standard. Checking the difference between view and copy using NumPy lists slice assignment is tested explicitly.

---

# Unit 3: Data Manipulation using Pandas

## Series, Data Frame, Index objects & Loading Data

1. Consider the series `a` given below and write commands to perform the following operations : `a= pd.Series([6,np.nan,-4,np.nan,3,8,np.nan,5])` (i) Sort the values and keep NaN in initial positions. (ii) Assign rank in descending order. (iii) Retrieve all values except NaN.

**Source:**

- 6060 / 2024 / Sem II / Q6(c)

2. Consider the Series object Company having `Company_Name` as index and Profit (in Crores) as values:

```
Company_Name   Profit
TCS            350
Reliance       200
L&T            800
Wipro          150
```

Write the python commands to perform the following operations: (i) To display the Company_Name having profit > 250. (ii) To display the index. (iii) To assign name 'Company_Name' to index.

**Source:**

- 6060 / 2024 / Sem II / Q1(c)

3. Consider the series `a` given below and give the output of the following commands: `a = pd.Series()` (i) `a.rank()` (ii) `a.rank(method='first')` (iii) `a.rank(ascending=False)`

**Source:**

- 2012 / 2023 / Sem II / Q1(c)

4. Create a Pandas DataFrame that holds employee data with the columns : Name, Age, and Salary, including some missing values. Then, perform the following actions : (i) Drop all rows that contain missing values. (ii) Filter and display the employee records where the Salary is greater than ₹50,000.

**Source:**

- 5325 / 2025 / Sem II / Q1(f)

5. Consider the dataframe `Score` given below :

```
Name  Class  Score1  Score2  Score3
A     1      85      90      88
B     2      74      86      80
C     1      83      71      92
D     2      64      68      73
E     2      77      62      72
F     1      90      87      92
```

Give the output of following commands : (i) `Score[['Name', 'Class']]` (ii) `Score[Score['Class'] ==1] ['Name']` (iii) `Score[Score['Score3'] < 80]` (iv) `Score['Class'].value_counts().sort_index()` (v) `Score.sum(axis="columns")` Write a function `diff` to compute the difference between the maximum and minimum of each column of dataframe Score and apply it to dataframe Score.

**Source:**

- 6060 / 2024 / Sem II / Q7(b)

6. Consider the series `S1` and `S2` given below:

```
  S1     S2
A 1    A 5
B 2    B 6
C 3    D 7
D 4    E 8
```

Give the output of the following python pandas commands : (i) `S1 [ : 3] * 10` (ii) `S1 + S2` (iii) `S2 [ : :-1] * 5`

**Source:**

- 2012 / 2023 / Sem II / Q1(f)

7. Write code to read each row of a given csv file. Skip the header of the file while reading. Also print the number of rows and the field names.

**Source:**

- 4432 / 2024 / Sem V / Q3(a)

8. Write a code to read a CSV file with new delimiter as ';' and line terminator as '\n'.

**Source:**

- 1095 / 2022 / Sem V / Q1(h)

9. Write a code to read the data from a csv file. Find the number of rows and columns in the data, replace missing values with zero, and remove duplicate values. Write the modified data back to the original file.

**Source:**

- 1095 / 2022 / Sem V / Q3(b)

10. Give the python commands to create a dictionary with 5 keys - 'A', 'B', 'C', 'D', 'E' and value as follows. Key A: List of numbers from 1 to 10 skipping 2 at a time. Key B: List of Strings from A to E. Key C: List of 5 numbers obtained using random normal distribution function. Key D: List of 5 random integers from 20 to 30. Key E: Square root of 5 random numbers from 50 to 70. Give python commands to perform the following operations : (i) Create DataFrame data using the above dictionary. (ii) Convert Column A to index. (iii) Rename the rest of the columns as Area, Temperature, Latitude and Longitude.

**Source:**

- 2012 / 2023 / Sem II / Q5(a)

11. Consider the DataFrame `Frame` given below :

```
Name    Age  Weight  Height
Ram     15   45.6    140
Ravi    23   34.9    160
Reena   32   45.6    145
Rita    20   60.7    155
Rishi   33   54.7    170
Romi    21   34.6    144
```

Write python commands to perform the following operations: (i) Compute the correlation of Age with both Weight and Height. (ii) Sort Frame in descending order of Age. (iii) To find the index for the row with minimum Age. (iv) Calculate cumulative sum for Weight for all Students. (v) To set height of 'Rita' and 'Romi' to NA. (vi) Replace the value 32 with 18 and 33 with 19 in Age column. (vii) Define map function to convert values of Name column to upper case.

**Source:**

- 2012 / 2023 / Sem II / Q2(a)

12. Consider the following dataset `student`.

```
Year Name   Roll No Marks Age
1    Rani   23      70    18
2    Rita   24      75    20
3    Raj    25      80    22
1    Rahul  26      65    25
2    Rohit  27      80    28
```

Give the output of the following python commands: (i) `student [['Roll No ', ' Name ']] [2 : 4]` (ii) `student [student ['Age'] >20]` (iii) `student [student ['Age'] >20] ['Name']` (iv) `avg_marks = np.mean (student.Marks); student[student['Marks']>avg_marks]` (v) `first = student [student ['Year'] ==1]['Marks']; np.mean(first)`

**Source:**

- 2012 / 2023 / Sem II / Q6(a)

## Data Wrangling (Missing Data, Reindexing, Merging, Hierarchical Indexing)

1. What is data wrangling? Identify the possible issues that can arise in data wrangling process?

**Source:**

- 6060 / 2024 / Sem II / Q4(a)

2. Consider a csv file `test.csv` having 3 columns and 50 rows. Write python command to perform following operations: (i) Read the file test.csv into a DataFrame data. (ii) Print the first 10 rows of data. (iii) Display the 5 summary statistics for each column of data. (iv) Remove the rows with all null values. (v) Identify duplicate values in data.

**Source:**

- 6060 / 2024 / Sem II / Q4(b)

3. Consider the DataFrame data given below.

```
One Two Three Four Five
1   14  34    NaN  NaN
34  21  NaN   12   NaN
NaN 23  NaN   2    NaN
34  21  32    33   NaN
```

Write python commands to perform the following operations: (i) Drop columns with any null values. (ii) Replace the null values with the mean of each column. (iii) Drop the null values where there are at least 2 null values in a row. (iv) Replace all null values by the last known valid observation.

**Source:**

- 2012 / 2023 / Sem II / Q4(a)

4. Given the following dataframe, provide the output for the following commands: `ord_no, purch_amt, ord_date, customer_id` (contains mixed NaN values) (i) `df.dropna(thresh=2)` (ii) `df.dropna(how='all')` (iii) `df.dropna(how='all', axis=1)` (iv) `df.isnull()` (v) `df.isnull().values.any()`

**Source:**

- 4432 / 2024 / Sem V / Q2(c)

5. Consider the following dataframe `df` containing data of students admitted in the college.

```
Id  Name  Age Section City   Gender Marks
S0  Anit  10  A       Gurgaon M      60
...
```

(i) Find all the rows where Age is greater than or equal to 12 and the Gender is male. (ii) If Age is greater than 20, then use the loc function to update Section with "S" and City with Pune. (iii) Select rows 1 to 2 with columns 2 to 3 using iloc.

**Source:**

- 4432 / 2024 / Sem V / Q1(k)

6. Explain what hierarchical indexing is in pandas. How do you create and access data using hierarchical indexing?

**Source:**

- 5325 / 2025 / Sem II / Q3(a)

7. What is hierarchical Indexing? Why do we use hierarchical indexing in pandas? Which pandas feature enables you to have multiple index levels on an axis? Give an example of hierarchical indexing.

**Source:**

- 6060 / 2024 / Sem II / Q5(b)

8. Consider dataframe `df` given below :

```
Number State One Two Three
       Ohio  0   1   2
       Colorado 3 4  5
```

Provide the output of following commands. (i) `df.stack()` (ii) `df.unstack(level=0)`

**Source:**

- 6060 / 2024 / Sem II / Q6(b)

9. Consider the DataFrame `df` given below:

```
EmployeeID Department Salary Age
1001       English    1000   23
...
```

Write the python code to perform the following operations: (i) Create a hierarchical index on Department and Employee ID. (ii) Give the summary level statistics for each column. (iii) Give the output for the following:

1. `df.stack()`
2. `df.unstack()`

**Source:**

- 2012 / 2023 / Sem II / Q7(a)

10. Give the output of the following code :

```
import Pandas as pd
s1 = pd.Series(['Certificate', 'Bachelor', 'Master', 'Doctorate'],index =)
s1.reindex(range(10), method = 'ffill')
print(s1)
```

**Source:**

- 6060 / 2024 / Sem II / Q4(g)

11. Differentiate between `ffill` and `bfill`. Provide the output of the given code:

```
import pandas as pd
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=)
print(obj3.reindex(range(6), method='ffill'))
print(obj3.reindex(range(6), method='bfill'))
```

**Source:**

- 4432 / 2024 / Sem V / Q3(b)

12. Give output of the following code. (i)

```
import pandas as pd
obj3 = pd.Series(['wow', 'good', 'great'], index=)
obj3.reindex(range(6), method='ffill')
```

**Source:**

- 1095 / 2022 / Sem V / Q1(a)(i)

13. Differentiate `pandas.merge` and `pandas.concat`.

**Source:**

- 4432 / 2024 / Sem V / Q2(a)(ii)

14. Write the code to merge the two given datasets `data1` and `data2` using key1, key2.

**Source:**

- 4432 / 2024 / Sem V / Q5(b)

15. Consider the following piece of code and give the output:

```
import pandas as pd
df1 = pd.DataFrame({'id' :, 'val' : ['a', 'b', 'c', 'd']})
df2 = pd.DataFrame({'id' :, 'val' : ['p', 'q', 'r', 's', 't', 'u']})
df3 = pd.merge(df1, df2, on= 'id', how= 'outer')
print(df3)
```

How many NaN values are there in the data frame df3? Write pandas command to replace NaN with the last known valid value in df3.

**Source:**

- 6060 / 2024 / Sem II / Q2(c)

16. Consider the DataFrames `First` and `Second` given below:

```
First (One, Two)
Second (One, Two)
```

Consider the following python code segment: `right = pd.merge(first, second, how='right', on='One')` `left = pd.merge(first, second, how='inner', on='Two')` Show the content of the new DataFrames right and left.

**Source:**

- 2012 / 2023 / Sem II / Q1(b) _(note: first question 1b in paper)_

17. Find the output that will be produced on the execution of the following code snippet :

```
data = pd.DataFrame(, [np.NaN, 8, 10], [np.NaN, 12, np.NaN], [np.NaN, np.NaN, np.NaN])
print(data)
print(data.dropna(thresh = 2))
print(data.fillna(method = 'ffill', limit = 2))
```

**Source:**

- 1673 / 2024 / Sem III / Q1(f)

18. Find the output that will be produced on the execution of the following code snippet:

```
df1=pd.DataFrame({'A':, 'B':})
df2 = pd.DataFrame({'A':})
print(df1)
print(df2)
df2['A'] = df1['A'] + 10
print(df2)
print(df2 > df1['B'].min())
```

**Source:**

- 1673 / 2024 / Sem III / Q6(a)(iii)

19. Consider dataframe `df 2` given below :

```
Name Age
0 Rohit 10
1 Amit 13
2 Ankur 12
```

Write python commands to perform following operations: (i) Create a new object df 3 by reindexing df 2 row index as and column index as ['x', 'y']. (ii) Delete the entry of 'Amit' from df3. (iii) Rename index of df 2 as. (iv) Check if the entry 'Rohit' exists in df 2. (v) Modify Age of 'Ankur' to 15 usings loc command.

**Source:**

- 6060 / 2024 / Sem II / Q5(c)

20. Consider the following code :

```
import pandas as pd
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval':})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval':})
```

Provide output of the following : (i) `pd.merge(left, right, on=['key1'])` (ii) `prop_cumsum=left.sort_values(by='key2', ascending=False).lval.cumsum(); print(prop_cumsum)` (iii) `left.append(right)`

**Source:**

- 1095 / 2022 / Sem V / Q6(a)

## Discretization and Binning

1. Differentiate between `qcut` and `cut` methods.

**Source:**

- 4432 / 2024 / Sem V / Q2(a)(i)

2. Consider the following list l1. `l1 =` Discretise the l1 into 4 bins using cut() and qcut(). Give the names ['first', 'second', 'third', 'fourth'] to the bins. What type of object is returned by the pandas after binning? What output is generated by attributes codes and categories of binning object?

**Source:**

- 2012 / 2023 / Sem II / Q2(b)

3. Consider the following numeric grades (out of 4). Formulate bins for the given grades as per the following condition :

```
Below 2.5: Very bad
Between 2.5 to 3: Bad
Between 3 to 3.25: Average
Between 3.25 to 3.5: Good
Between 3.5 to 3.75: Very good
Between 3.75 to 4: Excellent
```

**Source:**

- 4432 / 2024 / Sem V / Q2(b)

4. Write python code to create a numpy array a1 containing 50 floating points values in the range 0 to 1. Put the data of numpy array a1 into 5 bins. Set the precision to 4. Assign names to bins as ['Small', 'Medium', 'Large', 'x-Large', 'xx-Large'].

**Source:**

- 6060 / 2024 / Sem II / Q3(a)

5. Consider an array, `ages`, consisting of age of 12 people ``. Using appropriate libraries, write code to : (i) Create four bins of the array ages, using right side closed intervals `(18-25], (25-35], (35-60], (60-100]`. Name the categories as 'Youth', 'YoungAdult', 'MiddleAged' and 'Senior' respectively. Display the number of values in each category. (ii) Create four equal-sized categories of the array ages.

**Source:**

- 1673 / 2024 / Sem III / Q6(b)

6. Consider the data array = `[0.9296, 0.3164, 0.1839, 0.2046, 0.5677, 0.5955, 0.9645, 0.6532, 0.7489, 0.6536]` of 10 floating-point values. Write code for following : (i) Create 5 bins of the array using the cut method. (ii) Create 5 bins of the array using the qcut method. (iii) Create 5 bins of the array with precision = 2 using cut method. Also explain the usage of parameter precision.

**Source:**

- 1095 / 2022 / Sem V / Q5(b)

7. What is the output of following code :

```
import pandas as pd
data =
bins =
output = pd.cut(data, bins)
print(output)
```

**Source:**

- 5325 / 2025 / Sem II / Q3(b)(iii)

## Frequency Analysis

- **Most repeated questions:** Difference between `cut` and `qcut` functions. `ffill` vs `bfill`. `drop_duplicates` and `dropna` behavior with limits/thresholds. Database style joins via `pd.merge` vs `pd.concat`.
- **Frequently asked concepts:** The role of the `axis` parameter in aggregate operations (`.sum(axis='columns')` vs `.sum(axis=0)`). `stack()` and `unstack()` for multi-index operations.
- **Trend analysis across years:** Consistently heavy emphasis on replacing `NaN` via various functions. Extensive use of filtering datasets dynamically (`Score[Score['Score3'] < 80]`). Recent Generic Elective (GE) papers present simple dictionary-to-dataframe instantiations.

---

# Unit 4: Plotting and Visualization

## Matplotlib

1. What is the purpose of using Matplotlib in Python? Describe briefly any three types of plots that can be created using Matplotlib.

**Source:**

- 5325 / 2025 / Sem II / Q1(a)

2. Find the output of the following Python code. Illustrate the shapes along with their dimensions and colour that will be displayed on the plot.

```
import matplotlib.pyplot as pit
import matplotlib.patches as patches
fig, ax = plt.subplots()
rectangle = patches.Rectangle((0.1, 0.1), 0.3, 0.4, linewidth=2, edgecolor = 'blue', facecolor='lightblue')
ax.add_patch(rectangle)
circle = patches.Circle((0.7, 0.7), 0.2,linewidth=2, edgecolor='green', facecolor='lightgreen')
ax.add_patch(circle)
triangle = patches.Polygon([(0.5, 0.1), (0.9, 0.5), (0.1, 0.5)], closed=True, linewidth=2, edgecolor='red', facecolor='lightcoral')
ax.add_patch(triangle)
ax.set_aspect('equal', 'box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```

**Source:**

- 5325 / 2025 / Sem II / Q7(a)

3. Write a Python program to plot a quadratic function `y = x^2 - 4x + 3` using Numpy and Matplotlib. (i) Generate a list of integer values from -10 to 10 using a suitable NumPy function. (ii) Compute the corresponding values of the function. (iii) Plot the function using a blue dotted line. (iv) Add suitable labels for the X and Y axes and a meaningful title. (v) Display the plot.

**Source:**

- 5325 / 2025 / Sem II / Q5(a)

4. Write python commands to create a figure object using matplotlib. The Figure object has one subplot that contains 3 line graphs. Define legend and chart title of the graph. Define a different style and colour for each line in the subplot. Import appropriate libraries.

**Source:**

- 2012 / 2023 / Sem II / Q3(c)

5. Refer to the DataFrame `Frame` given in question 2 (a), Write a python program to perform the following operations in the given dataset with columns Name, Age, Weight, Height. (i) Create a figure and include 2 subplots in it. (ii) In the first subplot create a scatter plot between two variables Age and Height. (iii) In the second subplot draw a horizontal bar plot between Name and Weight. (iv) Set the title for the figure as 'Data Analysis'. (v) Give appropriate labels for x and y axis. (vi) Save the figure to file with name 'analysis.png'.

**Source:**

- 2012 / 2023 / Sem II / Q6(b)

6. Write a python code to create a figure and a subplot using matplotlib functions. Plot a rectangle of size 3.5 x 8.5 at point (2.0, 7.0), a circle of radius 2.5 at point (7.0, 2.0) as patches in the subplot, functions for plotting. Set the colour of rectangle as 'Green' and color of circle as 'Blue'. Set the x-scale and y-scale to 1-10. Import appropriate libraries.

**Source:**

- 2012 / 2023 / Sem II / Q5(b)

7. Create a figure and add two subplots in it. In the first subplot, create a scatter plot between Salary and Age. Give labels to the x-axis as Salary and the y-axis as Age. Also, give a title to this plot. Discretize Salary into 3 equal bins. In the second subplot, draw a figure to visualize the count of the number of employees in each of these bins. Save the plotted figure to a file named 'Employees.png'.

**Source:**

- 1673 / 2024 / Sem III / Q5(b)(ii-iii)

## Plotting functions in Pandas

1. You are given Sales Data as following :

```
import pandas as pd
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 'Sales_A':, 'Sales_B':}
df = pd.DataFrame(data)
```

From above dataset containing monthly sales data for two products — Product A and Product B, write the code for the following : (i) Create a line plot showing monthly sales of both products on the same chart. (ii) Add labels for the x-axis (Month) and y-axis (Sales). (iii) Add a legend to distinguish between Product A and Product B. (iv) Create a bar chart to compare total sales for each product across the 6-month period. (v) Add a title to each plot and display them clearly.

**Source:**

- 5325 / 2025 / Sem II / Q3(b)

2. Consider the pandas series `s2 = pd.Series()`. Write python code to plot cumulative sum of s2. Set the x limit to and y limit to. Set the style of line graph to dot(.) pattern and marker to star shape. Set appropriate values for xticks and yticks.

**Source:**

- 6060 / 2024 / Sem II / Q6(a)

3. Write a python code to draw a scatter plot comparing monthly revenue (in Crores) and monthly expenditure (in Crores) of a company for year 2021. `revenue =` `expenditure =` Import necessary libraries. Assign the title of the plot as 'Revenue vs Expenditure' and label y-axis as 'Expenditure'. Assign red color to 'Expenditure' data points and green color to 'Revenue' data points.

**Source:**

- 6060 / 2024 / Sem II / Q1(d)

4. Refer to DataFrame `House_Rent` given in question 2(a), Write a python code to plot a bar plot displaying no of Furnished, Unfurnished, Semi-Furnished houses. Import appropriate libraries. The title of graph should be "House Data". Give appropriate labels for x and y axis. Save the figure with name "house.jpg".

**Source:**

- 6060 / 2024 / Sem II / Q2(b)

5. Given rainfall = captured for 5 days of a month, days =. Write code in Python to plot a line with days and rainfall as x and y axis respectively. Mark each point with a red circle of size 20. Add a title to the graph. (Make use of appropriate libraries.)

**Source:**

- 1673 / 2024 / Sem III / Q1(a)

6. Give the output for `df.plot.bar()`.

```
import pandas as pd
df=pd.DataFrame([,,],index=['one','two','three','four'], columns=pd.Index(['A','B','C'],name='MyPlot'))
```

**Source:**

- 1095 / 2022 / Sem V / Q1(a)(iii)

7. Write a code program to draw a scatter plot comparing marks of `Mathematics=` and `Science =` subjects. Import the necessary libraries. Title the plot as 'Marks Comparison' and label y-axis as 'Marks Scored'. Assign red color to mathematics marks points and blue color to science marks points.

**Source:**

- 1095 / 2022 / Sem V / Q4(b)

8. Consider the following dataframe, `company`, showing details of sales done by salespersons in two quarters: (person, sales, quarter, country) Draw a boxplot of the sales.

**Source:**

- 1673 / 2024 / Sem III / Q4(b)(v)

9. Compare the highest and lowest salary for each gender using bar plot. (Context: read from `employee.csv`).

**Source:**

- 1673 / 2024 / Sem III / Q7(d)

10. Plot the heatmap of columns `Hours_studied` and `Marks_obtained` of the dataframe `Student`.

**Source:**

- 1673 / 2024 / Sem III / Q3(a)(iv)

## Frequency Analysis

- **Most repeated questions:** Drawing `scatter` plots with strict color formatting arrays mapped to different data features, and setting up plots with `plt.subplots`.
- **Frequently asked concepts:** Use of `patches` (`Rectangle`, `Circle`, `Polygon`). Axis limits (`xlim`, `ylim`), axis labels (`xlabel`, `ylabel`), saving plots (`savefig`).
- **Trend analysis across years:** The exams generally require writing long, complete functions incorporating matplotlib objects, specifically multiple subplots in a figure (`ax1 = fig.add_subplot...`). Also, direct Pandas plotting via `df.plot.bar()` and `df.plot()` is often mixed with Matplotlib customization requests.

---

# Data Aggregation and Group operations

## Group by Mechanics and Data Aggregation

1. Write Python code to answer the following (Make use of appropriate libraries): (i) Group the data on the column `ord_date` and calculate the total purchase amount `purch_amt` year wise and month wise. (ii) Group the data on the column `customer_Id` and create a list of order date `ord_date` for each group. (iii) Group on the columns `customer_id`, `salesman_id` and then sort sum of `purch_amt` within the groups.

**Source:**

- 4432 / 2024 / Sem V / Q4(a)

2. Write the code to split the given dataset into groups based on `customer_id` and create a list of order date `ord_date` for each group.

**Source:**

- 4432 / 2024 / Sem V / Q5(c)

3. Consider a dataframe `df` as

```
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
```

Provide the output for the following: (i) `print(df)` (ii) `m1 = df['data1'].groupby([df['key1'], df['key2']]).mean(); print(m1)` (iii) `m2 = df['data1'].groupby([df['key1']]).mean()` (iv) `pieces = dict(list(df.groupby('key1'))); pieces['b']` (v) `for(k1,k2),group in df.groupby(['key1','key2']): print ((k1, k2)); print(group)`

**Source:**

- 1095 / 2022 / Sem V / Q2(a)

4. Consider dataframe `df Student`, consisting of student details: `Name, Hours_studied, Marks_obtained`. Write Python code to answer the following: (i) Find names of students who got maximum marks. (ii) Find the average number of hours studied by the students.

**Source:**

- 1673 / 2024 / Sem III / Q3(a)

5. Consider the following dataframe `House_Rent` given below. (i) Find the index of house with maximum rent. (ii) Sort the dataframe House_Rent on "Area". (iii) Calculate total Area and total rent. (iv) Compute the count of houses having rooms 1, 2, 3 etc.

**Source:**

- 6060 / 2024 / Sem II / Q2(a)

6. Read the data from the given CSV file `employee.csv` into a dataframe `empData`. (b) Calculate and display the total salary for each role. (c) Display the total number of females along with their average salary.

**Source:**

- 1673 / 2024 / Sem III / Q7(b-c)

## Pivot Tables and Cross Tabulation

1. You are given the following dataset of student enrollments in various online courses: `student_id`, `course`, `gender`, `day`, `device`, `score`, `attempts` (iv) Using `pd.crosstab()`, display a frequency table showing the count of students for each course and device combination. Add totals using margins=True.

**Source:**

- 5325 / 2025 / Sem II / Q7(b)(iv)

2. Using Pandas `pivot_table()` method: (a) Display the average `score_pct` and average `attempts` (b) Use `gender` and `day` as row indices and `device` as columns (c) Use margins = True to include row and column totals (d) Round the result to 2 decimal places

**Source:**

- 5325 / 2025 / Sem II / Q7(b)(iii)

3. What is a pivot table? Give one example.

**Source:**

- 1095 / 2022 / Sem V / Q1(b)

4. Set the first column 'Id' as the row index of the given dataframe `df`. Create a pivot table of `df` to display the total number of admissions as per 'Section' and 'Gender'.

**Source:**

- 4432 / 2024 / Sem V / Q1(i)

## Time Series

1. Provide code to create a time-series with two index labels - 2011/9/01 and 2011/9/02. Assign random values.

**Source:**

- 4432 / 2024 / Sem V / Q1(a)

2. Identify the need to resample Timeseries data.

**Source:**

- 4432 / 2024 / Sem V / Q6(b)

3. Create a Timeseries Dataframe with date range 01-02-2022 to 30-02-2022 with 1 min frequency interval. The dataframe has two columns populated with random values.

**Source:**

- 4432 / 2024 / Sem V / Q6(a)

4. Consider the following dataset. `Datetime`, `value1`, `value2`, `value3` (i) Resample for 10min with sum function for value1, mean for value2 and max for value 3. (ii) Downsample data to 30s.

**Source:**

- 4432 / 2024 / Sem V / Q6(c)

5. Generate DatetimeIndex of length 20 where each index will be Tuesday of the third week of a month starting from 10-Jan-2022.

**Source:**

- 1095 / 2022 / Sem V / Q1(j)

6. Consider the code given below:

```
import pandas as pd
from datetime import datetime
dates = [datetime(2011,1,2),datetime(2011,1,5), datetime(2011,1,7),datetime(2011,1,8), datetime(2011,1,10),datetime(2011,1,12)]
ts = pd.Series(np.random.randn(6), index=dates)
```

Provide output for the following code: (i) `print (ts)` (ii) `print(ts + ts[::-1])` (iii) `print (ts.index)`

**Source:**

- 1095 / 2022 / Sem V / Q7(a)

7. Write a code to convert string of date '2022-10-20' to string of date '20/10/2022'.

**Source:**

- 1095 / 2022 / Sem V / Q7(b)

8. Provide output of the following code:

```
rng=pd.date_range('2010-01-01',periods=12,freq='T')
ts= pd.Series(np.arange(12), indexing=rng)
print(ts)
print(ts.resample('5min', closed= 'right').sum())
print(ts.resample('5min', closed= 'right', label='right', loffset= '-1s').sum())
print(ts.resample('5min').ohlc())
```

**Source:**

- 1095 / 2022 / Sem V / Q7(c)

## Frequency Analysis

- **Most repeated questions:** Producing cross-tabulations (`pd.crosstab()`) and pivot tables with row margins. Resampling TimeSeries specifically involving offset shifting and aggregate functions.
- **Frequently asked concepts:** `groupby` operations with multiple keys, creating dynamic `DatetimeIndex` items, extracting specific group values iteratively (e.g. converting groupby objects to dicts), `margins=True`.
- **Trend analysis across years:** The concept of `pivot_tables` is heavily tested in the recent 2025 examination. Working with `DatetimeIndex` specifically to test offset strings (`'T'`, `5min`) was prominent in the 2022 and 2024 (Sem V) tests but is omitted heavily in Generic Elective papers for lower semesters.
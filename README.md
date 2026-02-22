## There are two main database types, like the core ones, and those are:

-- Relational Databases (RDBMS)
. There short defination is they store data in the structured tables like in the form of the (rows, columns).
-- Non-Relational Databases (NoSQL Databases)
. There short defination is they store unstructured or the semi-structured data, like the database documents -> which are like
the JSON documents(MongoDB, etc).

. But main thing is in Django mainly relational databases are used, so understanding them is important.


## What is Database?
. A database is like a structured system which is used for storing, managing, and retrieving the data efficiently.
. In Django the relational databases like the,
 - PostgreSQL
 - MySQL
 - SQLite (which is provided as a built in one for the use).
 One point here these all store the data in the tables.


 ## Tables, Rows. Columns:
1. Tables (relations)
A table is the fundamental component which are used for storing the related data.
Example:  A database can contain the multiple tables, and the each table has a unique name being used for the specific purpose.

2. Columns (fields/attributes)
The columns are the vertical elements in a table that show the structure of the data.
Example: in a Users table for example, the user_id, name, and the email are columns.

3. Rows (records/tuples)
The rows are the horizontal elements in a table that show the individual data entries.
Example: one row in a Users table can contain like number one: rehan which is user name, and the number two: rehan@gmail.com which is hte user email.

This is the practical example for understanding tables, rows, columns use:

if we are making a multi-store e commerce platform so this is the basic use:

- Users
- Stores
- Products

here instead of storing everything in one big structure, the relational design will separate the key parts.

Example:

users:
id	username  email

stores:
id  name  user_id

products
id  name  price  store_id

So here:

each table represents the one entity.
users -> stores the accounts information
stores -> stores the business/store information
products -> stores the items which are sold inside the store

Relationships:
user_id in stores points to the users.id
store_id in products points to the stores.id

So this is the clean relationship chain

User > Store -> Product

in this example the key points are like the:
. one entity = one table
. and the relationships are being handled here with the use of foreign keys



## Primary Key Concept

the key points of a primary key are:

. uniqueness
. different identity

Example:
If a email was the primary key, and then if the user changes email -> so this way the identity changes, so this is not a good way.

Primary key characteristics:
. immutable
. never reused

not so good primary key ideas:
phone_number -> people can change their number
username -> it can also be changed so,

so keeping this in mind is important.


## Foreign Key Concept

A foreign key creates a relationship check for connecting different components properly.
Example:
store.product_id points to the products.id

so this means:
we cannot add a product with product_id = 20 if the store does not exist.


foreign keys other imp points:
CASCADE -> deletes the child automatically
SET NULL -> orphan but keep record
RESTRICT -> block deletion

so without the foreign keys:
the database will not work properly.


## Constraints -> help in data safety

the constraints protect our data, like:

-- NOT NULL
this prevents the data needed is not.

-- UNIQUE
this prevents the duplication.

Example:
CHECK
age INT CHECK (age >= 18)

DEFAULT
status VARCHAR(21) DEFAULT 'pending'

## NULL vs NOT NULL

NULL simply means:
. the unknown value

Example:
salary = NULL
. so is this mean 0? -> then the answer is no
. does this mean its empty? -> then the answer is again no.

in reality it means:
we don’t know.

key point:
the NULL acts differently in comparison to the IS NULL.
like,
WHERE salary = NULL   
WHERE salary IS NULL 

so the point to remember is NULL is not equal to anything, even itself.


## SQL Key Concepts

the simple sql query with logic is like:

SELECT name
FROM users
WHERE age > 18
ORDER BY name;

the main points to understand here are:

FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT

--- SELECT
The Select chooses columns, means from where we select the specific data from the given table for example.

--- WHERE 
a condition for filtering perhaps, like we select adn then condition is applied where this requirement is needed.

Example:
SELECT *
FROM users
WHERE age > 18;

so simply only the rows condition are kept.

-- GROUP BY
Example:
Count products per store.

SELECT product_id, COUNT(*)
FROM stores
GROUP BY product_id;

so here the rows are grouped by product_id.

-- HAVING 
its like WHERE but the difference is:

. WHERE is used mainly for filtering the rows.
. HAVING is used for filtering the groups.

-- ORDER BY
it is used for sorting the gained results according to the condition we run for extracting or filtering data.

-- LIMIT
it is used for 
restricting the result count we got again after running our conditions. and this is mainly used in pagination logic.


## JOINS 
the concpet of joins is like:
Join = combine the rows based on the related column.

-- INNER JOIN:
this works like intersection like returning values which are common between two points. example could be like:

stores:
1,2,3
products:
product_id 1,1,2

the result:
1,2


-- LEFT JOIN
this is for returning all the left + the matching values from the right, and in this:
the non-matching are considered -> NULL
so this could be used to find the:
stores without products.

SELECT stores.*
FROM stores
LEFT JOIN products
ON stores.id = products.product_id
WHERE products.id IS NULL;


-- RIGHT JOIN
this is opposite to the left join, like this is used for returning all the right + the matching values from the left side:

-- FULL JOIN
these are like union, these return all the values from the both sides, whether the values are similar or different it shows both.


## AGGREGATIONS 
the use of aggregation methods are mainly like for reducing the multiple rows into the one value.

Main Functions:

COUNT -> used for counting the values
SUM -> used for returning the addition or like sum count b/w two values
AVG -> used for returning the average b/w two values
MIN -> used for returning the min possible value inside any row for example
MAX -> used for returning the max possible value inside any row for example

Example:
Average product count per store.

SELECT product_id, COUNT(*) 
FROM stores
GROUP BY product_id;



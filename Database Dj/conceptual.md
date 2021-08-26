Conceptual Exercise
Answer the following questions below:

What is PostgreSQL? PostgreSQL is a relational database management system used to store, access, and manage data.

What is the difference between SQL and PostgreSQL? SQL is the language used to query the database, whereas PostgreSQL is the management system for the database itself.

In psql, how do you connect to a database? \c database_name

What is the difference between HAVING and WHERE? 'WHERE' filters rows before grouping using 'GROUP BY', whereas 'HAVING' filters rows after they have been grouped using 'GROUP BY'.

What is the difference between an INNER and OUTER join? An inner join joins tables based only on the intersecting data of tables. An outer join does so on all data, not just on data that matches both tables.

What is the difference between a LEFT OUTER and RIGHT OUTER join? A left outer returns all data from the left table and any intersecting data from the right table. A right outer returns all data from the right table and any intersecting data from the left table.

What is an ORM? What do they do? An ORM is an object relational mapper such as SQLAlchemy that translates the services between the OOP in a server language and the relational data in a database

What are some differences between making HTTP requests using AJAX and from the server side using a library like requests? Unlike server-side requests, AJAX requests are made from Javascript directly in the browser that allow the app to send requests and receive responses without having to reload the browser page.

What is CSRF? What is the purpose of the CSRF token? CSRF is a type of website exploitation where unauthorized code is transmitted from something such as hidden information in a form. A CSRF token is used in a form to verify that the information being responded with is originating from the app itself and not a malicious entity.

What is the purpose of form.hidden_tag()? This is used in a form to place a hidden field such as a CSRF token that is not directly visible to the app user.
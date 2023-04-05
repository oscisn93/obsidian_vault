# Definitions

**Backend**: The part of the application that is concerned with accessing and processing of application data. Popular backend frameworks include Express.js, Flask, and SpringBoot.

**Database**: Technically a database management system (DBMS) is an application that concerns itself with persistent storage and retrieval of user data. Popular examples include MySQL, MongoDB, and DynamoDB.

# Database Paradigms

SQL: Based on the structure query language, a C-based programming langugae specialized for operations on relationanl tables. ACID. atomicity, consistency, isolation, and durability.

No-SQL: Loose grouping for a wide range of paradigms which are not based around the SQL language. Include document-oriented, key-value, grpah, and column-oriented databases. CAP. consistency, availabilty, and partition tolerance.

# ORM

Object Relational Mappers are programs that help translate your database models into program objects and perform wueries without writing them in the syntax of your own programming laguage rather than in that of the database management system. Popular ORMs are SQLalchemy for Python, Hibernate for Java, and Prisma for NodeJS- a sponsor and the one we will use for this workshop.

# SQL Databases

While there are some differences between SQL based database management systems, there are far more similarities due to the fact that they are all based on the relational entity model and SQL language. For this workshop we will be using MySQL.

# DDL

The downside of using SQL databases is that you have to define the database schema yourself. This requires a signinficant amount of time if you are new to SQL and can result in setting up the database incorrectly if you are not careful. This means definig all the tables in your schema as well as the relational constraints and attribute constraints.

# Using the Prisma CLI

This is where the Prisma CLI comes in. Prisma allws you to define your schema using a much simpler, cross platform syntax. These are defined in the prisma.schema file. Next You'll want to define a Prisma client, using the prisma generate command. This will generate a client for your database that goes through prisma. Finally you run prisma db push to create the database. Now you are ready to populate it and use it in your app.

# Seeding the DB

To seed the database you can go about this one of two ways- the hard way or the easy way. The hard way is to create a seed.ts file that will connect to your database and manually create new rows. However, there is a Prisma CLI tool that can help us: prisma studio. Prisma studio opens up a live server which allows us to add new records to our databse via a GUI.

# Connecting to the DB


# Creating Endpoints

Now that we have created a database and seeded it , we are ready to run queries against it: That is we need to access the data from a frontend application to display to a user. I've created a simple client application here, that will be requesting task objects from the database and presenting them graphically to the user. To create the endpoint we first create a fucntion that access the database and retrieves the data we need. Prisma has an easy to understand handful of methods for this. We need the findMany method. Once weve written this logic, we need to add the function to an endpoint- in express this is writtena s app.get(path, callback) where the callback is executed when the endpoint is requested.

```typescript
import express from "express";
import cors from "cors";

const app = express();

app.use(cors())
app.use(json());

app.get('/tasks', async (req,res)=> {
  const data = await prisma.tasks.findMany()?;
  res.send(data);
})
```


# Fashion_Billing_system

A desktop application built using Tkinter for managing fashion billing operations, including adding, updating, displaying, searching, and deleting customer and product records in a fashion store.
 
1 Install dependencies:

Make sure you have Python installed. Then, install the required package:
pip install pymysql

2. Run the application:
   python fashion_billing_system.py
   
3. Database Setup

 Install MySQL:

Ensure that you have MySQL installed and running on your system.

Create the database and table:

Open your MySQL command line or any MySQL client and run the following commands:
CREATE DATABASE fashion;
USE fashion;
CREATE TABLE fashion(
    PId INT PRIMARY KEY,
    CName VARCHAR(50),
    gender VARCHAR(10),
    address VARCHAR(100),
    MobNo BIGINT,
    ClType VARCHAR(50),
    brand VARCHAR(50),
    cost INT
);

4. Usage

* Add New Record: Fill in the product and customer details and click "Add New" to add a new record to the database.
* Display Records: Click "Display" to fetch and show all records from the database.
* Update Record: Select a record from the list, modify the details, and click "Update" to save changes.
* Delete Record: Select a record from the list and click "Delete" to remove it from the database.
* Search Record: Enter the product ID and click "Search" to find a specific record.
* Reset Form: Click "Reset" to clear all input fields.
Exit Application: Click "Exit" to close the application.

5. Features

Add New Record: Insert new customer and product details into the database.
Display Records: Retrieve and display all records from the database in a tabular format.
Update Record: Modify existing records with new information.
Delete Record: Remove records from the database.
Search Record: Find a specific record by product ID.
User-friendly Interface: Easy to navigate and use with clear labels and buttons.

6. Code Overview
   
The application is implemented using Python's Tkinter library for the GUI and PyMySQL for database operations. Here is a brief overview of the main components:

* Class FashionDB: Main class that initializes the GUI and defines methods for database operations.
  
* Methods:
iExit(): Closes the application.
Reset(): Clears all input fields.
addData(): Adds a new record to the database.
DisplayData(): Displays all records from the database.
fashionInfo(ev): Fetches the selected record details into input fields.
update(): Updates the selected record in the database.
deleteDB(): Deletes the selected record from the database.
searchDB(): Searches for a specific record by product ID.

# Land Rental System

## Scenario

TechnoPropertyNepal is a private company that has a stock of different land on a
contract basis in different locations in Nepal. Thus, the company allows its clients to
rent the available land in various locations. The land stocks which are available are to
be charged on a monthly basis.

The TechnoPropertyNepal manages the availability of the land in a single text file. The
program must be able to read the text file and display the lands that are available or
not available for rent. Adding to that, the program should carry out the changes
according to the nature of the transaction (i.e., renting of the land and returning the
land to the company after the termination of the contract). With each transaction made,
a note or invoice must be generated. For instance, if the customer rents land for 6
months, then the status in the main text file must be modified to not available. Similarly,
if the customer returns the land after the termination of the rental contract, the Status
must be updated to available.

A sample format of the text file including the information about the Land Renting
System is as follows:

101, Kathmandu, North, 4, 50000, Available

102, Pokhara, East, 5, 60000, Not Available

103, Lalitpur, South, 10, 100000, Available

*1st column shows the kitta number of lands, 2nd column shows the name of the
city/district, 3rd column shows the direction of the land (Land Faced), 4th column shows
anna, 5th column shows the price in Nepalese Rupee, 6th column shows the availability
status of the land.

#### Note: You can use your own format and add other information too.

A note/invoice should be generated for each transaction. When land is rented, a
note/invoice should be generated (as a .txt file) which must contain the kitta number
of lands, name of the city/district, the direction of the land (Land Faced), area of land
(anna), name of the customer, date and time of rent, the duration of rent, and the total
amount. Also, if a customer decides to rent more than one land, then the amount
should be added up for all the rented lands.

When the land is returned back, a note/invoice should be generated again which
should include the name of the customer, kitta number of the land, name of the
city/district, the direction of the land (Land Faced), date and time of returning, the
duration of rent, area of land(anna), and the total amount. However, if a client is unable
to renew the contract on time and is late to return the land, in such case a fine should
be applied on a monthly basis which should be written to the file again.

* The format of the notes/invoices is up to you. But each file should have a unique
name. The customer has to take the available land as a whole. For example, if the
kitta number is 101, it includes an area comprising 4 annas of land. The customer
must rent the entire 4 annas of land; they cannot rent less than that.

## Algorithm

- An algorithm should be developed for the application where everything the
program does should be taken into account. The algorithm should be described in
steps, pseudocode, and flowcharts should also be included.

## Data Structures

- The programming should be done using data structures and operations in Python
for input/output, character and string processing, and data storage.
- It can use any primitive or complex data structures which might be necessary for
holding the data (pairs, lists, strings, dictionaries, etc.)
- The choice of data structures must be specified in the report.

## Program

- The program must work in a loop, displaying the available lands and waiting for
the administrator to enter details of the customers. The program should not close
unless the administrator decides to do so.
- The program must check the input data, displaying error messages whenever
unwanted data is entered, for example if some string value is entered where a
numerical value is expected.
- The program must be implemented in a modular way with separate functions for
the different operations such as input/output, reading files, generating
invoices/notes, etc.

## NOTE




FOLLOWING THINGS MUST BE DONE IN YOUR CODING PART OF YOUR COURSEWORK

- code MUST BE divided into 4 different .py(python) files (read, write, main and operations)
- code MUST BE broken down to different functions for different logical task
- code MUST HAVE implementation of TRY EXCEPT BLOCK (at least one TRY EXCEPT BLOCK is required)

FOLLOWING THINGS ARE NOT TO BE DONE IN YOUR CODING PART OF YOUR COURSEWORK

- code MUST NOT contain the naming (naming of VARIABLES, FUNCTIONS AND FILES) like, "abc", "1234", "ccc", "zzz" etc. PROPER naming convention is required
- code MUST NOT contain the ROMAN NEPALI naming like, "aana_validation_gareko", "ID_check_gareko", "user_ko_id","user_ko_quantity" etc.PROPER naming convention is required
- your are NOT ALLOWED to CREATE a function inside of a function, you are ONLY ALLOWED to CALL a function inside of a function

FOLLOWING THINGS CAN BE DONE IN YOUR COURSEWORK

- you CAN name your own land details
- you CAN use 2D list or Dictionary approach to do the coursework
- you CAN user your own format for printing the bill, displaying the bill, user messages, land details, user options
- you CAN use OOP concept to complete your coursework as well
- you CAN add any additional option than rent return and Exit for user
- you CAN write logic for renting non existing land rather than renting the lands that are only available in the text file

FOLLOWING THINGS MUST BE DONE BY YOUR PROGRAM

- your program SHOULD display the available lands 
- your program SHOULD give user  the option to rent, return and EXIT from the system
- your program SHOULD change the STOCK to unavailable to the main text file when rented
- your program SHOULD change the STOCK to available to the main text file when returned
- your program SHOULD be able to rent one or more land at a same time and print all the rented land(s) to one singular bill
- your program SHOULD be able to return one or more land at a same time and print all the returned land(s) to one singular bill
- your program SHOULD generate bill for both rent and return 
- IF your user returned delay than rented month then 10% of price as fine should be applicable .
For example:

Rented month=3
Returned month=6
Price per month = 50000
Aana=4

Then, delayed month=6-3=3 month
Price= (Price per month*Returned month)
	=50000*6
	=300000

Fine_price = 10/100* (Delayed month*Price per month)
	   =10/100*(3*50000)
	   =10/100(150000)=15000

Amount_with_fine=Price+fine_price
		=300000+15000
		=315000

- If your user returned land before rented month, then price for rented month will be applicable 
Rented month=3
Returned month=6
Price per month = 50000
Aana=4
Then, total price= 6*50000=300000
- your program SHOULD generate each bill uniquely 
- your program SHOULD NOT crash in any way because of some invalid input or any other cause
- Make sure to add single/multiline comments to your code and also make sure to add docstrings.
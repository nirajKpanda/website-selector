# website-selector 

Python script which scraps the given set of websites as input and test wheather it is a ecommerce website or not.

## Getting Started

Developed and tested in Python 3.X and windows OS. But we can run and use this wrapper as per our envornment UNIX/MAC.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.x
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
pip
```

```
pandas : pip install pandas
```

```
requests : pip install requests
```

```
Rest of the modules come acorss the python 3.x distribution. If not we can install it by pip install <module-name>
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
python ecom_website_selector.py -i <input file of all websites> -o <output csv file where you need to store the result>[Not Mandatory]
```

### Design approach

1. Read all websites from given input .txt file and storing into a list of websites
2. Iterating each website in the wbsites list to test wheather it is an ecommerce website or not?
3. Using request module to get the html markup of the given website home page
4. Expecting some given links in the website html markup to confirm the site is ecommerce or not.


### Limitations

1. If certain webite cannot be reached during time of test, script would have mark it as non ecommerce site due to HTTP error.
2. Relying more on given sets of links to validate the website is ecommerce or not.


###  Scope of imporovement

-> More efficient web scrapping design to validate the site is ecommerce or not.

# Dummy Database Writer

Dummy Database Writer is a CLI which allows you to generate random data for databases.

> **Note**
> This project is still being worked on

## Dependencies:
- <b>Python</b> (<a href="https://www.python.org/downloads/">Install here</a>)
- <b>Pip</b> (<a href="https://www.geeksforgeeks.org/download-and-install-pip-latest-version/">Install here</a>)

## Installation
Download the <a href="https://github.com/jorgealves/dummy_db_writer/releases">latest release</a> archive. <br> 

Install the script using <b>pip</b>:

```
pip install dummy_db_writer-0.1.0.zip
``` 

## Usage
Run: writer go [OPTIONS]

Options:

  -t, --table TEXT | **Table name**
  
  -c, --column TEXT | **Column name**
  
  -v, --columnValue [name/date/email/text/address/zipcode] | **Table column value**                         
  
  -n, --records INTEGER [default: 50] | **Number of records to create**
  
  --help     

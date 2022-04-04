# Loan Qualifier Application

*LOAN QUALIFIER APPLICATION* is a command line application to match applicants with qualifying loans. This application automate the time intensive handling of filtering loan data based on various set criterias from a list of institutions. The application automaticaly filters data from a given data file (.csv) comparing them to the user CLI input and allows to output the qualifying loans data to a csv file if desired.

It is currently being developed as part of a UCBerkeley Bootcamp.

---

## Requirements

This application was writen in Python 3.9.7.

**Operating System:**
* Window 10 (or higher) using Gitbash.
* MacOS 10.14 (or higher) using a terminal.
* Linux Ubuntu 20.04 (or higher) using a terminal.

**Will need to be installed:**

*fire* 0.4.0
```
$ pip install fire
```

*questionary* 1.10.0

```
$ pip install questionary
```

---

## Installation

To install the application you will need to clone the GitHub repository.

```
$ git clone https://github.com/yanickw/loan_qualifier_application.git
```


---

## Get Started

Running the *LOAN QUALIFIER APPLICATION*:
```
$ python app.py
```
You'll then get prompt a first question. Rate-sheet can be access from any relative path location. For this example we are using a generic rate-sheet csv file located in the folder /data.
```
? Enter a file path to a rate-sheet (.csv): data/daily_rate_sheet.csv
```
Here's the list of criteria to determine which loans the user qualifies for.
* **Credit Score:** <span style="color: blue;"> *The applicant's current credit score.*</span>
* **Loan Size:** <span style="color: blue;"> *The applicant's total monthly debt payments.*</span>
* **Debt to Income Ratio:** <span style="color: blue;"> *Calculated from the applicant's total monthly debt payments against his total monthly income.*</span>
* **Loan to Value ratio:** <span style="color: blue;"> *Calculated from the applicant's loan amount against the estimated home value.*</span>

In order to return the list of loans the following questions are prompt to the user from the CLI:
```
? What's your credit score? 
? What's your current amount of monthly debt? 
? What's your total monthly income? <The applicant's total monthly income.>
? What's your desired loan amount? <The total loan amount applied for.>
? What's your home value? <The estimated home value.>
```

Following these questions the CLI then displays information about:
* *The applicant monthly debt to income ratio.*
* *The loan to value ratio.*
* *The amount of qualifying loans found based on the criteria.*

If you wish, you can then save the list of qualifying loans to a ".csv" file by answering these questions:
```
? Would you like to save the file? < Yes / No >
? Where do you want to save the file (.csv)? <directory>/<filename.csv>
```

The resulting ".csv" file will contain the filtered qualifying loans with header.

| Lender  | Max Loan Amount | Max LTV | Max DTI | Min Credit Score | Interest Rate |
| ------- |:---------------:|:-------:|:-------:|:----------------:|:-------------:|
|         |                 |         |         |                  |               |

---

## Contributors

This application originated from a Berkeley Bootcamp.

For any inquieries, feedbacks or comments about this project please email me at yanickw@gmail.com

I can also be reached on [LinkedIn](https://www.linkedin.com/in/yanickwilisky/)
or  [Twitter](https://twitter.com/yanickwilisky).

---

## License

MIT License

Copyright (c) 2022 Yanick Wilisky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

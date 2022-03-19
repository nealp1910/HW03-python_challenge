Goals Not Directly Python
1.  Basics of Terminal so you can navigate to python files located in folders (Day1)
1.  Update repository files from command line (Day 1)
1.  Clone GitHub folder and add files and push content back to GitHub.  Similar to Homework process (Day3)
​
​
​
Goals of Each Day  
Day 1:
1.  Create conda environment and activate it  
1.  Run python files from terminal using `python <filename>`
1.  Setting Variables and using the print statement.  Note:  f-strings are the most widely used method i.e. `print(f"Text like you want to see it and add variable content with curly brackets {variable}")`
1.  Prompts using `input_response = input("Message goes here about what to type: ")`
1.  Operators (ie =, ==, !=, etc):  Best summary for this is [here](https://www.w3schools.com/python/python_operators.asp).
1.  Flow Control:  if/elif/else Structure (aka Flow Control).  See this reference [here](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
1.  Data Structures - List (aka [ ]  ) versus Tuple (aka ( )  ).  We will add to this sets and dictionaries and these are the 4 data structures in python. Here is a good [document](https://docs.python.org/3/tutorial/datastructures.html#).
1.  Loops - for/while
​
Day 2:  
1.  Loop Practice
1.  Reading/Writing Files using `with open` and `csv.reader` and `csv.writer`
1.  Zipping Data 
1.  Reading, Storing, and Manipulating Data - Activity 12 is Similar to Homework.
1.  Functions that only print message to console (not very helpful but an introduction)
​
Day 3:
1.  Dictionaries
1.  Making lists from lists (list comprehensions)
1.  Functions that use a return (very helpful)
1.  Examples of caculations and multiple concepts combined.
​
Homework:
1.  Make repo (Day 3 Topic):
    *  Go to GitHub and click on the Cat logo in the upper left corner.  Find the Green button that says `New`
    *  On the Create a new repository page.  Fill in the repo name, give it a short description (can be changed later), select Public, select Add a README, select Add .gitignore, in the new dropdown select Python.
    * Click `Create repository`
1.  You should now see your new repo and it will only have an empty README.md file and a .gitignore file.  Lets add these to your desktop.
1.  Clone repo:  
    *  On the repo main page, click the green `Code` button.
    *  There are three link options (HTTPS, SSH, GithubCLI), make sure to click the SSH tab.  The link will then look like `git@github.com:<username>/<repo name>.git`.
    *  Copy the link and go to your desktop and right click and choose 'Git Bash Here' or 'Open terminal in Folder'.  
    *  In this terminal type, `git clone <paste link here>`.  This downloads a folder on your desktop that is linked to the online repo.
1.  Open this folder on your desktop like you normally would.  Copy the homework files into this folder.
1.  Have your file structure inside this repo look like this for the python homework:  
```
      python_challenge 
            |__ PyBank 
            |    |__ Analysis/ 
            |    |__ Resources/  
            |    |   |__ budget_data.csv
            |    |
            |    |__ main.py
            |
            |__ PyPoll  
            |    |__ Analysis/ 
            |    |__ Resources/  
            |    |   |__ election_data.csv
            |    |
            |    |__ main.py
            |
            |__ README.md
            |__ .gitignore
​
```
1.  The key concepts I would work on understanding that apply for the homework are:  
    *  Prompts - Day 1, Activity 4
    *  Conditionals - Day 1, Acitivity 8
    *  Lists - Day 1, Activity 9 (append(), index())
    *  Loops - Day 1, Activity 11 (for/in, range(), len())
    *  Read csvs - Several examples but Day 2, Activity 9 explore it well
    *  Data capture - Day 2, Activity 12 (uses lists, appends, csv.reader, for loops).  This is probably similar to the homework.
    *  Dictionaries - Day 3, Activity 3 - good for PyPoll
    *  List comprehensions - Day 3, Activity 5
    *  Maybe there are some other activities that can give you inspiration.  
    
1.  After Day 2 you can start attempting to read the data and print it to the terminal.  If you use the structure above then I image one line of code would be for PyBank `os.path.join("Resources", "budget_data.csv")`.  Can you explain why it would be this instead of what you saw in most of the class activities?  It's slightly differet.  How to use this further is done in Activity 12, and some Day 3 early activities and will be covered next.  
1.  PyBank is probably the easier one to code and can be completed using lists.  
    *  It is a similar concept to the VBA homework where we are looping through data and restructing it.
    *  Most of the concepts are learned in Day2 Activities
1.  PyPoll is probably a bit more complicated to program but easier to understand than PyBank and can be completed using lists or dictionaries.
    * List could be used to complete this activity by using the `if` and `in` structure and `list.index()` method that we say in `Day 1 Activity 8 and Activity 9`.  The more official way of doing it is to use a dictionary because a dictionary structure was created for this type of data.
1.  At this point, you can start planning what you should do on paper.  Read the instructions about what is required and see if you can write steps for what is needed.
    *  Need to bring the data into the script - aka csvreader, csv.reader
    *  At the end, a command line output and file needs generated - aka print() and csv.writer
    *  What do we do with data after we read it?  It's coming next in Day 2, Activity 12 and Day 3, Activities.  Hint: in some cases we will add it to lists and in some cases we can do calculations with this as each row is read.
    *  Check the data file.  Also, note that Excel will not read the Date column correctly.  Look at the .csv file in VSCode or in a text editor.  The data is in Month-Year format.  What does each column represent?  If I was going to do the objectives of this assignment, I would first ask myself how would I do this manually. The questions asked are as follows:
        *  Refer to the sample analysis output at the bottom to make sense of the objectives.
        *  Total months is self explanitory after looking at the data
        *  Total:  The data file is a list of profit/loss data of just each month so the net total amount is the summation of all the numerical data
        *  The changes in proit/loss is a month-to-month calculation finding the change between each month as in this month less last month (hint:  you will need this calculated monthly data for the next two questions).  The sum of all these differences added together then divided by the total months makes a single value called "Average Change".  See homework sample output.
        * The greatest increase in profits is using the month-to-month profit change calculated previously and finding the max value out of all the months. You need to find the month and the greatest amount.
        *  Same idea with greatest decrease.  The greatest drop from one month to the next.  Need to find the month and the value.  
    
​
​
​
The final output of your script should look similar to the following:
​
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```
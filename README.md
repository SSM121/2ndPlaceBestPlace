# 2ndPlaceBestPlace

This is the main repo for CS-3450, Introduction to Software Engineering, Spring 2021.
The members of this team are James Bates, Nathan Holst, Spencer Clemens, and Spencer Kasteler.


Proffessor: Dan Watson
TA: Bradley Payne

## Repo Organization and Naming Scheme
Lower Camel Case is the naming scheme for any file we can change the name of. Django default file names are left as is. The source files are located in the src directory and the documentation is located in docs. 
## Version Control Procedure
Each member should fork or branch the repo and submit pull or merge requests. The requests should be reviewed by someone else on the team before they are accepted. If 24 hrs go by without a review the person submitting the code may accept the merge.
## Tool Stack Description and Setup Procedure
### Software stack requirements
1. Python 3.7 or later
2. Django 3.1.5 or later
3. Vanilla Javascript

### Setup instructions
On first git pull run ```python src/manage.py migrate```
## Build Instructions
run ```python src/manage.py runserver```
## Unit Testing
#### Intro
As no code has been written the team will eventually create methods that verfie that specfic sections of the probram behiave as designed. The unit tests will have three phases.
#### The three phases of unit tests
 1. Initialize a small chunk of the program (AKA System under test)
 2. Apply some stimulus to the system under test
 3. Observe resulting behavior
## System Testing
#### Intro
 Just like in the unit testing section code has yet to be written so the following will be a general outline of what the team is planning on doing. The purpose of the system test is to determine if the system works as a whole unit. The team will test the software for the following.
#### Things to look for in system testing:
* Mainline functions: Do the main functions of the application behave as expected?
* Basic Usability: Can a user freely navigate through the screens without any difficulties
* Accessibility: Is the system easily accessible for the end user?
* Error Conditions: Are suitable error messages displayed when something goes wrong?
* Load Testing: Does the system work well under load?
* Regression Testing: When a new feature is added does the addition create or recreate bugs? 



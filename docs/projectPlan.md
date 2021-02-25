# Parking Genie
## Project Summary
### general overview
The Parking Lot Genie is an app that helps connect event directors with local parking space owners and event attendees. From dedicated parking lots to individual driveways the Parking Lot Genie helps simplify finding a place to park for any event.
### Current Phase
The Parking Genie is currently under development. The team is in the requirements gathering phase. The main goals/ objectives of this phase are to visualize and describe in detail what the finished project should look like. During this phase we are also flushing out team roles, project structure, definitions, and other organizational materials. 

## Team Organization

### Positions 

* Leader (Project Manager)
  * Nathan Holst
 
* Member
  * James Bates
  * Spencer Kastler
  * Spencer Clemens
 
### Skills

* Python
  * Spencer Clemens
  * Jame Bates
  * Nathan Holst
  * Spencer Kastler
* Java Script
  * Nathan Holst
  * Spencer Kastler
* HTML
  * Spencer Clemens
  * James Bates
  * Nathan Holst
* GitHub
  * Spencer Clemens
  * James Bates
* Django
  * Nathan Holst
  * Spencer Kastler
* SQLite
  * None
* Discord
  * Spencer Clemens
  * James Bates
* Mark Down Documentation
  * Spencer Kastler
  * Nathan Holst
  * Spencer Clemens
* Aws/ Other cloud hosts
  * Spencer Clemens

## Software Development Process
The development will be broken up into five phases.  Each phase will be a little like a Sprint in an Agile method and a little like an iteration in a Spiral process.  Specifically, each phase will be like a Sprint, in that work to be done will be organized into small tasks, placed into a “backlog”, and prioritized.   Then, using on time-box scheduling, the team will decide which tasks the phase (Sprint) will address.  The team will use a Scrum Board to keep track of tasks in the backlog, those that will be part of the current Sprint, those in progress, and those that are done.

Each phase will also be a little like an iteration in a Spiral process, in that each phase will include some risk analysis and that any development activity (requirements capture, analysis, design, implementation, etc.) can be done during any phase.  Early phases will focus on understanding (requirements capture and analysis) and subsequent phases will focus on design and implementation.  Each phase will include a retrospective.

| Phase | Iteration |
|-------|-----------|
|   1   | Requirements Capture |
|   2   | Analysis, Architectural, UI, and DB Design |
|   3   |  Implementation, and Unit Testing |
|   4   |  More Implementation and Testing  |

We will use Unified Modeling Language (UML) to document user goals, structural concepts, component interactions, and behaviors.

## Communication Policy 2/11/2021

### General Communication
* Policies for communication
  * Academic Freedom and Professional Responsibilites:

    Academic freedom is the right to teach, study, discuss, investigate, discover, create, and publish freely. Academic freedom protects the rights of faculty members in teaching and of students in learning. Freedom in research is fundamental to the advancement of truth. Faculty members are entitled to full freedom in teaching, research, and creative activities, subject to the limitations imposed by professional responsibility. USU Policy 403 further defines academic freedom and professional responsibilities.

* Tools for communication
  * Direct communication
    * The project team members will use discord to directly communicate ideas, project updates, etc. Discord was choosen as the desired platform for communication due to Discords ability to create new chanels, document interactions, and ability to communicate through more than just text. 

* Team Meetings
  * The team meets every Tuesday and Thursday during class time.
  * Additinal meetings can be set up if desired.

* Online cordination --- Needs more work past this point
  * Discord
  * Trello Board : https://trello.com/b/WEys9Bi9/2ndplacebestplacetrelloboard
* Reporting progress
  * Trello Board
  * Final Group Review before Assignment Due Date

## Risk Analysis
###1 Account Manipulation
*Likelyhood: low
*Severity: high
*Consequences:
Because this includes account verification, there would be no way to sign in to the account, so no one could add events, no one could add parking to those events, no one could purchase parking spots or verify that a parking spot was purchased.
*Workarounds:
Go back to how things are without the app, first come first serve for parking with the attendant taking money when the customer arrives.

###2 Parking Lot Manipulation
*Likelyhood: low
*Severity: high
*Consequences:
There would be no parking available in the database in which to purchase parking for an Event.
*Workarounds:
Go back to how things are without the app, first come first serve for parking with the attendant taking money when the customer arrives.

###3 Purchase Parking Spots
*Likelyhood: low
*Severity: med
*Consequences:
Customers would only be able to view available parking lots not purchase a space prior to event.
*Workarounds:
Attendants update current lot availability, and sell spots at entry to parking lot.

###4 Event Manipulation
*Likelyhood: low
*Severity: high
*Consequences:
No events, no need for parking at those events...
*Workarounds:
Go back to how things are without the app, first come first serve for parking with the attendant taking money when the customer arrives.

###5 Money Manipulation
*Likelyhood: low
*Severity: med
*Consequences: 
Customers would not be able to purchase a parking spot, Owners would not receive their payment from customers.
*Workarounds:
Modify code for customers to "reserve" a parking space, then have attendants collect payment upon arrival of customer.

###6 Parking Pass Generation
*Likelyhood: low
*Severity: med
*Consequences:
Customer would not have any form of receipt for their purchase, or proof that they should park in that spot.
*Workarounds:
Attendants check customers names off of a list of those having purchased a spot in their lot.


## Configuration Managment
See the repo [README](../README.md)

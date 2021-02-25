# Introduction and Context
When a large event happens up at the University there can be a major influx of vehicles attempting to park as close as possible while also not having to pay very much. Some of these vehicles expect a large group area in which to "tailgate" before the event, while others just want a space big enough to squeeze their car into. Because all of these vehicles attempting to fight for the same few parking spots can create not only stress, but sometimes irritation leading to road rage. The Parking Genie, is a savior for all. Even if you end up parking farther away than you would have liked, knowing that you have a parking spot can still take away the stress of getting to an event and not having a place to park.

This document describes the different users and their goals. It then describes the function requirements of how this program will assist those users in acheiving their goals, and the non-functional requirements of how this program is being developed. The next section covers the future features that have yet to be added to this program, yet are not yet implemented. The final portion of this document is a Glossary of terms and how they are defined in the context of this program.

# Users and Their Goals
## Administrator
Maintain the application.

## Attendant
Authenticate customer with QR code or from list.
Show customer where to park.

## Customer
Purchase a parking spot for an event. 
Get directions to their parking spot.
Receive QR code as proof of purchase.
Add money to their account.

## Manager
Add events to database.
Check revenue.
Pay owners.

## Owner
Add parking lot to Event.
Receive income from application.

# Functional Requirements
1. Account manipulation
#### The ability for a customer, manager, owner, or administrator to launch, terminate, or edit the properties of an account based apon the users authorization level.
    1. create an account
    2. edit an account
    3. delete an account
    4. authenticate an account
2. Parking Lot manipulation

#### The ability for a manager, owner, or administrator to launch, terminate, or edit the properties of a parking lot based apon the users authorization level.
    1. add parking lots
    2. remove parking lots
    3. connect parking lots to an event
    4. filter parking by location
    5. filter parking by price
3. Purchase parking spots

#### The ability for a user to purchase a spot for an event.
    1. buy a parking space
    2. show parking location(s)
    3. cancel purchase of a parking space
4. Event manipulation

#### The ability for a manager, or administrator to launch, terminate, or edit the properties of an Event based apon the users authorization level.
    1. add events
    2. edit events
    3. cancel events
5. Money manipulations

#### Receive payments from the user or assign credit to mangers and owners.
    1. receive payments/ Deduct credit from account
    2. Add money to fictional test account
    3. check revenue of all lots/ specific lots
    4. Pay out users
6. Parking pass generation 

#### Generate QR codes for the users to display at arivial of the parking lot
    1. receive QR codes as proof of purchase
    2. generate QR codes 
    3. authenticate QR codes


# Non-Functional Requirements
1. Back End Authentication
    1. Payment Authentication
    2. User Rights Authentication
    3. Use cryptogaphry instead of plain text for user password Authentication

# Future Features
1. Android and ios apps
2. integration with various payment systems 


# Glossary
## Administrator
Person who maintains the application, educates and assists managers when necessary.

## Attendant
Temporary account for the person who verifies that customer has purchased a parking spot and directs them to that spots location.

## Authenticator <<Service>>
A back end tool that will verify a users account and privileges of that account.

## Customer
One who uses this application to find and purchase a parking spot so that they may attend an Event.

## Database
Server location of Events, parking lots, and user accounts.

## Event
A large gathering of people at the University that would necessitate additional parking.

## Manager
Person who receives Event information from the University and adds it to the database. Also in charge of distributing money gained through application to owners.

## Owner
Person who has legal control of a parking lot and wishes to use this application to gain revenue for its use during an Event.

## Parking Lot
A location with at least one Parking Spot or Tailgate Parking Spot, that has at least one attendant, is legally controlled by an owner, and can be added to an event.

## Parking Spot
A location for parking inside of a parking lot. 

## Tailgate Parking Spot
A larger parking spot to accomodate a larger vehicle and have room for a "tailgate party."

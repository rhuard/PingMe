# PingMe
 potential-carnival
 
Master: [![Build Status](https://travis-ci.org/rhuard/PingMe.svg?branch=master)](https://travis-ci.org/rhuard/PingMe)
Dev: [![Build Status](https://travis-ci.org/rhuard/PingMe.svg?branch=dev)](https://travis-ci.org/rhuard/PingMe)

The idea is to create a program that will run an arbitray executable.
Then when done report the time and the status of the executable through
various methods.

##Usage
PingMe.py "ls -al" [Lists all directories in the current folder and pings when done]

PingMe.py -c test_wait [runs the file test_wait then pings when done]

### options
-h, --help [displayes help message]
-r, --reporter [chooses reporter]

## Hierarchy
Tests [contain executable files and unit tests for Probram]

PingMe.py [Executable to call, parses options]

PingMe [Package for PingMe functonality]

PingMe/Execute [contains Executor classes these are what allows arbirary execution]
PingMe/Ping [Contains Pinger Classes which allow for different notifcation types]
PingMe/eporter [Gets infromation from the Executor and gives to the pinger]

## Extending

In order to implement a new Ping Method, implement the Pinger for such a Method
Then you will need to add the option to the PingMe.py parser

If you want more information to ping yourself with then you will need to
implement another Reporter (and also extend the executor)

To implement another you are going to want to inherit form Basic reporter
and override the report (which already takes **kwargs so go nuts ;) )

To implement another Executor inherit from an existing executor and
override execute Method.

## Current/Planned Functionality

Current Pingers:
Console (c or console option)

Planned:
Text
Email

current Executor/Reporters:
Basic [just time for execution and Return Code]

Planned:
StartStop [start time and stop time of execution and return code]

#!/usr/bin/python3
import optparse
import PingMe.Ping.Pinger as P
import PingMe.Ping.TextPinger as T

def Setup():

    #create parser for options
    parser = optparse.OptionParser()
    parser.add_option("-r", "--reporter", dest="report",
                        help="reporter you would like to use")

    #create Pinger dictonary
    pingers = {"c": P.Pinger,
     "Console": P.Pinger,
     "t": T.TextPinger,
     "Text": T.TextPinger}

    return parser,pingers

def Main():

    parser,pingers = Setup()
    (options, args) = parser.parse_args()

    #default to Console
    if options.report == None:
        options.report = "c"

    p = pingers[options.report]()
    p.RunThenPing(args[0])

if __name__ == "__main__":
    Main()

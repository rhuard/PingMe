#!/usr/bin/python3
import optparse
import PingMe.Ping.Pinger as P
import PingMe.Ping.TextPinger as T
import PingMe.Ping.EmailPinger as E

def Setup():

    #create parser for options
    parser = optparse.OptionParser()
    parser.add_option("-p", "--pinger", dest="pinger",
                        help="pinger you would like to use")

    #create Pinger dictonary
    pingers = {"c": P.Pinger,
     "console": P.Pinger,
     "t": T.TextPinger,
     "text": T.TextPinger,
     "e" : E.EmailPinger,
     "email" : E.EmailPinger}

    return parser,pingers

def Main():

    parser,pingers = Setup()
    (options, args) = parser.parse_args()

    #default to Console
    if options.pinger == None:
        options.pinger = "c"

    p = pingers[options.pinger]()
    p.RunThenPing(args)

if __name__ == "__main__":
    Main()

import PingMe.Reporter.BasicReporter as BR
import PingMe.Execute.Executor as E

class Pinger():

    def __init__(self):
        pass

    def RunThenPing(self, args):
        reporter = BR.BasicReporter()
        e = E.Executor(args, reporter)

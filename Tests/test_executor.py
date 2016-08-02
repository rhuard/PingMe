from PingMe.Reporter.BasicReporter import BasicReporter as R
from PingMe.Execute.Executor import Executor as E

def test_executor_echo():
    r = R()
    e = E(['echo','test 123'], r)
    r_code = e.Execute()
    assert 0 == r_code

def test_executor_unknown():
    r = R()
    e = E(['adsaf','test 123'], r)
    r_code = e.Execute()
    assert -1 == r_code

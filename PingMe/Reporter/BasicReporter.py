class BasicReporter():

    def __init__(self):
        pass

    def Report(self, *args, **kwargs):
        print("\n*****************************")
        print("time taken: " + str(round(kwargs['ttime'], 2)))
        print("Return Code " + str(kwargs['rcode']))

class Covid_India:

    def __init__(self, state, confirmed, active, recovered, deceased, tested):
        self.state = state
        self.confirmed = confirmed
        self.active = active
        self.recovered = recovered
        self.deceased = deceased
        self.tested = tested


def main():

    ob1 = Covid_India("Punjab", 567844, 345678, 12345, 2343, 2436654)

    print(ob1.__dict__ )




if __name__ == '__main__':
    main()

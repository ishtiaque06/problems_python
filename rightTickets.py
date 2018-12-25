# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Event:
    def __init__(self, list):
        self.id = int(list[0])
        self.x = int(list[1])
        self.y = int(list[2])
        pricesInt = [int(item) for item in list[3:]]
        self.ticketPrices = sorted(pricesInt, reverse=True)

    def __repr__(self):
        return str((self.id, self.x, self.y, self.ticketPrices))


class Buyer:
    def __init__(self, list):
        self.x = int(list[0])
        self.y = int(list[1])

    def __repr__(self):
        return str((self.x, self.y))


def properTickets(buyers, events):
    for buyer in buyers:
        distance = []
        event_dict = {}
        for event in events:
            if len(event.ticketPrices) != 0:
                event_dict[event] = manhattan_distance(buyer.x, buyer.y, event.x, event.y)
        min_distance_events = [min(event_dict, key=event_dict.get)]
        if len(min_distance_events) == 1:
            print("{} {}".format(min_distance_events[0].id, min_distance_events[0].ticketPrices.pop()))


# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())

numberOfEvents = int(input())
EventStore = []
for i in range(numberOfEvents):
    eventLine = input()  # EvendID EventX EventY listOfPrices
    # TODO: you will need to parse and store the events
    eventList = eventLine.split(" ")
    EventStore.append(Event(eventList))

numberOfBuyers = int(input())
BuyerStore = []
for i in range(numberOfBuyers):
    buyerLine = input()
    # TODO: you will need to parse and store the buyers
    buyerList = buyerLine.split(" ")
    BuyerStore.append(Buyer(buyerList))

# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)


properTickets(BuyerStore, EventStore)
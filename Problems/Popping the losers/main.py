# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
firms = OrderedDict(json.loads(input()))
# from collections import OrderedDict
# firms = OrderedDict({"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0, "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3})

# your code here

firms.popitem(last=True)
firms.popitem(last=True)
print(firms)

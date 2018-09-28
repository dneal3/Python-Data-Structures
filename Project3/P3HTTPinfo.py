class HTTPinfo():
    def __init__(self, ip=None, tier=None, estimate=None):
        self.ip = ip
        self.tier = tier
        self.estimate = estimate

    def __repr__(self):
        return '[{}, {}, {}]'.format(self.ip, self.tier, self.estimate)

        # I got the idea to use rich comps from Prof. Sventek in class
        
    def __eq__(self, other):
        if (self.tier == other.tier) and (self.estimate == other.estimate):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.tier == other.tier):
            if int(self.estimate) > int(other.estimate): # turn into ints cuz string comps are not what im looking for
                return True # higher estimate means it is less 
            else:
                return False # lower estimate means it's greater

        elif ((self.tier == "B") and (other.tier == "A")): # b is always less important than a
            return True

        elif ((self.tier == "A") and (other.tier == "B")): # a is always greater than b 
            return False
        

    def __gt__(self, other):
        if (self.tier == other.tier):
            if int(self.estimate) < int(other.estimate):
                return True
            else:
                return False

        elif (self.tier == "B") and (other.tier == "A"):
            return False

        elif (self.tier == "A") and (other.tier == "B"):
            return True

    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True

    def __ge__(self, other):
        if (self.tier == other.tier) and (self.estimate == other.estimate):
            return True
        elif (self.tier == other.tier):
            if int(self.estimate) < int(other.estimate):
                return True
            else:
                return False

        elif (self.tier == "B") and (other.tier == "A"):
            return False

        elif (self.tier == "A") and (other.tier == "B"):
            return True


    def __le__(self, other):
        if (self.tier == other.tier) and (self.estimate == other.estimate):
            return True
        
        elif (self.tier == other.tier):
            if int(self.estimate) > int(other.estimate):
                return True
            else:
                return False

        elif (self.tier == "B") and (other.tier == "A"):
            return True

        elif (self.tier == "A") and (other.tier == "B"):
            return False

    # i could however use my rich comparisons to 'sort' the list
    # i think i can make a list of a tiers and b tiers , then i can by only estimates
    # although my rich comparisons take that into account so it really isnt that necessary
    # i'd need to iterate through my priority queue for each thing though which is probably log n time
    # and then i'd need to compare each thing to each thing, only really need the __ge__ or __le__
    # operators though. 


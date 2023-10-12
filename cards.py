from settings import *

LANDMARKS={"Harbor":        [2,"When you roll the dice, if the result is 10+, you may add 2 to the total."], #0 - done
           "Train Station": [4,"You may roll 1 or 2 dice."], #1 - done
           "Shopping Mall": [10,"Your 'cup' and 'house' establisments earn +1 coin when activated."], #2 - done
           "Amusement Park":[16,"If you roll doubles, take another turn after this one."], #3 - done
           "Radio Tower":   [22,"Once per turn, you may reroll the dice."], #4 - done
           "Airport":       [30,"If you do not build anything on your turn, get 10 coins from the bank."], #5 - done
           "City Hall":     [0,"After earning income, if you have no coins, get 1 coin from the bank."] #6 - done
          }

#                                     cost color rolls reward symbol description
PROPERTIES_16={ "Bakery":            [1,GREEN,[2,3],1,'house',"Get 1 coin from the bank. (your turn only)"],
                "General Store":     [0,GREEN,[2],2,'house',"If you have less than 2 landmarks built, get 2 coins from the bank. (your turn only)"],
                "Convenience Store": [2,GREEN,[4],3,'house',"Get 3 coins from the bank. (your turn only)"],
                "Flower Shop":       [1,GREEN,[6],1,'house',"Get 3 coins from the bank for each Flower Garden you own. (your turn only)"],
                "Demolition Company":[2,GREEN,[4],8,'briefcase',"Demolish 1 of your built landmarks (flip it back over). When you do, get 8 coins from the bank. (your turn only)"],
                "Loan Office":       [-5,GREEN,[5,6],-2,'briefcase',"When built, get 5 coins from the bank. When activated, pay 2 coins to the bank. (your turn only)"],
                
                "Wheat Field":       [1,BLUE,[1],1,'grain',"Get 1 coin from the bank. (anyone's turn)"],
                "Ranch":             [1,BLUE,[2],1,'cow',"Get 1 coin from the bank. (anyone's turn)"],
                "Corn Field":        [2,BLUE,[3,4],1,'grain',"If you have less than 2 landmarks built, get 1 coin from the bank. (anyone's turn)"],
                "Flower Garden":     [2,BLUE,[4],1,'grain',"Get 1 coin from the bank. (anyone's turn)"],
                "Forest":            [3,BLUE,[5],1,'sun',"Get 1 coin from the bank. (anyone's turn)"],
                
                "Cafe":              [2,RED,[3],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Sushi Bar":         [4,RED,[1],3,'cup',"If you own a harbor, take 3 coins from the active player. (opponent's turn)"],
                "French Restaurant": [3,RED,[5],5,'cup',"If the active player has at least 2 landmarks built, take 5 coins from them. (opponent's turn)"],
              }

PROPERTIES_714={"Cheese Factory":     [5,GREEN,[7],3,'factory',"Get 3 coins from the bank for each 'cow' establishment you own. (your turn only)"],
                "Furniture Factory":  [3,GREEN,[8],3,'factory',"Get 3 coins from the bank for each 'sun' establishment you own. (your turn only)"],
                "Winery":             [3,GREEN,[9],6,'factory',"Get 6 coins from the bank for each Vineyard you own. Then close this establishment for renovation. (your turn only)"],
                "Soda Bottling Plant":[5,GREEN,[11],1,'factory',"Get 1 coin from the bank for each 'cup' establishment owned by all players. (your turn only)"],
                "Farmer's Market":    [2,GREEN,[11,12],2,'fruit',"Get 2 coins from the bank for each 'grain' establishment you own. (your turn only)"],
                "Food Warehouse":     [2,GREEN,[12,13],2,'house',"Get 2 coins from the bank for each 'cup' establishment you own. (your turn only)"],
                "Moving Company":     [2,GREEN,[9,10],4,'briefcase',"Give 1 of your non 'tower' establishments to an opponent. When you do, get 4 coins from the bank. (your turn only)"],
                
                "Vineyard":          [3,BLUE,[7],3,'grain',"Get 3 coins from the bank. (anyone's turn)"],
                "Mackerel Boat":     [2,BLUE,[8],3,'boat',"If you own a harbor, get 3 coins from the bank. (anyone's turn)"],
                "Mine":              [6,BLUE,[9],5,'sun',"Get 5 coins from the bank. (anyone's turn)"],
                "Apple Orchard":     [3,BLUE,[10],3,'grain',"Get 3 coins from the bank. (anyone's turn)"],
                "Tuna Boat":         [5,BLUE,[12,13,14],0,'boat',"The active player rolls 2 dice. If you own a harbor, get coins from the bank equal to the result. (anyone's turn)"],
                
                "Pizza Joint":       [1,RED,[7],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Hamburger Stand":   [1,RED,[8],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Family Restaurant": [3,RED,[9,10],2,'cup',"Take 2 coins from the active player. (opponent's turn)"],
                "Private Club":      [4,RED,[12,13,14],0,'cup',"If the active player has at least 3 landmarks built, take all of their coins. (opponent's turn)"],
               }

PROPERTIES_PURPLE={"TV Station":        [7,PURPLE,[6],5,'tower',"Take 5 coins from an opponent. (your turn only)"],
                   "Stadium":           [6,PURPLE,[6],2,'tower',"Take 2 coins each opponent. (your turn only)"],
                   "Business Center":   [8,PURPLE,[6],0,'tower',"Exchange 1 of your non 'tower' establishments for 1 an opponent owns. (your turn only)"],
                   "Publisher":         [5,PURPLE,[7],1,'tower',"Take 1 coin from each opponent for each 'cup' and 'house' establishment they own. (your turn only)"],
                   "Renovation Company":[4,PURPLE,[8],1,'tower',"Close for renovation all copies of any 1 establishment in play. Take 1 coin from each opponent for each of their establishments closed in this way. (your turn only)"],
                   "Tax Office":        [4,PURPLE,[8,9],0,'tower',"From each opponent who has 10+ coins, take half of their coins, rounded down. (your turn only)"],
                   "Tech Startup":      [1,PURPLE,[10],0,'tower',"At the end of each of your turns, you may add 1 coin to this card. When activated, take coins from each opponent equal to the amount on this card. (your turn only)"],
                   "Exhibit Hall":      [7,PURPLE,[10],0,'tower',"You may activate 1 of your non 'tower' establishments instead. If you do, return this establishment to the supply. (your turn only)"],
                   "Park":              [3,PURPLE,[11,12,13],0,'tower',"Redistribute all players' coins as evenly as possible, making up any difference with coins from the bank. (your turn only)"]
                  }

#                                    cost color rolls reward symbol description
PROPERTIES_ALL={"Bakery":            [1,GREEN,[2,3],1,'house',"Get 1 coin from the bank. (your turn only)"],
                "General Store":     [0,GREEN,[2],2,'house',"If you have less than 2 landmarks built, get 2 coins from the bank. (your turn only)"],
                "Convenience Store": [2,GREEN,[4],3,'house',"Get 3 coins from the bank. (your turn only)"],
                "Flower Shop":       [1,GREEN,[6],1,'house',"Get 3 coins from the bank for each Flower Garden you own. (your turn only)"],
                "Demolition Company":[2,GREEN,[4],8,'briefcase',"Demolish 1 of your built landmarks (flip it back over). When you do, get 8 coins from the bank. (your turn only)"],
                "Loan Office":       [-5,GREEN,[5,6],-2,'briefcase',"When built, get 5 coins from the bank. When activated, pay 2 coins to the bank. (your turn only)"],
                
                "Wheat Field":       [1,BLUE,[1],1,'grain',"Get 1 coin from the bank. (anyone's turn)"],
                "Ranch":             [1,BLUE,[2],1,'cow',"Get 1 coin from the bank. (anyone's turn)"],
                "Corn Field":        [2,BLUE,[3,4],1,'grain',"If you have less than 2 landmarks built, get 1 coin from the bank. (anyone's turn)"],
                "Flower Garden":     [2,BLUE,[4],1,'grain',"Get 1 coin from the bank. (anyone's turn)"],
                "Forest":            [3,BLUE,[5],1,'sun',"Get 1 coin from the bank. (anyone's turn)"],
                
                "Cafe":              [2,RED,[3],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Sushi Bar":         [4,RED,[1],3,'cup',"If you own a harbor, take 3 coins from the active player. (opponent's turn)"],
                "French Restaurant": [3,RED,[5],5,'cup',"If the active player has at least 2 landmarks built, take 5 coins from them. (opponent's turn)"],
                
                
                "Cheese Factory":     [5,GREEN,[7],3,'factory',"Get 3 coins from the bank for each 'cow' establishment you own. (your turn only)"],
                "Furniture Factory":  [3,GREEN,[8],3,'factory',"Get 3 coins from the bank for each 'sun' establishment you own. (your turn only)"],
                "Winery":             [3,GREEN,[9],6,'factory',"Get 6 coins from the bank for each Vineyard you own. Then close this establishment for renovation. (your turn only)"],
                "Soda Bottling Plant":[5,GREEN,[11],1,'factory',"Get 1 coin from the bank for each 'cup' establishment owned by all players. (your turn only)"],
                "Farmer's Market":    [2,GREEN,[11,12],2,'fruit',"Get 2 coins from the bank for each 'grain' establishment you own. (your turn only)"],
                "Food Warehouse":     [2,GREEN,[12,13],2,'house',"Get 2 coins from the bank for each 'cup' establishment you own. (your turn only)"],
                "Moving Company":     [2,GREEN,[9,10],4,'briefcase',"Give 1 of your non 'tower' establishments to an opponent. When you do, get 4 coins from the bank. (your turn only)"],
                
                "Vineyard":          [3,BLUE,[7],3,'grain',"Get 3 coins from the bank. (anyone's turn)"],
                "Mackerel Boat":     [2,BLUE,[8],3,'boat',"If you own a harbor, get 3 coins from the bank. (anyone's turn)"],
                "Mine":              [6,BLUE,[9],5,'sun',"Get 5 coins from the bank. (anyone's turn)"],
                "Apple Orchard":     [3,BLUE,[10],3,'grain',"Get 3 coins from the bank. (anyone's turn)"],
                "Tuna Boat":         [5,BLUE,[12,13,14],0,'boat',"The active player rolls 2 dice. If you own a harbor, get coins from the bank equal to the result. (anyone's turn)"],
                
                "Pizza Joint":       [1,RED,[7],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Hamburger Stand":   [1,RED,[8],1,'cup',"Take 1 coin from the active player. (opponent's turn)"],
                "Family Restaurant": [3,RED,[9,10],2,'cup',"Take 2 coins from the active player. (opponent's turn)"],
                "Private Club":      [4,RED,[12,13,14],0,'cup',"If the active player has at least 3 landmarks built, take all of their coins. (opponent's turn)"],
                
                
                "TV Station":        [7,PURPLE,[6],5,'tower',"Take 5 coins from an opponent. (your turn only)"], #not done!
                "Stadium":           [6,PURPLE,[6],2,'tower',"Take 2 coins each opponent. (your turn only)"],
                "Business Center":   [8,PURPLE,[6],0,'tower',"Exchange 1 of your non 'tower' establishments for 1 an opponent owns. (your turn only)"],
                "Publisher":         [5,PURPLE,[7],1,'tower',"Take 1 coin from each opponent for each 'cup' and 'house' establishment they own. (your turn only)"],
                "Renovation Company":[4,PURPLE,[8],1,'tower',"Close for renovation all copies of any 1 establishment in play. Take 1 coin from each opponent for each of their establishments closed in this way. (your turn only)"],
                "Tax Office":        [4,PURPLE,[8,9],0,'tower',"From each opponent who has 10+ coins, take half of their coins, rounded down. (your turn only)"],
                "Tech Startup":      [1,PURPLE,[10],0,'tower',"At the end of each of your turns, you may add 1 coin to this card. When activated, take coins from each opponent equal to the amount on this card. (your turn only)"],
                "Exhibit Hall":      [7,PURPLE,[10],0,'tower',"You may activate 1 of your non 'tower' establishments instead. If you do, return this establishment to the supply. (your turn only)"],
                "Park":              [3,PURPLE,[11,12,13],0,'tower',"Redistribute all players' coins as evenly as possible, making up any difference with coins from the bank. (your turn only)"]
               }

#lists of names of properties with certain symbols to help with income for properties based on number of 'symbol' properties owned
PROPERTIES_COW=[]
PROPERTIES_SUN=[]
PROPERTIES_CUP=[]
PROPERTIES_GRAIN=[]
PROPERTIES_HOUSE=[]
for name in list(PROPERTIES_ALL):
    if PROPERTIES_ALL[name][4]=='cow':
        PROPERTIES_COW.append(name)
    elif PROPERTIES_ALL[name][4]=='sun':
        PROPERTIES_SUN.append(name)
    elif PROPERTIES_ALL[name][4]=='cup':
        PROPERTIES_CUP.append(name)
    elif PROPERTIES_ALL[name][4]=='grain':
        PROPERTIES_GRAIN.append(name)
    elif PROPERTIES_ALL[name][4]=='house':
        PROPERTIES_HOUSE.append(name)
# print(PROPERTIES_COW,PROPERTIES_SUN,PROPERTIES_CUP,PROPERTIES_GRAIN,PROPERTIES_HOUSE)

class Card():
    def __init__(self,name,price,type,description):
        self.name=name #name of card
        self.price=price #price of card
        self.type=type #type of card (property or landmark)
        self.description=description
        if self.type=='landmark':
            self.symbol='tower'
        else:
            self.symbol=PROPERTIES_ALL[name][4]
        
class LandmarkCard(Card):
    def __init__(self,name):
        Card.__init__(self,name,LANDMARKS[name][0],'landmark',LANDMARKS[name][1])
        self.active=False #whether or not card power is being used
        
class PropertyCard(Card):
    def __init__(self,name):
        Card.__init__(self,name,PROPERTIES_ALL[name][0],'property',PROPERTIES_ALL[name][5])
        self.color=PROPERTIES_ALL[name][1] #color of card: blue, green, red, or purple
        self.rolls=PROPERTIES_ALL[name][2] #numbers that activate card
        self.reward=PROPERTIES_ALL[name][3] #reward for rolling number to activate card
        self.renovating=False #tag for whether card is under renovation or not, starts False
        
        
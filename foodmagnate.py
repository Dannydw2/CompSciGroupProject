# here is you code in an easy to pint pormat ready to confuse your computer science teacher

# Skeleton Program code for the AQA A Level Paper 1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# wr




# here is you code in an easy to pint pormat ready to confuse your computer science teacher

# Skeleton Program code for the AQA A Level Paper 1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.5.1 programming environment

import math      # used for distance calculations (e.g. Pythagoras)
import random    # used for randomness in simulation

#-------------------------------------------------------------------------------------
#--------------------------------your house class-------------------------------------
#-------------------------------------------------------------------------------------

class Household:
  _NextID = 1   # class variable to give each household a unique ID

  def __init__(self, X, Y):
    self._XCoord = X   # store X position
    self._YCoord = Y   # store Y position
    self._ChanceEatOutPerDay = random.random()  # random probability (0–1) of eating out
    self._ID = Household._NextID   # assign unique ID
    Household._NextID += 1         # increment ID for next household

  def GetDetails(self):
    # returns formatted string of household info
    Details = str(self._ID) + "     Coordinates: (" + str(self._XCoord) + ", " + str(self._YCoord) + ")     Eat out probability: " + str(self._ChanceEatOutPerDay)
    return Details

  def GetChanceEatOut(self):
    return self._ChanceEatOutPerDay   # returns probability of eating out

  def GetX(self):
    return self._XCoord   # returns X coordinate

  def GetY(self):
    return self._YCoord   # returns Y coordinate

#-------------------------------------------------------------------------------------
#----------------------------your settlment class-------------------------------------
#-------------------------------------------------------------------------------------

class Settlement:
  def __init__(self):
    self._XSize = 1000   # width of map
    self._YSize = 1000   # height of map
    self._StartNoOfHouseholds = 250   # initial households
    self._Households = []             # list to store households
    self._CreateHouseholds()          # populate initial households
 
  def GetNumberOfHouseholds(self):
    return len(self._Households)   # returns total households

  def GetXSize(self):
    return self._XSize   # returns width

  def GetYSize(self):
    return self._YSize   # returns height

  def GetRandomLocation(self):
    # generates random coordinate within settlement
    X = random.randint(0, self._XSize - 1)
    Y = random.randint(0, self._YSize - 1)
    return X, Y

  def _CreateHouseholds(self):
    # creates starting households
    for Count in range (0, self._StartNoOfHouseholds):
      self.AddHousehold()

  def AddHousehold(self):
    # creates and adds one household
    X, Y = self.GetRandomLocation()
    Temp = Household(X, Y)
    self._Households.append(Temp)

  def DisplayHouseholds(self):
    # prints all household info
    print("\n**********************************")
    print("*** Details of all households: ***")
    print("**********************************\n")
    for H in self._Households:
      print(H.GetDetails())
    print()

  def FindOutifHouseholdEatsOut(self, HouseholdNo):
    # determines if a household eats out today
    EatOutRNo = random.random()
    X = self._Households[HouseholdNo].GetX()
    Y = self._Households[HouseholdNo].GetY()
    if EatOutRNo < self._Households[HouseholdNo].GetChanceEatOut():
      return True, X, Y   # they eat out
    else:
      return False, X, Y  # they stay home
    
#-------------------------------------------------------------------------------------
#----------------------------your large settlment class-------------------------------
#-------------------------------------------------------------------------------------

class LargeSettlement(Settlement):
  def __init__(self, ExtraXSize, ExtraYSize, ExtraHouseholds):
    super(LargeSettlement, self).__init__()  # call parent constructor
    self._XSize += ExtraXSize
    self._YSize += ExtraYSize
    self._StartNoOfHouseholds += ExtraHouseholds
    # add extra households
    for Count in range (1, ExtraHouseholds + 1):
      self.AddHousehold()

#-------------------------------------------------------------------------------------
#----------------------------your outlet class----------------------------------------
#-------------------------------------------------------------------------------------

class Outlet:
  def __init__(self, XCoord, YCoord, MaxCapacityBase):
    self._XCoord = XCoord
    self._YCoord = YCoord
    self._Capacity = int(MaxCapacityBase * 0.6)  # starting capacity (60%)
    # random variation in max capacity
    self._MaxCapacity = MaxCapacityBase + random.randint(0, 49) - random.randint(0, 49)
    # calculate daily costs
    self._DailyCosts = MaxCapacityBase * 0.2 + self._Capacity * 0.5 + 100
    self.NewDay()

  def GetCapacity(self):
    return self._Capacity

  def GetX(self):
    return self._XCoord

  def GetY(self):
    return self._YCoord

  def AlterDailyCost(self, Amount):
    self._DailyCosts += Amount   # adjust daily cost

  def AlterCapacity(self, Change):
    # change outlet capacity with limits
    OldCapacity = self._Capacity
    self._Capacity += Change
    if self._Capacity > self._MaxCapacity:
      self._Capacity = self._MaxCapacity
      return self._MaxCapacity - OldCapacity
    elif self._Capacity < 0:
      self._Capacity = 0
    # recalculate costs after change
    self._DailyCosts = self._MaxCapacity * 0.2 + self._Capacity * 0.5 + 100
    return Change

  def IncrementVisits(self):
    self._VisitsToday += 1   # increase customer count
       
  def NewDay(self):
    self._VisitsToday = 0   # reset visits each day

  def CalculateDailyProfitLoss(self, AvgCostPerMeal, AvgPricePerMeal):
    # profit = (profit per meal × visits) - daily costs
    return (AvgPricePerMeal - AvgCostPerMeal) * self._VisitsToday - self._DailyCosts

  def GetDetails(self):
    # return outlet details
    Details = "Coordinates: (" + str(self._XCoord) + ", " + str(self._YCoord) + ")     Capacity: " + str(self._Capacity) + "      Maximum Capacity: "
    Details += str(self._MaxCapacity) + "      Daily Costs: " + str(self._DailyCosts) + "      Visits today: " + str(self._VisitsToday)
    return Details
  
#-------------------------------------------------------------------------------------
#----------------------------your company class---------------------------------------
#-------------------------------------------------------------------------------------

class Company:
  def __init__(self, Name, Category, Balance, X, Y, FuelCostPerUnit, BaseCostOfDelivery):
    self._Outlets = []   # list of outlets
    # cost values for outlet types
    self._FamilyOutletCost = 1000
    self._FastFoodOutletCost = 2000
    self._NamedChefOutletCost = 15000
    # capacity values
    self._FamilyFoodOutletCapacity = 150
    self._FastFoodOutletCapacity = 200        
    self._NamedChefOutletCapacity = 50
    self._Name = Name
    self._Category = Category
    self._Balance = Balance
    self._FuelCostPerUnit = FuelCostPerUnit
    self._BaseCostOfDelivery = BaseCostOfDelivery
    self._ReputationScore = 100
    self._DailyCosts = 100

    # set pricing based on business type
    if self._Category == "fast food":
      self._AvgCostPerMeal = 5
      self._AvgPricePerMeal = 10
      self._ReputationScore += random.random() * 10 - 8
    elif self._Category == "family":
      self._AvgCostPerMeal = 12
      self._AvgPricePerMeal = 14
      self._ReputationScore += random.random() * 30 - 5
    else:
      self._AvgCostPerMeal = 20
      self._AvgPricePerMeal = 40
      self._ReputationScore += random.random() * 50

    self.OpenOutlet(X, Y)  # open first outlet

  # (methods below mostly manage company data, outlets, and finances)

  def AddVisitToNearestOutlet(self, X, Y):
    # find nearest outlet using distance formula
    NearestOutlet = 0
    NearestOutletDistance = math.sqrt((self._Outlets[0].GetX() - X) ** 2 + (self._Outlets[0].GetY() - Y) ** 2)
    for Current in range (1, len(self._Outlets)):
      CurrentDistance = math.sqrt((self._Outlets[Current].GetX() - X) ** 2 + (self._Outlets[Current].GetY() - Y) ** 2)
      if CurrentDistance < NearestOutletDistance:
        NearestOutletDistance = CurrentDistance
        NearestOutlet = Current
    self._Outlets[NearestOutlet].IncrementVisits()

  def ProcessDayEnd(self):
    # calculates daily profit/loss for company
    Details = ""
    ProfitLossFromOutlets = 0

    if len(self._Outlets) > 1:
      DeliveryCosts = self._BaseCostOfDelivery + self.CalculateDeliveryCost()
    else:
      DeliveryCosts = self._BaseCostOfDelivery

    for Current in range (0, len(self._Outlets)):
      ProfitLossFromThisOutlet = self._Outlets[Current].CalculateDailyProfitLoss(self._AvgCostPerMeal, self._AvgPricePerMeal)
      ProfitLossFromOutlets += ProfitLossFromThisOutlet

    # update balance
    self._Balance += ProfitLossFromOutlets - self._DailyCosts - DeliveryCosts
    return Details

#-------------------------------------------------------------------------------------
#----------------------------your simulation class------------------------------------
#-------------------------------------------------------------------------------------

class Simulation:
  def __init__(self):
    self._Companies = []
    self._FuelCostPerUnit = 0.0098
    self._BaseCostforDelivery = 100

    # choose settlement size
    Choice = input("Enter L for a large settlement, anything else for a normal size settlement: ")
    if Choice == "L":
      ExtraX = int(input("Enter additional amount to add to X size of settlement: "))
      ExtraY = int(input("Enter additional amount to add to Y size of settlement: "))
      ExtraHouseholds = int(input("Enter additional number of households to add to settlement: "))
      self._SimulationSettlement = LargeSettlement(ExtraX, ExtraY, ExtraHouseholds)
    else:
      self._SimulationSettlement = Settlement()

  def ProcessDayEnd(self):
    # simulate one full day
    TotalReputation = 0.0
    Reputations = []

    # calculate cumulative reputation (used for weighted random choice)
    for C in self._Companies:
      C.NewDay()
      TotalReputation += C.GetReputationScore()
      Reputations.append(TotalReputation)

    # loop through households
    LoopMax = self._SimulationSettlement.GetNumberOfHouseholds() - 1
    for Counter in range (0, LoopMax + 1):
      EatsOut, X, Y = self._SimulationSettlement.FindOutifHouseholdEatsOut(Counter)

      if EatsOut:
        # pick company based on reputation
        CompanyRNo = random.randint(1, int(TotalReputation))
        Current = 0
        while Current < len(Reputations):
          if CompanyRNo < Reputations[Current]:
            self._Companies[Current].AddVisitToNearestOutlet(X, Y)
            break
          Current += 1

#-------------------------------------------------------------------------------------
#-----------------------------------main program--------------------------------------
#-------------------------------------------------------------------------------------

def Main():
  ThisSim = Simulation()  # create simulation
  ThisSim.Run()           # run simulation loop

if __name__ == "__main__":
  Main()

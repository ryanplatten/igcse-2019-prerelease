
# The functions needed for each section are listed below before the main section of the program

# This is task 1 - entering the items -------------------------------
def itemEntry(itemDescripton, reservePrice, highestBid, mostRecentBid, bidderNumber, noOfBids):
    item = input("What is the description of the item? ")
    itemDescripton.append(item)
    reserve = int(input("What is the reserve price of the item? "))
    reservePrice.append(reserve)
    highestBid.append(0)
    mostRecentBid.append(0)
    bidderNumber.append(0)
    noOfBids.append(0)
    sold.append("No")
    auctionCompanyFee.append(0)


# Part of task 2 - viewing the items ---------------------------------
def viewItem():
    answer = int(input("Which item would you like to view the details of? "))
    print("The item is " + str(itemDescription[answer]) + " and has a reserve price of $" + str(reservePrice[answer]))
    print("The highest bid so far is $" + str(highestBid[answer]))


# Part of task 2 - bidding on items
def bidOnItem():
    itemNumber = int(input("Which item number are you bidding on? "))
    print("You are bidding on " + str(itemDescription[itemNumber]))
    bid = int(input("What is your bid price? "))
    mostRecentBid[itemNumber] = bid
    bidBidderNumber = input("What is your bidder number? ")
    noOfBids[itemNumber] = noOfBids[itemNumber] + 1
    if bid > highestBid[itemNumber] and bid > reservePrice[itemNumber]:
        highestBid[itemNumber] = bid
        bidderNumber[itemNumber] = bidBidderNumber
        print("Your bid is now the highest for " + str(itemDescription[itemNumber]) + ".")
    else:
        print("You will have to submit a higher bid.")

# The following functions are parts of task 3 ------------------------

# Check the items that reach the reserve price and update them to Sold and allocate a 10% fee to the auction company
def reservePriceReached(itemDescripton, reservePrice, highestBid, auctionCompanyFee):
    count = 0
    for i in itemDescription:
        if highestBid[count] >= reservePrice[count]:
            sold[count] = "Yes"
            auctionCompanyFee[count] = highestBid[count] / 100 * 10
        count = count + 1


# Calculate the total fees the auction company will receive on sold items
def totalAuctionCompanyFee():
    totalFeeReceived = sum(auctionCompanyFee)
    print("The total fees received by the auction company for this auction are: $" + str(totalFeeReceived))


# Calculate the total sales for the auction including the fees
def totalFeeForAllItems():
    totalFees = sum(highestBid)
    print("The total sum received today including bids and fees is $" + str(totalFees))


# Display a list of the items that did not reach the reserve price but did receive bids.
# If there were none, then display "None"
def itemsNotSoldButBidOn():
    print("The following items received bids, but did not meet the reserve price:")
    count = 0
    bidOnItems = 0
    for i in itemDescription:
        if sold[count] == "No" and mostRecentBid[count] != 0:
            print("Item number " + str(count) + " had a bid of $" + str(mostRecentBid[count]) + ".")
            bidOnItems = bidOnItems + 1
        count = count + 1
    if bidOnItems == 0:
        print("None")


# Display all items that received no bids
def itemsNotBidOn():
    print("The following items received no bids:")
    count = 0
    noBids = 0
    for i in itemDescription:
        if sold[count] == "No" and mostRecentBid[count] == 0:
            print("Item number " + str(count) + " received no bids.")
            noBids = noBids + 1
        count = count + 1
    if noBids == 0:
        print("None")


# Calculate and display the final numbers from the auction
def finalNumbers(sold, mostRecentBid, noOfBids):
    noOfItemsSold = 0
    noOfItemsNotMeetingReserve = 0
    noOfItemsWithNoBids = 0
    count = 0
    for i in itemDescription:
        if sold[count] != "No":
            noOfItemsSold = noOfItemsSold + 1
        if sold[count] == "No" and mostRecentBid[count] != 0:
            noOfItemsNotMeetingReserve = noOfItemsNotMeetingReserve + 1
        if noOfBids[count] == 0:
            noOfItemsWithNoBids = noOfItemsWithNoBids + 1
        count = count + 1
    print("The total number of items sold was " + str(noOfItemsSold) + ".")
    print("The number of items that did not meet their reserve price was " + str(noOfItemsNotMeetingReserve) + ".")
    print("The number of items that received no bids was " + str(noOfItemsWithNoBids) + ".")


# ----------------------------------------------------------------------

# The following lines set up the arrays needed to store all of the information (some items added for data validation)
itemDescription = ["Blue Coat", "Red Hat", "Furry Mittens"]
reservePrice = [12, 15, 45]
highestBid = [0, 0, 0]
mostRecentBid = [0, 0, 0]
bidderNumber = [0, 0, 0]
noOfBids = [0, 0, 0]
sold = ["No", "No", "No"]
auctionCompanyFee = [0, 0, 0]

# ---------------------The main program begins now--------------------

print("Welcome to the auction!")
moreItems = "y"
print("Please enter the first item up for auction.")

# This is the main part where the auctioneer can enter items in to be bid on
while moreItems == "y":
    itemEntry(itemDescription, reservePrice, highestBid, mostRecentBid, bidderNumber, noOfBids)
    moreItems = input("Would you like to enter another item for auction? (y/n)")
    moreItems.lower()

#The following loops through the description list to give the bidder the name and item number
print("The auction items for today are:")
itemNo = 0
for i in itemDescription:
    description = itemDescription[itemNo]
    print(str(itemNo) + " " + str(description))
    itemNo = itemNo + 1

#The next part asks the bidder whether they would like additional information on any items
doYouWantToView = input("Would you like to view any items up for auction? (y/n)")
while doYouWantToView == "y":
    viewItem()
    doYouWantToView = input("Would you like to view another item? (y/n)")

#This is the main loop where bidders can submit bids
doYouWantToBid = input("Would you like to bid on an item? (y/n)")
while doYouWantToBid == "y":
    bidOnItem()
    doYouWantToBid = input("Would you like to submit another bid? (y/n)")

reservePriceReached(itemDescription, reservePrice, highestBid, auctionCompanyFee)

print(sold)
print(mostRecentBid)
print(highestBid)

totalAuctionCompanyFee()
totalFeeForAllItems()
itemsNotSoldButBidOn()
itemsNotBidOn()
finalNumbers(sold, mostRecentBid, noOfBids)







from art import logo
print(logo)


last_bidder = False
list_of_bidders = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while last_bidder == False:
    name = input("What is your name ?: ")
    price = int(input("What is your bid ?: $ "))
    list_of_bidders.update({name: price})
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if more_bidders == 'no':
        find_highest_bidder(list_of_bidders)
        last_bidder = True
    else:
        print("\n" * 40)



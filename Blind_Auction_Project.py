from art1 import logo
print(logo)

def func_for_finding_highest_bidder(bidding_system):
    highest_bid = 0
    winner = " "
    for bidder in bidding_system:
        bid_amount = bidding_system[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? : ")
    bid = int(input("What is your bid?:"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=="no":
        continue_bidding = False
        func_for_finding_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n" * 20)











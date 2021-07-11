import time as t


def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


auction = {}
highest = 0
flag = 'yes'
while flag == 'yes':
    name = input("What's your name? ")
    amount = int(input("What's your bid? $"))
    if amount > highest:
        highest = amount
    auction[amount] = name
    flag = input("Are there any other bidders? 'yes' or 'no'\n").lower()
    if flag == 'yes':
        clear()
print(f"Highest Bid is :{highest} by {auction[highest]}")
for i in range(3, 0, -1):
    print(i)
    t.sleep(2)
print(f"Sold to {auction[highest].upper()}!")

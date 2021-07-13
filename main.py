import time as t


def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction = {}
highest = 0
flag = 'yes'
print(logo)
print("Welcome to the Auction House")
while flag == 'yes':
    name = input("What's your name? ")
    amount = int(input("What's your bid? $"))
    if amount > highest:
        highest = amount
    auction[amount] = name
    flag = input("Are there any other bidders? 'yes' or 'no'\n").lower()
    if flag == 'yes':
        clear()
print(f"Highest Bid is ${highest} by {auction[highest].upper()}")
for i in range(3, 0, -1):
    print(i)
    t.sleep(1)
print(f"Sold to {auction[highest].upper()}!")

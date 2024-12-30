import random
import art
import game_data


"""" Function to compare the followers"""
def compare_followers(account_1,account_2):
    account_a_followers = account_1["follower_count"]
    account_b_followers = account_2["follower_count"]
    if account_a_followers >account_b_followers:
        #print(account_a_followers)
        return choice == "a"
    else:
        #print(account_b_followers)
        return choice == "b"

"""" Function to extract the account details"""
def account_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(game_data.data)

while game_should_continue:
    account_a = account_b

    if account_a == account_b:
        account_b = random.choice(game_data.data)

    account_a_details = account_data(account_a)
    account_b_details = (account_data(account_b))

    print(f"Compare A: {account_a_details}")

    print(art.vs)

    print(f"Compare B: {account_b_details}")

    choice = input("Who has more followers? Type 'A' or 'B':").lower()
    more_followers = compare_followers(account_a,account_b)

    if more_followers:
        score += 1
        print(f"Your score is {score}")
    else:
        game_should_continue = False

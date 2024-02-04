team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kavin", "age": 31, "number": 12},
]


def repr_players(players: list[dict]):
    for player in players:
        print(f"\t[Player {player['number']}]: {player['name']}, {player['age']}")


def player_add(name: str, age: int, number: int):
    for num in team:
        if num["number"] == number:
            print("There is a player with this number\n")
            return
    player: dict = {"name": name, "age": age, "number": number}
    team.append(player)
    print(f"a new player has been added under number'{number}'")


def player_delete(number: int):
    for player in team:
        if player["number"] == number:
            team.remove(player)
            print(f"player numbered '{number}' removed")


def player_update(number_old: int, number_new: int):
    for player in team:
        if player["number"] == number_old:
            player["number"] = number_new
            print(
                f"""player number '{number_old}' has changed now plays under 
                number '{number_new}'"""
            )


def main():
    operations = ("add", "del", "repr", "change", "exit")

    while True:
        operation = input("Please enter the operation (add, del, repr, change, exit): ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue
        if operation == "exit":
            print("bye")
            break
        elif operation == "del":
            user_del = int(input("Enter the player number: "))
            player_delete(user_del)
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input("Enter new player information(name, age, number)")
            user_items: list[str] = user_data.split(",")
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("age and number of player must be integers\n\n")
                continue
        elif operation == "change":
            number_old = input("enter old player number: ")
            number_new = input("enter new player number: ")
            try:
                player_update(number_old=int(number_old), number_new=int(number_new))
            except ValueError:
                print("number of player must be integers\n\n")
                continue
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()

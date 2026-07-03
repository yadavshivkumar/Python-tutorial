seat_type = input("Enter seat type(sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("You have selected a sleeper seat.")
    case "ac":
        print("You have selected an AC seat.")
    case "general":
        print("You have selected a general seat.")
    case "luxury":
        print("You have selected a luxury seat.")
    case _:
        print("Invalid seat type.")

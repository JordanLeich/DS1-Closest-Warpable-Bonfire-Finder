def find_closest_bonfire(boss=None):
    bonfire_locations = {
        "Asylum Demon": "Firelink Shrine",
        "Bell Gargoyle": "Altar of Sunlight or Undead Parish",
        "Capra Demon": "Firelink Shrine",
        "Ceaseless Discharge": "Daughter of Chaos",
        "Centipede Demon": "Daughter of Chaos",
        "Chaos Witch Quelaag": "Firelink Shrine",
        "Crossbreed Priscilla": "Painted World of Ariamis",
        "Dark Sun Gwyndolin": "Darkmoon Tomb",
        "Demon Firesage": "Daughter of Chaos",
        "Firelink Shrine": "Firelink Shrine",
        "Gaping Dragon": "Depths",
        "Great Grey Wolf Sif": "Undead Parish",
        "Gwyn Lord of Cinder": "Firelink Shrine",
        "Iron Golem": "Undead Parish",
        "Moonlight Butterfly": "Undead Parish",
        "Nito": "Catacombs (Remastered version only, otherwise Firelink Shrine)",
        "Pinwheel": "Firelink Shrine",
        "Ornstein and Smough": "Anor Londo or Darkmoon Tomb",
        "Seath the Scaleless": "The Duke's Archives",
        "Stray Demon": "Firelink Shrine",
        "Taurus Demon": "Firelink Shrine",
        "The Bed of Chaos": "Daughter of Chaos",
        "Artorias the Abysswalker": "Oolacile Sanctuary",
        "Black Dragon Kalameet": "Oolacile Township",
        "Manus, Father of the Abyss": "Oolacile Township",
        "Sanctuary Guardian": "Sanctuary Garden"
    }

    if boss is None:
        return list(bonfire_locations.keys())  # Return all boss names when no argument is provided

    # Case-insensitive matching for boss names
    boss = next((k for k in bonfire_locations.keys() if k.lower() == boss.lower()), None)

    return bonfire_locations.get(boss, "Invalid boss name or number.")


def display_boss_names():
    print("Select the boss you are trying to reach with the Lordvessel:")
    for boss_num, boss_name in enumerate(find_closest_bonfire(), start=1):
        print(f"{boss_num}: {boss_name}")


def main():
    while True:
        display_boss_names()

        try:
            user_input = input("Enter the boss name or its number: ").strip()

            if user_input.isdigit():  # If the input is a number, convert it to an integer
                user_input = int(user_input)

                if 1 <= user_input <= len(find_closest_bonfire()):
                    user_input = list(find_closest_bonfire())[user_input - 1]
                else:
                    raise ValueError("Invalid boss number.")

            closest_bonfire = find_closest_bonfire(user_input)
            print(f"The closest warpable bonfire to {user_input} is: {closest_bonfire}")

            while True:
                another_boss = input("Do you want to find another boss location? (Y/N): ").strip().lower()
                if another_boss in ('y', 'n'):
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")

            if another_boss == 'n':
                break

        except ValueError as e:
            print(e)
            print("Invalid input. Please enter a valid boss name or number.")


if __name__ == "__main__":
    main()
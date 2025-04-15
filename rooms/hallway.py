from time import daylight


class Hallway:
    def get_description(self):
        return (
            "Nyní se nacházíš v dlouhé, studené chodbě."
            "Na stěnách visí pochodně. Cesta vede dál na do žaláře  a zpět do cely .\n"
            "Příkazy: jdi zpět, porozhlednout"
        )
    def handle_command(self, command):
        if command == "jdi zpět":
            from rooms.start_room import StartRoom
            print("Vracíš se zpět do cely...")
            return StartRoom()

        elif command == "porozhlednout":
            print("Vidíš pavučiny, starý nápis na stěně: Kdo vstoupí, už nevyjde .")
            return None

        else:
            print("tímto směrem nemůžeš jít ")
            return None

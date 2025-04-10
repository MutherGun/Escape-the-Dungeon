class Hallway:
    def get_description(self):
        return (
            "Nyní se nacházíš v dlouhé, studené chodbě."
            "Na stěnách visí pochodně. Cesta vede dál na sever a zpět na jih .\n"
            "Příkazy: go south, look around"
        )
    def handle_command(self, command):
        if command == "go south":
            from rooms.start_room import StartRoom
            print("Vracíš se zpět do cely...")
            return StartRoom()

        elif command == "look around":
            print("Vidíš pavučiny, starý nápis na stěně: Kdo vstoupí, už nevyjde .")
            return None

        else:
            print("tímto směrem nemůžeš jít ")
            return None

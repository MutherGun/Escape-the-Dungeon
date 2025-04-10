from rooms.hallway import Hallway

class StartRoom:
    def get_description(self):
        return (
            "Nacházíš se v temné cele. "
            "Jediné světlo sem proniká malým okénkem s mříží. "
            "Dveře na sever jsou pootevřené.\n"
            "Příkazy: go north, look around, exit"
        )
    def handle_command(self, command):
        if command == "go north":
            print("otevíráš dveře a vsupuješ do temné chodby...")
            return Hallway()
        elif command == "look around":
            print("Vidíš starou postel , zrezivělý zámek a spoustu prachu. ")
            return None
        else:
            print("Nerozumím tomuto příkazu.")
            return None
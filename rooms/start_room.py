from rooms.hallway import Hallway

class StartRoom:
    def get_description(self):
        return (
            "Nacházíš se v temné cele. "
            "Jediné světlo sem proniká malým okénkem s mříží. "
            "Dveře z cely jsou pootevřené.\n"
            "Příkazy: vyjdi ven , porozhlednout, konec"
        )
    def handle_command(self, command):
        if command == "vyjdi ven":
            print("otevíráš dveře a vsupuješ do temné chodby...")
            return Hallway()
        elif command == "porozhlednout":
            print("Vidíš starou postel , zrezivělý zámek a spoustu prachu. ")
            return None
        else:
            print("Nerozumím tomuto příkazu.")
            return None
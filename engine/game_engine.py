class GameEngine:
    def __init__(self, start_room):
        self.current_room = start_room
        self.is_running = True

    def run(self):
        while self.is_running:
            self.show_room()
            player_input = input("> ").strip().lower()
            self.handle_input(player_input)

    def show_room(self):
        print("\n" + "=" * 40)
        print(self.current_room.get_description())
        print("=" * 40)

    def handle_input(self, command):
        if command == "exit" or command == "quit":
            print("Ukončuji hru. Díky za hraní!")
            self.is_running = False

        else:
            next_room = self.current_room.handle_command(command)
            if next_room:
                self.current_room = next_room
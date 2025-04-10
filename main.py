from engine.game_engine import GameEngine
from rooms.start_room import StartRoom

def main():
    print("Vítej ve hře Escape the Dungeon")
    start_room = StartRoom()
    engine = GameEngine(start_room)
    engine.run()

if __name__ == "__main__":
    main()
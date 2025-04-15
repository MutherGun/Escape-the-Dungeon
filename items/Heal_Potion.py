from item import Item

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "Restore 20 HP.")

    def use(self, player):
        healed = min(20, player.max.health - player.health)
        player.health += healed
        print(f"Použil jsi Lektvar Zdraví  a obnovil {healed} životů! Nyní máš {player.health}/{player.max_health} HP.")